<?php
require_once ('mysql_connect.php');

class fetch_dataset extends db_connect {

	protected $convictBigTable; /* Name of the convictBigTable */
	protected $rabBigTable; /* Name of the rabBigTable */

	/*
	 * Desired functionality:
	 * return a certain dataset based upon special criteria
	 * link two datasets in a new table
	 * create foreign keys between tables
	 */

	/*
	 * Remove a view from the DB
	 * @param string $viewname
	 * @return true/false
	 */
	protected function destroy_view_bigtable ($viewname) {
		$viewname = $this->c->real_escape_string ($viewname);
		$q = "DROP VIEW %s";
		$q = sprintf ($q, $viewname);
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		return true;
	}

	protected function scrub_sql (&$var) {
		$var = $this->c->real_escape_string ($var);
	}

	/*
	 * Escape table & column names
	 * @param stringref $table
	 */
	protected function escape_sql_attr (&$var) {
		$var = '`'.$var.'`'; /*NOTGOOD*/
	}

	/*
	 * Function to get the names of the columns for a certain table.
	 * @param string $table_name
	 * @return array $columns[i] = $column
	 */
	public function get_column_names ($table_name) {
		$columns = array ();
		$t = $this->c->real_escape_string ($table_name);
		$q = "SHOW COLUMNS FROM `%s`";
		$q = sprintf ($q, $t);
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		while ($row = $r->fetch_assoc ()) {
			array_push ($columns, $row['Field']);
		}
		return $columns;
	}

	/*
	 * Function to create a bigtable view with all information pertaining to convicts
	 * Recreate for every session
	 * @return true/false
	 */
	protected function create_view_convictBigTable () {
		$bigTableName = 'convictBigTable'.time ();
		$q = "CREATE VIEW `%s`.`%s` AS
		SELECT g.Id_gedetineerde, v.Id_verblijf, v.Rolnummer, v.Inschrijvingsdatum_d, v.Inschrijvingsdatum_m, v.Inschrijvingsdatum_j, v.Leeftijd, v.Lichaamslengte_m, v.Lichaamslengte_andere, v.Lichaamsgewicht_opname, v.Lichaamsgewicht_ontslag, v.Haarkleur, v.Ontslagdatum_d, v.Ontslagdatum_m, v.Ontslagdatum_j, g.Voornaam, g.Naam, g.Geslacht, g.Geboortejaar, p.Plaatsnaam_vertaling as Geboorteplaats, w.Plaatsnaam_vertaling as Woonplaats
		FROM Verblijf v, Gedetineerde g, Geboorteplaats p, Woonplaats w WHERE
		w.Id_verbl = v.Id_verblijf AND
		g.Id_gedetineerde = v.Id_ged AND
		p.Id_verbl = v.ID_verblijf;";
		$q = sprintf ($q, $this->c->real_escape_string ($this->d), $bigTableName);
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		$this->convictBigTable = $bigTableName;
		/*INSERT INTO `ewout_doctoraat_16012015`.`prisonerBigTable_normalised`
(`p_ID`,
`Inschrijvingsdatum`,
`Geboorteplaats`,
`Leeftijd`)
SELECT `prisonerBigTable`.`Id_gedetineerde`,
    STR_TO_DATE(CONCAT(`prisonerBigTable`.`Inschrijvingsdatum_d`, '/', `prisonerBigTable`.`Inschrijvingsdatum_m`, '/',  `prisonerBigTable`.`Inschrijvingsdatum_j`, ' 0:00:00'),'%e/%c/%Y %k:%i:%s'),
    `prisonerBigTable`.`Geboorteplaats`,
    `prisonerBigTable`.`Leeftijd`
FROM `ewout_doctoraat_16012015`.`prisonerBigTable`;

*/
		return true;
	}

	/*
	 * Function to create a bigtable view from the table RAB_geboortes
	 * Recreate for every session
	 * @return true/false
	 */
	protected function create_view_rabBigTable () {
		$bigTableName = 'rabBigTable'.time ();
		$q = "CREATE VIEW `%s`.`%s` AS
		SELECT g.UUID, g.geboorteplaats, g.`onvolledige datum`, g.Aktedatum, g.geboortedatum, g.Voornaam, g.Naam, g.jaar FROM RAB_geboortes g
		WHERE
		g.`Beroep vader` IS NOT NULL AND
		g.`Beroep vader` NOT LIKE '';";
		$q = sprintf ($q, $this->c->real_escape_string ($this->d), $bigTableName);
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		$this->rabBigTable = $bigTableName;
		return true;
	}

