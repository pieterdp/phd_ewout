<?php
/*
 * Index page
 */
include_once ('lib/html_generator.php');
include_once ('etc/config.php');
include_once ('lib/class_fetch_dataset.php');

$html = include_skin ('minimal');
$m = new fetch_dataset ();

/*
*/
/* Backu-up option */
$c = $m->get_column_names ('Verblijf');
echo $html->create_base_page ('Erfgoedtools', $c);
echo $html->create_base_page ('Erfgoedtools', $c);
exit (0);
?>
