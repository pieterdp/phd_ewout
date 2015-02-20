<?php
/*
 * Index page
 */
include_once ('lib/html_generator.php');
include_once ('etc/config.php');
include_once ('lib/class_fetch_dataset.php');
include_once ('lib/class_visual_query_builder.php');

$html = include_skin ('minimal');

$v = new visual_query_builder ();
$w = $v->display_where_clause ();

echo $w;

exit (0);
?>
