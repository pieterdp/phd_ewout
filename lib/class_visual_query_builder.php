<?php

include_once ('class_html.php');

class visual_query_builder extends html_generator {

	protected $operators = array ();

	function __construct ($template = null) {
		parent::__construct ($template);
		$this->operators = array ('=', '<>', '<', '>', '<=', '>=', 'BETWEEN', 'LIKE', 'IN');
	}

	/*
	 * Display a form to create a query for convicts from a certain community ('Geboorteplaats') and date_cohort (oldest_date, youngest_date)
	 * @param array $list_of_gb
	 * @return string $convict_query_form
	 */
	public function display_convict_query_form ($list_of_gb) {
		$template = '<div class="query_form" id="query_form">
		<h1>Dataset selecteren</h1>
		%s
		</div>';
		$date_template = '<span class="pseudo_label">%s</span>%s';
		$input_wrapper = '<div class="query_form_input">
			%s
		</div>';
		/* The list of GB-names is a select-list */
		$options = array ();
		foreach ($list_of_gb as $gb) {
			array_push ($options, array ('value' => $gb, 'display' => $gb));
		}
		$gb_places = $this->select_template ('geboorteplaats', $options, array (array ('key' => 'id', 'value' => 'geboorteplaatsen-select'), array ('key' => 'class', 'value' => 'query_form')), array (array ('key' => 'class', 'value' => 'query_form')), 'Geboorteplaats');
		$geboorteplaats = sprintf ($input_wrapper, $gb_places);
		/* Create other input forms */
		$date_input = array (	$this->input_template ('datum_oud_d', 'text', 'datum_oud_d', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 2)), false),
								$this->input_template ('datum_oud_m', 'text', 'datum_oud_m', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 2)), false),
								$this->input_template ('datum_oud_y', 'text', 'datum_oud_y', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 4)), false));
		$datum_oud = sprintf ($date_template,
								'Datum_oud (dd/mm/yyyy)',
								implode ('&nbsp;&mdash;&nbsp;', $date_input));
		$date_input = array (	$this->input_template ('datum_jong_d', 'text', 'datum_jong_d', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 2)), false),
								$this->input_template ('datum_jong_m', 'text', 'datum_jong_m', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 2)), false),
								$this->input_template ('datum_jong_y', 'text', 'datum_jong_y', null, array (array ('key' => 'class', 'value' => 'datum'), array ('key' => 'size', 'value' => 4)), false));
		$datum_jong = sprintf ($date_template,
								'Datum_jong (dd/mm/yyyy)',
								implode ('&nbsp;&mdash;&nbsp;', $date_input));
		$hidden_submit = $this->input_template ('submit', 'hidden', 'submit', null, array (), false);
		$submit = $this->create_submit_reset_buttons (array (array ('key' => 'class', 'value' => 'query_form')));
		/* Create form */
		//form_template ($form_elements, $action, $method, $name, $attributes = array ())
		$form = $this->form_template (	array ($geboorteplaats, $datum_oud, $datum_jong, $hidden_submit, $submit),
										'',
										'post',
										array (array ('key' => 'class', 'value' => 'query_form')));
		return sprintf ($template, $form);
	}

	/*
	 * Display a query-builder row of the form "foo" "operator" "bar" for inclusion in a WHERE-clause
	 * @return string $query_builder_row
	 */
	public function display_where_clause () {
		$template = '<div id="where" class="where">
			<div id="where_clause-0" class="where_clause">
				<div id="left_where_clause-0" class="where_clause_left">
				%s
				</div>
				<div id="where_clause_operator-0" class="where_clause_operator">
				%s
				</div>
				<div id="right_where_clause-0" class="where_clause_right">
				%s
				</div>
			</div>
			%s
		</div>';
		$where_display = sprintf ($template,
			$this->input_template ('left_where_clause_input-0', 'text', 'left_where_clause_input-0', null, array (array ('key' => 'class', 'value' => 'where_clause_input')), false),
			$this->mk_list_limited_where_operators (),
			$this->input_template ('right_where_clause_input-0', 'text', 'right_where_clause_input-0', null, array (array ('key' => 'class', 'value' => 'where_clause_input')), false),
			$this->input_template ('where-i', 'hidden', 'where-i', null, array (array ('key' => 'value', 'value' => '0')), false)
		);
		return $where_display;
	}

	/* MUST BE DECODED WHEN USED */
	/*
	 * Create a list with SQL-operators this system supports (<select><option></option></select>)
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
