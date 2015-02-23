<?php

class html_generator {

	protected $tmpl; /* HTML template - <name>.tmpl - should contain [TITLE] & [CONTENT] at minimum, may be hooked */
	protected $loc; /* Location of the template */
	protected $attribute_wrapper; /* Wrapper for attributes */

	function __construct ($template = null) {
		if ($template === null) {
			$template = 'minimal';
		}
		$this->loc = 'lib/html/'.$template.'/';
		if (!file_exists ($this->loc.$template.'.tmpl')) {
			die ("Error: template '$template.tmpl' does not exist in html/-subdirectory.");
		}
		$this->tmpl = file_get_contents ($this->loc.$template.'.tmpl');
		$this->attribute_wrapper = '%s="%s"';
	}

	/*
	 * Function to load a template
	 * @param string $template_name
	 * @param string $template_loc
	 * @return string $template
	 */
	protected function load_template ($template, $lc = null) {
		if ($lc == null) {
			$lc = $this->loc;
		}
		if (!file_exists ($lc.$template.'.tmpl')) {
			die ("Error: template '$template.tmpl' does not exist in html/-subdirectory.");
		}
		return file_get_contents ($lc.'/'.$template.'.tmpl');
	}
	
	/*
	 * Create a base page - i.e. replace [TITLE] & [CONTENT]
	 * @param string $title
	 * @param string $content
	 * @return string $page
	 */
	public function create_base_page ($title, $content) {
		$page = str_replace (array ('[TITLE]', '[CONTENT]'), array ($title, $content), $this->tmpl);
		return $page;
	}
	
