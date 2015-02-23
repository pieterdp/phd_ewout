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
	 * Function to return a list of Geboorteplaatsen from prisonerBigTable_normalised
	 * @return array $geboorteplaatsen
	 */
	public function select_gb_from_prisonerBT_normalised () {
		$result = array ();
		$q = "SELECT DISTINCT `Geboorteplaats` FROM `prisonerBigTable_normalised` WHERE `Geboorteplaats` IS NOT NULL AND `Geboorteplaats` <> 'Onbekend' AND `Geboorteplaats` <> '' AND `matched` = 'NO' ORDER BY `Geboorteplaats`";
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

	/*
	 * Function to return a list of convicts from a certain place within a certain time range
	 * @param string $gb_plaats
	 * @param DateTime $date_oud
	 * @param DateTime $date_jong
	 * @return assoc array $convicts (naam, voornaam, inschrijfdatum (DateTime), leeftijd, geboorteplaats)
	 */
	public function get_convicts_from_prisonerBT_normalised ($gb_plaats, $date_oud, $date_jong) {
		if (!$date_oud instanceof DateTime) {
			throw new Exception ("Error: \$date_oud is not a DateTime object!");
			return false;
		}
		if (!$date_jong instanceof DateTime) {
			throw new Exception ("Error: \$date_jong is not a DateTime object!");
			return false;
		}
		$result = array ();
		//d/m/y
		$q = "SELECT p.p_ID, p.Naam, p.Voornaam, p.Inschrijvingsdatum, p.Leeftijd, p.Geboorteplaats FROM prisonerBigTable_normalised p WHERE
		p.Geboorteplaats LIKE ? AND
		p.Inschrijvingsdatum BETWEEN ? AND ? AND
		p.matched = 'NO'";
		// STR_TO_DATE(CONCAT(?, ' 0:00:00'),'%e/%c/%Y %k:%i:%s')
		if (!$stmt = $this->c->prepare ($q)) {
			throw new Exception ("Error: failed to prepare query $q: ".$this->c->error);
			return false;
		}
		$date_jong = $date_jong->format ('o-m-d H:i:s');
		$date_oud = $date_oud->format ('o-m-d H:i:s');
		$stmt->bind_param ('sss', '%'.$gb_plaats.'%', $date_jong, $date_oud);
		if (!$stmt->execute ()) {
			throw new Exception ("Error: failed to execute query $q: ".$stmt->error);
			return false;
		}
		$stmt->bind_result ($p_id, $naam, $voornaam, $inschrijvingsdatum, $leeftijd, $geboorteplaats);
		while ($stmt->fetch ()) {
			$row = array (
				'p_id' => $p_id,
				'naam' => $naam,
				'voornaam' => $voornaam,
				'inschrijvingsdatum' => DateTime::createFromFormat ('Y-m-d H:i:s', $inschrijvingsdatum),
				'leeftijd' => $leeftijd,
				'geboorteplaats' => $geboorteplaats
			);
			array_push ($result, $row);
		}
		$stmt = null;
		return $result;
	}
	
	
}

?>
