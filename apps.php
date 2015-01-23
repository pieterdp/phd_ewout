<?php
if (isset ($_GET['name']) && $_GET['name'] == 'vioe') {
	header ("location: http://erfgoeddb.helptux.be/vioe.php");
	exit (0);
}
if (isset ($_GET['name']) && $_GET['name'] == 'gemeenteswvl') {
	header ("location: http://erfgoeddb.helptux.be/gemeenteswvl.php");
	exit (0);
}
/*
 * Index page
 */
include_once ('lib/html_generator.php');
include_once ('etc/config.php');

$html = include_skin ('minimal');

/*
*/
/* Back-up option */
$c = '<h1>Tools</h1>
<p>Deze "tools" zijn ontworpen om het werk aan de Beeldbank West-Vlaanderen eenvoudiger te maken.</p>
<ul>
<li><a href="unified.xml">XML-lijst met gegeolokeerde monumenten uit West-Vlaanderen</a>('.(filesize ('unified.xml') / 1024 / 1024).' MB)</li>
<li><a href="apps.php?name=vioe">Wrapper rond zoekformulier VIOE (bevat API)</a></li>
<li><a href="apps.php?name=gemeenteswvl">Opzoeken van West-Vlaamse gemeentes, deelgemeentes en straten</a></li>
<li><a href="lookup/lookup.php?action=termen">Matchen van termenlijsten aan de AAT</a> (vereist login)</li>
</ul>';
echo $html->create_base_page ('Erfgoedtools', $c);
exit (0);
?>