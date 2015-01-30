<?php

include_once ('class_html.php');

class visual_query_builder extends html_generator {

	protected $operators = array ();

	function __construct ($template = null) {
		parent::__construct ($template);
		$this->operators = array ('=', '<>', '<', '>', '<=', '>=', 'BETWEEN', 'LIKE', 'IN');
	}

	/*
	 * Display a query-builder row of the form "foo" "operator" "bar" for inclusion in a WHERE-clause
	 * @return string $query_builder_row
	 */
	public function display_where_clause () {
		$template = '<div id="where_clause-0" class="where_clause">
			<div id="left_where_clause-0" class="where_clause_left">
			%s
			</div>
			<div id="where_clause_operator-0" class="where_clause_operator">
			%s
			</div>
			<div id="right_where_clause0" class="where_clause_right">
			%s
			</div>
		</div>';
		$where_display = sprintf ($template,
			$this->input_template ('left_where_clause_input-0', 'text', 'left_where_clause_input-0', null, array (array ('key' => 'class', 'value' => 'where_clause_input')), false),
			$this->mk_list_limited_where_operators (),
			$this->input_template ('right_where_clause_input-0', 'text', 'right_where_clause_input-0', null, array (array ('key' => 'class', 'value' => 'where_clause_input')), false)
		);
		return $where_display;
	}

	/* MUST BE DECODED WHEN USED */
	/*
	 * Create a list with SQL-operators this systeem supports (<select><option></option></select>)
	 * @return string $select_list
	 */
	protected function mk_list_limited_where_operators () {
		$options_operators = array ();
		foreach ($this->operators as $operator) {
			array_push ($options_operators, array ('value' => $operator, 'display' => $operator));
		}
		$select_list = $this->select_template	(	'where_operator-0',
													$options_operators,
													array (
														array ('key' => 'id', 'value' => 'where_operator-0'),
														array ('key' => 'class', 'value' => 'where_operators')
													)
												);
		return $select_list;
	}

}

?>
