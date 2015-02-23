<?php

include_once ('lib/html_generator.php');
include_once ('lib/class_visual_query_builder.php');
include_once ('etc/config.php');
include_once ('lib/class_login.php');
include_once ('lib/class_fetch_dataset.php');

$t = 'minimal';
$html = include_skin ($t);

/*
 * Log-in business
 */
$l = new login ();
$l->l_session_start ();
if ($l->check_login () != true) {
	$referrer = 'application.php';
	if ($_SERVER['HTTPS'] != '' && isset ($_SERVER['HTTPS'])) {
		$loc = 'https://'.$_SERVER['SERVER_NAME'].'/doctoraat_ewout/login.php?return-to=doctoraat_ewout/'.$referrer;
	} else {
		$loc = 'http://'.$_SERVER['SERVER_NAME'].'/doctoraat_ewout/login.php?return-to=doctoraat_ewout/'.$referrer;
	}
	header ("Location: $loc");
	exit (0);
}

if (isset ($_GET['stage'])) {
	$stage = $_GET['stage'];
} else {
	/* Create general landing page */
	$c = '<h1>Convict-matcher</h1>
	<p>
	Deze applicatie helpt om gevangenen (tabel `prisonerBigTable_normalised`) te koppelen aan de geboorteaktes uit het RAB (tabel `RAB_geboortes_normalised`).
	</p>
	<p>
	<ol>
	<li><a href="application.php?stage=1" name="stage_1">Stage 1</a>: selecteer lijst met gevangenen en begin met koppelen.</li>
	<li><a href="application.php?stage=7" name="stage_7">Stage 7</a>: toon lijst met gekoppelde gevangenen.</li>
	</ol>
	</p>';
	echo $html->create_base_page ('Convict-matcher', $c);
	exit (0);
}
/*
 * Stages:
 * 1 => select the convicts from one of the predefined queries
 * 2 => show the user the result set & select the first convict to work on
 * 3 => match the convict to the list of births & select possible matches
 * 3.5 => if no matches were found, broaden criteria
 * 4 => show possible matches & allow the user to select the "match"
 * 5 => update linking table with the match, indicate in the convict table set that this user was matched
 * 6 => GOTO 2 IF still convicts in the list, else GOTO 1
 * 7 => show matching lists
 */
switch ($stage) {
	case '1':
		$v = new visual_query_builder ($t);
		$f = new fetch_dataset ();
		echo $html->create_base_page ('Convict-matcher', $v->display_convict_query_form ($f->select_gb_from_prisonerBT_normalised ()));
		exit (0);
	break;
	case '2':
	break;
	case '3':
	break;
	case '4':
	break;
	case '5':
	break;
	case '6':
	break;
	case '7':
	break;
}


?>
