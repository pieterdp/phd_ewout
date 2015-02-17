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
	for (let attribute of attributes) {
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
	where_i = where_i.getAttribute ('value');
	/* Add new row */
	/* Update where-i */
}
