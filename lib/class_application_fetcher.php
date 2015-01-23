<?php

include_once ('class_fetch_dataset.php');

class application_fetcher extends fetch_dataset {

	/*
	 * Requirements:
	 * Columns to return: Id_gedetineerde, Id_verblijf, Voornaam, Naam, Inschrijvingsdatum_d, Inschrijvingsdatum_m, Inschrijvingsdatum_j, Leeftijd, Geboortejaar, Geboorteplaats, Woonplaats
	 * Select from view using select_from_convictBigTable ($columns_to_select, $where_clauses)
	 * @param string $name - name of the convict
	 * @return array $result[i] = row
	 */
	public function get_convict_by_name ($name) {
		/*$name = $this->c->real_escape_string ($name);*/ /* Escaping is done in select_from */
		$columns_to_select = array ('Id_gedetineerde', 'Id_verblijf', 'Voornaam', 'Naam', 'Inschrijvingsdatum_d', 'Inschrijvingsdatum_m', 'Inschrijvingsdatum_j', 'Leeftijd', 'Geboortejaar', 'Geboorteplaats', 'Woonplaats');
		$result = array ();
		$result = $this->select_from_convictBigTable ($columns_to_select, array (array ('column' => 'Naam', 'comparison' => 'LIKE', 'value' => '%'.$name.'%')));
		return result;
		//select_from_convictBigTable ($columns_to_select, $where_clauses)
	}
	/* use http://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html to compare dates with eachother */

	/*
	 * convict_shortened_name: core of the name (no van/de/vande etc.) to make matching possible */
	 /* add possibility to modify core name yourself */
	public function compare_convicts ($convict_uuid, $convict_shortened_name) {
		$compare_query = "SELECT * FROM RAB_geboortes_normalised g, prisonerBigTable_normalised p WHERE
		g.Naam LIKE '%?%' AND
		p.p_ID = '?' AND
		g.Geboorteplaats LIKE p.Geboorteplaats AND
		g.Geboortedatum BETWEEN DATE_SUB(p.Inschrijvingsdatum, INTERVAL CAST(5 + p.Leeftijd AS SIGNED) YEAR) AND
		DATE_SUB(p.Inschrijvingsdatum, INTERVAL CAST(p.Leeftijd - 5 AS SIGNED) YEAR);";
	}
}

?>
