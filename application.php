<?php

include_once ('lib/html_generator.php');
include_once ('lib/class_visual_query_builder.php');
include_once ('etc/config.php');
include_once ('lib/class_login.php');
include_once ('lib/class_fetch_dataset.php');
include_once ('lib/class_date_parser.php');
include_once ('lib/class_application_fetcher.php');

$t = 'minimal';
$html = include_skin ($t);
$dp = new date_parser ();

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
		/* Fetch result */
		$f = new fetch_dataset ();
		if (!isset ($_POST['submit'])) {
			echo $html->create_base_page ('Convict matcher', '<div class="error"><h1>Error</h1><p>Fout: formulier niet ingevuld. Ga terug naar <a href="application.php?stage=1">de startpagina</a>.</p></div>');
			exit (1);
		}
		$geboorteplaats = $_POST['geboorteplaats'];
		$datum_oud = $dp->parseInputDate (array ('y' => $_POST['datum_oud_y'], 'm' => $_POST['datum_oud_m'], 'd' => $_POST['datum_oud_d']));
		$datum_jong = $dp->parseInputDate (array ('y' => $_POST['datum_jong_y'], 'm' => $_POST['datum_jong_m'], 'd' => $_POST['datum_jong_d']));
		$convicts = $f->get_convicts_from_prisonerBT_normalised ($geboorteplaats, $datum_oud, $datum_jong);
		/* Show result */
		if (count ($convicts) == 0) {
			$table = '<div class="no-results"><h1>Geen resultaten</h1><p>Er werden geen resultaten gevonden. Probeer opnieuw met andere parameters.</p></div>';
		} else {
			$rows = array ();
			$column_names = array ('ID_gedetineerde', 'Naam', 'Voornaam', 'Inschrijfdatum', 'Leeftijd', 'Geboorteplaats', 'Match');
			foreach ($convicts as $convict) {
				$row = array (	htmlentities ($convict['p_id']),
								htmlentities ($convict['naam']),
								htmlentities ($convict['voornaam']),
								htmlentities ($convict['inschrijvingsdatum']->format ('Y-m-d')),
								htmlentities ($convict['leeftijd']),
								htmlentities ($convict['geboorteplaats']),
								'<a href="application.php?stage=3&amp;id='.$convict['p_id'].'">match</a>'
								);
				array_push ($rows, $row);
			}
			$table = $html->table_template ($column_names, $rows, array (array ('key' => 'class', 'value' => 'convict_table_results')), array (array ('key' => 'class', 'value' => 'convict_table_results')), array (array ('key' => 'class', 'value' => 'convict_table_results')), array (array ('key' => 'class', 'value' => 'convict_table_results')));
		}
		echo $html->create_base_page ('Convict-matcher (stage 2)', $table);
		exit (0);
	break;
	case '3':
		$ap = new application_fetcher ();
		/* Get prisoner by ID */
		if (!isset ($_GET['id'])) {
			echo $html->create_base_page ('Convict matcher', '<div class="error"><h1>Error</h1><p>Fout: geen ID opgegeven. Ga terug naar <a href="application.php?stage=1">de startpagina</a>.</p></div>');
			exit (1);
		}
		$p_id = $_GET['id'];
		/* Match with birth places (first with dates_inclusive, next without (3.5)) */
		$resulting_ids = $ap->match_prisoner_prisonerBT_normalised_to_RAB_normalised ($p_id);
		/* Return results */
		$rows = array ();
		foreach ($resulting_ids as $id) {
			$full = $ap->get_person_from_RAB_geboortes_normalised_by_ID ($id);
			$row = array (	htmlentities ($full['uuid']),
							htmlentities ($full['voornaam']),
							htmlentities ($full['naam']),
							htmlentities ($full['geboortedatum']),
							htmlentities ($full['geboorteplaats']),
							htmlentities ($full['datum_onvolledig']),
							htmlentities ($full['vader_beroep']),
							$html->input_template ('match', 'radio', 'match-'.$full['uuid'], null, array (array ('key' => 'class', 'value' => 'match_radio'), array ('key' => 'value', 'value' => $full['uuid'])), false)
							);
			array_push ($rows, $row);
		}
		/* Show results */
		if (count ($rows) == 0) {
			$form_content = '<div class="no-results"><p>Er werden geen resultaten gevonden.</p><input type="hidden" name="match" value="NONE_FOUND" /></div>';
		} else {
			$column_names = array ('UUID', 'Voornaam', 'Naam', 'Geboortedatum', 'Geboorteplaats', 'Datum (onvolledig)', 'Beroep vader');
			$form_content = $html->table_template ($column_names, $rows, array (array ('key' => 'class', 'value' => 'person_table_results')), array (array ('key' => 'class', 'value' => 'person_table_results')), array (array ('key' => 'class', 'value' => 'person_table_results')), array (array ('key' => 'class', 'value' => 'person_table_results')));
		}
		$template = '<div class="match_form" id="match_form">
		<h1>Personen matchen</h1>
		%s
		</div>';
		$hidden_submit = $this->input_template ('submit', 'hidden', 'submit', null, array (), false);
		$submit = $this->create_submit_reset_buttons (array (array ('key' => 'class', 'value' => 'match_form')));
		$input_list = array ($form_content);
		$input_list = array_merge ($input_list, $submit);
		$form = $html->form_template (	$input_list,
										'application.php?stage=5',
										'post',
										'match_form',
										array (array ('key' => 'class', 'value' => 'match_form')));
		$content = sprintf ($template, $form);
		echo $html->create_base_page ('Convict-matcher (stage 3)', $content);
		exit (0);
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