	/*
	 * Function to return a list of Geboorteplaatsen from prisonerBigTable_normalised
	 * @return array $geboorteplaatsen
	 */
	public function select_gb_from_prisonerBT_normalised () {
		$result = array ();
		$q = "SELECT DISTINCT `Geboorteplaats` FROM `prisonerBigTable_normalised` WHERE `Geboorteplaats` IS NOT NULL AND `Geboorteplaats` <> 'Onbekend'";
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		while ($row = $r->fetch_assoc ()) {
			array_push ($result, $row['Geboorteplaats']);
		}
		return $result;
	}
	

	protected function normalise_rabGeboortes () {
		$q = "";
		$q = "INSERT INTO `RAB_geboortes_normalised`(`UUID`, `ACCESS_ID`, `Microfilmnummer`, `Inventarisnummer`, `Geboorteplaats`, `Aktenummer`, `Datum_onvolledig`, `Datum_Republikeins`, `Aktedatum`, `Geboortedatum`, `Voornaam`, `Naam`, `Vader_voornaam`, `Vader_naam`, `Moeder_voornaam`, `Moeder_naam`, `Straat`, `Huisnummer`, `Wijk`, `Doodgeboren`, `Geslacht`, `Opmerkingen`, `Vader_leeftijd`, `Vader_geboorteplaats`, `Vader_geboortedatum`, `Vader_woonplaats`, `Vader_beroep`, `Vader_opmerking`, `Moeder_leeftijd`, `Moeder_geboorteplaats`, `Moeder_geboortedatum`, `Moeder_woonplaats`, `Moeder_beroep`, `Moeder_opmerking`, `Jaar`) SELECT `UUID`, `Id`, `Microfilmnummer`, `Inventarisnummer`, `geboorteplaats`, `Aktenummer`, `onvolledige datum`, `Republikeinse datum`, STR_TO_DATE(`Aktedatum`,'%e/%c/%Y %k:%i:%s'), STR_TO_DATE(`geboortedatum`,'%e/%c/%Y %k:%i:%s'), `Voornaam`, `Naam`, `Voornaam vader`, `Naam vader`, `Voornaam moeder`, `Naam moeder`, `straat`, `huisnummer`, `wijk`, `doodgeboren`, `geslacht`, `Opmerkingen`, `Leeftijd vader`, `Geboorteplaats vader`, `Geboortedatum vader`, `Woonplaats vader`, `Beroep vader`, `opmerking vader`, `Leeftijd moeder`, `Geboorteplaats moeder`, `Geboortedatum moeder`, `Woonplaats moeder`, `Beroep moeder`, `opmerking moeder`, `jaar` FROM `RAB_geboortes`;";
		/* Convert dates to MYSQL-dates 
		 * SELECT STR_TO_DATE('25/8/1851 0:00:00','%e/%c/%Y %k:%i:%s');*/
	}

	protected function normalise_prisonerBigTable () {
	}

	/*
	 * Select certain columns based on a set of WHERE-clauses (AND) in the convictBigTable
	 * @param array $columns_to_select
	 * @param array $where_clause[i] = array [column, comparison, value] (e.g. $where_clause[foo, =, bar])
	 * @return $array[i] = $row[cname => value]
	 */
	public function select_from_convictBigTable ($columns_to_select, $where_clauses) {
		$result = array ();
		if (!isset ($this->convictBigTable) || $this->convictBigTable == '') {
			/* View not yet created - create it */
			if ($this->create_view_convictBigTable () != true) {
				throw new Exception ("Error: failed creating view: ".$this->c->error);
				return false;
			}
		}
		array_walk ($columns_to_select, array ($this, 'scrub_sql'));
		array_walk ($columns_to_select, array ($this, 'escape_sql_attr'));
		$cs = implode (', ', $columns_to_select);
		$wc = array (); /* Array of WHERE-clauses */
		foreach ($where_clauses as $w_clause) {
			array_push ($wc, '`'.$this->c->real_escape_string ($w_clause['column']).'` '.$this->c->real_escape_string ($w_clause['comparison']).' \''.$this->c->real_escape_string ($w_clause['value']).'\'');
		}
		$w = implode (' AND ', $wc);
		$q = "SELECT % FROM `%` WHERE %;";
		$q = sprintf ($q, $cs, $this->c->real_escape_string ($this->d.'.'.$this->convictBigTable), $wc);
		if ($this->c->real_query ($q) != true) {
			throw new Exception ("Error: failed executing query: ".$this->c->error);
			return false;
		}
		$r = $this->c->store_result ();
		while ($row = $r->fetch_assoc ()) {
			array_push ($result, $row['Field']);
		}
		return $result;
	}

	
}

?>
