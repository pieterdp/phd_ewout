<?php

include_once ('mysql_connect.php');

class visual_query_parser extends db_connect {


	/*
	 * Function to fetch the where clause of a visual query
	 * (TODO? Support $_REQUEST so both GET & POST work)
	 * @return array $where_clauses[i] = array (left =>, operator =>, right =>) (html_decoded)
	 */
	public function fetch_where_clause () {
		/* left_where_clause_input-0
		 * where_operator-0
		 * right_where_clause_input-0
		 */
		$where_clauses = array ();
		$i = 0;
		while (isset ($_POST['left_where_clause_input-'.$i])) {
			$where_clause = array (
				'left' => $this->c->real_escape_string (html_entity_decode ($_POST['left_where_clause_input-'.$i])),
				'operator' => html_entity_decode ($_POST['where_operator-'.$i]),
				'right' => $this->c->real_escape_string (html_entity_decode ($_POST['right_where_clause_input-'.$i]))
			);
			array_push ($where_clauses, $where_clause);
			$i++;
		}
		return $where_clauses;
	}
}

?>
