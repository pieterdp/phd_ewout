<?php

include_once ('class_html.php');

class visual_query_builder extends class_html {

	protected $operators = array ();

	function __construct ($template = null) {
		parent::__construct ($template);
		$this->operators = array ('=', '<>', '<', '>', '<=', '>=', 'BETWEEN', 'LIKE', 'IN');
	}

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
			
	}

	protected function mk_list_limited_where_operators () {
		/*
	 * Create a select-list
	 * @param string $name
	 * @param array $options[i] = array (value = foo, display = bar)
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @param optional array $option_attributes[i] = array (key = foo, value = bar)
	 * @return string $select
	 */
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