	/*
	 * Function to make attributes ready for inclusion in HTML-string
	 * @param array $attributes[i] = array (key = foo, value = bar)
	 * @return array $parsed
	 */
	protected function parse_attributes ($attributes) {
		array_walk ($attributes, function (&$value, &$key) {
			$value = sprintf ($this->attribute_wrapper, htmlentities ($value['key']), htmlentities ($value['value']));
		});
		return $attributes;
	}

/* TODO: replace below with XML-functions (e.g. parent, child) */
	/*
	 * Create a base form
	 * @param array $form_elements[i] = $element (in HTML)
	 * @param string $action, $method, $name attributes
	 * @param optional array $attributes[i] = array (key = foo, value = bar) any additional attributes
	 * @return string $form
	 */
	public function form_template ($form_elements, $action, $method, $name, $attributes = array ()) {
		$form_wrapper = '<form action="%s" method="%s" name="%s" %s>
			%s
		</form>';
		if (count ($form_elements) == 0) {
			/* Error out */
			throw new Exception ("Error: no form child elements specified!");
			return false;
		}
		if ($action == '' || $action == null) {
			throw new Exception ("Error: action is null or empty!");
			return false;
		}
		if ($method == '' || $method == null) {
			throw new Exception ("Error: method is null or empty!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create form */
		$form = sprintf ($form_wrapper,
			htmlentities ($action),
			htmlentities ($method),
			htmlentities ($name),
			implode (' ', $attributes),
			implode ("\r", $form_elements)
		);
		return $form;
	}

	/*
	 * Create submit/reset buttons
	 * @param array $attributes
	 * @return array $buttons[submit, reset]
	 */
	protected function create_submit_reset_buttons ($attributes) {
		$buttons = array ();
		$buttons['submit'] = $this->button_template ('submit', 'Submit', $attributes);
		$buttons['reset'] = $this->button_template ('reset', 'Reset', $attributes);
		return $buttons;
	}

	/*
	 * Create a button
	 * @param string $type
	 * @param string $button_text
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @return string $button
	 */
	public function button_template ($type, $button_text, $attributes = array ()) {
		$button_wrapper = '<button type="%s" %s>%s</button>';
		if ($type == '' || $type == null) {
			throw new Exception ("Error: button_type is null or empty!");
			return false;
		}
		if ($button_text == '' || $button_text == null) {
			throw new Exception ("Error: button_text is null or empty!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create button */
		$button = sprintf ($button_wrapper,
			htmlentities ($type),
			implode (' ', $attributes),
			htmlentities ($button_text)
		);
		return $button;
	}

	/*
	 * Create a textarea
	 * @param string $name
	 * @param int $cols
	 * @param int $rows
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @param optional string $value
	 * @return string $textarea
	 */
	public function textarea_template ($name, $cols, $rows, $attributes = array (), $value = null) {
		$textarea_wrapper = '<textarea rows="%s" cols="%s" name="%s" %s>
		%s
		</textarea>';
		if ($rows == '' || $rows == null || !is_numeric ($rows)) {
			throw new Exception ("Error: rows is empty, null or not a number!");
			return false;
		}
		if ($cols == '' || $cols == null || !is_numeric ($cols)) {
			throw new Exception ("Error: cols is empty, null or not a number!");
			return false;
		}
		if ($name == '' || $name == null) {
			throw new Exception ("Error: name is empty or null!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create textarea */
		$textarea = sprintf ($textarea_wrapper,
			htmlentities ($rows),
			htmlentities ($cols),
			htmlentities ($name),
			implode (' ', $attributes),
			htmlentities ($value)
		);
		return $textarea;
	}

	/*
	 * Create a select-list
	 * @param string $name
	 * @param array $options[i] = array (value = foo, display = bar)
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @param optional array $option_attributes[i] = array (key = foo, value = bar)
	 * @return string $select
	 */
	public function select_template ($name, $options, $attributes = array (), $option_attributes = array (), $label = null) {
		$select_wrapper = '%s<select name="%s" %s>
		%s
		</select>';
		$label_wrapper = '<label for="%s">%s</label>';
		if ($name == '' || $name == null) {
			throw new Exception ("Error: name is empty or null!");
			return false;
		}
		if ($options == '' || $options == null || !is_array ($options)) {
			throw new Exception ("Error: options is empty, null or not an array!");
			return false;
		}
		if ($label != null && ($attributes['id'] == '' || !isset ($attributes['id'])) {
			$attributes['id'] = $name.'_'.time ();
		}
		$attributes = $this->parse_attributes ($attributes);
		$options_array = array ();
		foreach ($options as $option) {
			array_push ($options_array, $this->option_template ($option['value'], $option['display'], $option_attributes));
		}
		$h_label = '';
		if ($label != null) {
			$h_label = sprintf ($label_wrapper, $attributes['id'], htmlentities ($label));
		}
		/* Create select */
		$select = sprintf ($select_wrapper,
			$h_label,
			htmlentities ($name),
			implode (' ', $attributes),
			implode ("\n", $options_array)
		);
		return $select;
	}

	/*
	 * Create an option in a select list
	 * @param string $value
	 * @param string $display
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @return string $option
	 */
	public function option_template ($value, $display, $attributes = array ()) {
		$option_wrapper = '<option value="%s" %s>%s</option>';
		if ($value == '' || $value == null) {
			throw new Exception ("Error: value is empty or null!");
			return false;
		}
		if ($display == '' || $display == null) {
			throw new Exception ("Error: display is empty or null!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create option */
		$option = sprintf ($option_wrapper,
			htmlentities ($value),
			implode (' ', $attributes),
			htmlentities ($display)
		);
		return $option;
	}

	/* TODO: support hidden labels */
	/*
	 * Create a general input type
	 * @param string $name
	 * @param string $type
	 * @param string $id
	 * @param string $label (text, not HTML label)
	 * @param optional array $attributes = array (key = foo, value = bar)
	 * @param bool $use_label (default: true) - use a label. Setting this to false allows $label to be null and the label will not be created
	 * @return string $input
	 */
	public function input_template ($name, $type, $id, $label, $attributes = array (), $USE_LABEL = true) {
		$input_wrapper = '<label for="%s">%s</label>&nbsp;<input type="%s" name="%s" id="%s" %s />';
		$input_wrapper_no_label = '<input type="%s" name="%s" id="%s" %s />';
		if ($name == '' || $name == null) {
			throw new Exception ("Error: name is empty or null!");
			return false;
		}
		if ($type == '' || $type == null) {
			throw new Exception ("Error: type is empty or null!");
			return false;
		}
		if ($id == '' || $id == null) {
			throw new Exception ("Error: id is empty or null!");
			return false;
		}
		if (($label == '' || $label == null) && $USE_LABEL == true) {
			throw new Exception ("Error: label is empty or null!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create input element */
		if ($USE_LABEL == true) {
			$input = sprintf ($input_wrapper,
				htmlentities ($id),
				htmlentities ($label),
				htmlentities ($type),
				htmlentities ($name),
				htmlentities ($id),
				implode (' ', $attributes)
			);
		} else {
			$input = sprintf ($input_wrapper_no_label,
				htmlentities ($type),
				htmlentities ($name),
				htmlentities ($id),
				implode (' ', $attributes)
			);
		}
		return $input;
	}

	/*
	 * Create a table
	 * @param array $column_names[i] = value size of this array determines amount of columns
	 * @param array $content[i] = row[i] = cell_content size of this array determines amount of rows
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @param optional array $row_attributes[i] = array (key = foo, value = bar) (attributes for the row)
	 * @param optional array $cell_attributes[i] = array (key = foo, value = bar) (attributes for the cell)
	 * @param optional array $header_attributes[i] = array (key = foo, value = bar) (attributes for the header cells)
	 * @return string $table
	 */
	public function table_template ($column_names, $content, $attributes = array (), $row_attributes = array (), $cell_attributes = array (), $header_attributes = array ()) {
		$table_wrapper = '<table %s>
		%s
		</table>';
		if ($column_names == '' || $column_names == null || !is_array ($column_names)) {
			throw new Exception ("Error: column_names is empty, null or not an array!");
			return false;
		}
		if ($content == '' || $content == null || !is_array ($content)) {
			throw new Exception ("Error: content is empty, null or not an array!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create rows */
		$rows = array ();
		foreach ($content as $row) {
			/* Create HTML rows */
			array_push ($rows, $this->row_template ($row, $row_attributes, $cell_attributes));
		}
		/* Create table */
		$table = sprintf ($table_wrapper,
			implode (' ', $attributes),
			$this->table_header_template ($column_names, $header_attributes),
			implode ("\n", $rows)
		);
		return $table;
	}

	/*
	 * Create a header
	 * @param array $header[i] = header_content
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @return string $header
	 */
	public function table_header_template ($header, $attributes = array ()) {
		$head_wrapper = '<th %s>
		%s
		</th>';
		$row_wrapper = '<tr %s>
		%s
		</tr>';
		if ($header == '' || $header == null || !is_array ($header)) {
			throw new Exception ("Error: header is empty, null or not an array!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create headers */
		$h_array = array ();
		foreach ($header as $cell) {
			array_push ($h_array, sprintf ($head_wrapper,
				implode (' ', $attributes),
				$cell
			));
		}
		/* Create the header */
		$tr = sprintf ($row_wrapper,
			null,
			implode ("\n", $h_array)
		);
		return $tr;
	}

	/*
	 * Create a row
	 * @param array $row[i] = cell_content
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @param optional array $cell_attributes[i] = array (key = foo, value = bar) (attributes for the cell)
	 * @return string $row
	 */
	public function row_template ($row, $attributes = array (), $cell_attributes = array ()) {
		$row_wrapper = '<tr %s>
		%s
		</tr>';
		if ($row == '' || $row == null || !is_array ($row)) {
			throw new Exception ("Error: row is empty, null or not an array!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Convert all cells to a string */
		$cell_array = array ();
		foreach ($row as $cell) {
			array_push ($cell_array, $this->cell_template ($cell, $cell_attributes));
		}
		/* Create the row */
		$tr = sprintf ($row_wrapper,
			implode (' ', $attributes),
			implode ("\n", $cell_array)
		);
		return $tr;
	}

	/*
	 * Create a cell
	 * @param string $cell content
	 * @param optional array $attributes[i] = array (key = foo, value = bar)
	 * @return string $cell
	 */
	public function cell_template ($cell, $attributes = array ()) {
		$cell_wrapper = '<td %s>
		%s
		</td>';
		if ($cell == '' || $cell == null) {
			throw new Exception ("Error: cell content is empty or null!");
			return false;
		}
		$attributes = $this->parse_attributes ($attributes);
		/* Create cell */
		$td = sprintf ($cell_wrapper,
			implode (' ', $attributes),
			htmlentities ($cell)
		);
		return $td;
	}
}

?>
