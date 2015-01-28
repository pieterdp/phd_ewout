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
/* TODO: replace below with XML-functions (e.g. parent, child) */
	/*
	 * Create a base form
	 * @param array $form_elements[i] = $element
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
		array_walk ($attributes, function (&$value, &$key) {
			$value = sprintf ($this->attribute_wrapper, htmlentities ($value['key']), htmlentities ($value['value']));
		});
		/* Create form */
		$form = sprintf ($form_wrapper,
			htmlentities ($action),
			htmlentities ($method),
			htmlentities ($name),
			implode (' ', $attributes),
			implode ("\n", $form_elements)
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
		array_walk ($attributes, function (&$value, &$key) {
			$value = sprintf ($this->attribute_wrapper, htmlentities ($value['key']), htmlentities ($value['value']));
		});
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
	public function textarea_template ($name, $cols, $rows, $attributes = array, $value = null) {
	}
}

?>
