<?php

include_once ('class_fetch_dataset.php');

class application_fetcher extends fetch_dataset {

	/*
	 * Function to return a convict from prisonerBigTable_normalise by his p_id
	 * For use in later matching
	 * @param string $p_id
	 * @return assoc array $result (ID, p_ID, Inschrijvingsdatum, Geboorteplaats, Leeftijd, Naam, Voornaam)
	 */
	public function get_convict_from_prisonerBT_normalised_by_ID ($p_id) {
		$q = "SELECT ID, p_ID, Inschrijvingsdatum, Geboorteplaats, Leeftijd, Naam, Voornaam FROM prisonerBigTable_normalised
		WHERE p_ID = ?";
		if (!$stmt = $this->c->prepare ($q)) {
			throw new Exception ("Error: failed to prepare query $q: ".$this->c->error);
			return false;
		}
		$stmt->bind_param ('s', $p_id);
		if (!$stmt->execute ()) {
			throw new Exception ("Error: failed to execute query $q: ".$stmt->error);
			return false;
		}
		$stmt->bind_result ($id, $p_id, $inschrijvingsdatum, $geboorteplaats, $leeftijd, $naam, $voornaam);
		$stmt->fetch (); /* Only 1 result */
		$convict = array (
			'ID' => $id,
			'p_ID' => $p_id,
			'Inschrijvingsdatum' => $inschrijvingsdatum,
			'Geboorteplaats' => $geboorteplaats,
			'Leeftijd' => $leeftijd,
			'Naam' => $naam,
			'Voornaam' => $voornaam
		);
		$stmt->close ();
		$stmt = null;
		return $convict;
	}

	/*
	 * Function to match a prisoner (identified by p_ID) from prisonerBT_normalised to RAB_geboortes_normalised
	 * using the following (pseudo-)algorithm:
	 * 	match on Geboorteplaats (using LIKE)
	 * 	match on date_range (BETWEEN AND) like this:
	 * 			take Inschrijvingsdatum - Leeftijd - 5 year as lower boundary
	 * 			and  Inschrijvingsdatum - Leeftijd + 5 year as upper boundary
	 * if none found, ignore the date bit
	 * return results
	 * @param string $p_id
	 * @return array $results[i] = id
	 */
	public function match_prisoner_prisonerBT_normalised_to_RAB_normalised ($p_id) {
		$q = "SELECT g.UUID FROM RAB_geboortes_normalised g, prisonerBigTable_normalised p WHERE
		p.p_ID = ? AND
		g.Geboorteplaats LIKE CONCAT('%', p.Geboorteplaats, '%') AND
		g.Geboortedatum BETWEEN DATE_SUB(p.Inschrijvingsdatum, INTERVAL CAST(5 + p.Leeftijd AS SIGNED) YEAR) AND
		DATE_SUB(p.Inschrijvingsdatum, INTERVAL CAST(p.Leeftijd - 5 AS SIGNED) YEAR);";
		$results = array ();
		if (!$stmt = $this->c->prepare ($q)) {
			throw new Exception ("Error: failed to prepare query $q: ".$this->c->error);
			return false;
		}
		$stmt->bind_param ('s', $p_id);
		if (!$stmt->execute ()) {
			throw new Exception ("Error: failed to execute query $q: ".$stmt->error);
			return false;
		}
		$stmt->bind_result ($uuid);
		$i = 1; // <= CHANGE THIS BIT IF YOU WANT TO USE STAGE 3.5
		while ($stmt->fetch ()) {
			array_push ($results, $uuid);
			$i++;
		}
		$stmt->close ();
		$stmt = null;
		/* If we get no results, recreate the query without the age/gb-plaats parameters */
		/* USEFUL? TBD */
		if ($i == 0) {
			$q = "SELECT g.UUID FROM RAB_geboortes_normalised g, prisonerBigTable_normalised p WHERE
			p.p_ID = ? AND
			g.Geboorteplaats LIKE CONCAT('%', p.Geboorteplaats, '%');";
			if (!$stmt = $this->c->prepare ($q)) {
				throw new Exception ("Error: failed to prepare query $q: ".$this->c->error);
				return false;
			}
			$stmt->bind_param ('s', $p_id);
			if (!$stmt->execute ()) {
				throw new Exception ("Error: failed to execute query $q: ".$stmt->error);
				return false;
			}
			$stmt->bind_result ($uuid);
			while ($stmt->fetch ()) {
				array_push ($results, $uuid);
			}
			$stmt->close ();
			$stmt = null;
		}
		return $results;
	}

	/*
	 * Function to get a person from RAB_geboortes_normalised by his ID
	 * @param string $uuid
	 * @return assoc array (uuid =>, geboorteplaats =>, geboortedatum =>, datum_onvolledig =>, voornaam =>, naam =>, vader_beroep =>)
	 */
	public function get_person_from_RAB_geboortes_normalised_by_ID ($uuid) {
		$q = "SELECT g.UUID, g.Geboorteplaats, g.Geboortedatum, g.Datum_onvolledig, g.Voornaam, g.Naam, g.Vader_beroep FROM RAB_geboortes_normalised g WHERE
		g.UUID = ?";
		$results;
		if (!$stmt = $this->c->prepare ($q)) {
			throw new Exception ("Error: failed to prepare query $q: ".$this->c->error);
			return false;
		}
		$stmt->bind_param ('s', $uuid);
		if (!$stmt->execute ()) {
			throw new Exception ("Error: failed to execute query $q: ".$stmt->error);
			return false;
		}
		$stmt->bind_result ($uuid, $geboorteplaats, $geboortedatum, $datum_onvolledig, $voornaam, $naam, $vader_beroep);
		$stmt->fetch (); /* Only one result */
		array_push ($results, array (
							'uuid' => $uuid,
							'geboorteplaats' => $geboorteplaats,
							'geboortedatum' => $geboortedatum,
							'datum_onvolledig' => $datum_onvolledig,
							'voornaam' => $voornaam,
							'naam' => $naam,
							'vader_beroep' => $vader_beroep
						));
		$stmt->close ();
		$stmt = null;
		return $results;
	}














/* OLD CRUFT */

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
