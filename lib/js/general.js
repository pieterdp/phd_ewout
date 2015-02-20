/* General application JS */

/*
 * Function to add a child element to a container element
 * @param string id - id of the container element
 * @param domElement element to add
 * @return true/false
 */
function add_child (id, child) {
	var parent = document.getElementById (id);
	if (parent == null) {
		/* Error */
		window.alert ('Error: no element with id ' + id + ' exists.');
		return false;
	}
	parent.appendChild (child);
	return true;
}

/*
 * Create an element
 * @param string type
 * @param object attributes[i] = attribute.name = name, attribute.value = value (HTML-attributes)
 * @param string content (optional) (plain (HTML-encoded) text)
 * @return domElement element
 */
function create_element (type, attributes, content) {
	var element = document.createElement (type);
	/*createTextNode*/
	for (var i = 0; i < attributes.length; i++) {
		var attribute = attributes[i];
		element.setAttribute (attribute.name, attribute.value);
	}
	if (content) {
		/* Has content */
		var text = document.createTextNode (content);
		element.appendChild (text);
	}
	return element;
}

/* App-specific functions */
/*
 * Create a new WHERE-clause in the visual query builder
 * @return true/false
 */
function add_new_where_clause () {
	/* Get the number of the last existing where-clause (like an array, starts at 0) */
	var where_i = document.getElementById ('where-i');
	if (where_i == null) {
		window.alert ('Error: where-i could not be found.');
		return false;
	}
	new_i = where_i.getAttribute ('value');
	new_i = parseInt (new_i) + 1;
	where_i.setAttribute ('value', new_i);
	var where_clause = create_element ('div', [{name:"id", value:"where_clause-" + new_i}, {name:"class", value:"where_clause"}]);
	where_clause.appendChild (create_left_clause (new_i));
	where_clause.appendChild (create_operator_clause (new_i));
	where_clause.appendChild (create_right_clause (new_i));
	var container_div = document.getElementById ('where');
	container_div.appendChild (where_clause);
	return true;
}

/*
 * Create left clause
 * @param int new_id - the number of the new left_clause (clauses are numbered as where_clause-"number" - we want this number)
 * @return element left_clause
 */
function create_left_clause (new_id) {
	var div_new_id = 'left_where_clause-' + new_id;
	var div = create_element ('div', [{name:"id", value:div_new_id}, {name:"class", value:"where_clause_left"}]);
	var input_new_id = 'left_where_clause_input-' + new_id;
	var input = create_element ('input', [{name:"id", value:input_new_id}, {name:"name", value:input_new_id}, {name:"class", value:"where_clause_input"}, {name:"type", value:"text"}]);
	div.appendChild (input);
	return div;
}

/*
 * Create right clause
 * @param int new_id - the number of the new right_clause (clauses are numbered as where_clause-"number" - we want this number)
 * @return element right_clause
 */
function create_right_clause (new_id) {
	var div_new_id = 'right_where_clause-' + new_id;
	var div = create_element ('div', [{name:"id", value:div_new_id}, {name:"class", value:"where_clause_right"}]);
	var input_new_id = 'right_where_clause_input-' + new_id;
	var input = create_element ('input', [{name:"id", value:input_new_id}, {name:"name", value:input_new_id}, {name:"class", value:"where_clause_input"}, {name:"type", value:"text"}]);
	div.appendChild (input);
	return div;
}

/*
 * Create where operator clause
 * @param int new_id - the number of the new right_clause (clauses are numbered as where_clause-"number" - we want this number)
 * @return element operator_clause
 */
function create_operator_clause (new_id) {
	var div_new_id = 'where_clause_operator-' + new_id;
	var div = create_element ('div', [{name:"id", value:div_new_id}, {name:"class", value:"where_clause_operator"}]);
	var option_values = ['=', '<>', '<', '>', '<=', '>=', 'BETWEEN', 'LIKE', 'IN'];
	var input_new_id = 'where_operator-' + new_id;
	var select = create_element ('select', [{name:"id", value:input_new_id}, {name:"name", value:input_new_id}, {name:"class", value:"where_operators"}]);
	for (var i = 0; i < option_values.length; i++) {
		var option = create_element ('option', [{name:"value", value:option_values[i]}], option_values[i]);
		select.appendChild (option);
	}
	div.appendChild (select);
	return div;
}

/*
 * Function to update an attribute to a new number of a where clause or any of its children
 * @param Element element
 * @param int updated_i (number to add in xfz-i)
 * @param string attr_name
 * @return Element updated_element
 */
function where_update_id (element, updated_i, attr_name) {
	var old_id = element.getAttribute (attr_name);
	var new_id = old_id;
	new_id.replace (/-[0-9]+$/, '-' + updated_i);
	element.setAttribute (attr_name, new_id);
	return element;
}
