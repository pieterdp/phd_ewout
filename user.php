<?php

/* Page for users (e.g. change profile etc. */
include_once ('lib/class_create_user.php');
include_once ('lib/class_login.php');
include_once ('lib/page_generator.php');
include_once ('lib/mysql_connect.php');

$c = new create_user ();
$l = new login ();
$p = new page_generator ();
$db = new db_connect ();

$l->l_session_start ();

/* Redirect the user to login.php?return-to=user.php when not logged in */
if ($l->check_login () != true) {
	if (isset ($_SERVER['HTTPS'])) {
		$loc = 'https://'.$_SERVER['SERVER_NAME'];
	} else {
		$loc = 'http://'.$_SERVER['SERVER_NAME'];
	}
	header ("location: $loc/login.php?return-to=user.php", 302);
	exit (0);
}

/* Get the user id */
$uid = $l->get_user_id ($_SESSION['login'], 'session_hash');
if ($_SESSION['user'] != hash ('sha512', $uid)) {
	$m = '<span class="site-error error">An error occured (<span class="code">uid</span> doesn\'t match</span>)!</span>';
	echo $p->skin->create_base_page ('Gebruikersrechtenbeheer', $m);
	exit (0);
}
/* Get the CSRF */
$csrf = $l->csrf_string ($_SESSION['login']);
$action = $_GET['action'];

switch ($action) {
	case 'g_account':
		if (isset ($_POST['submit']) && $_POST['submit'] == '1') {
			/* Validate */
			$username = $_POST['username'];
			$email = $_POST['email'];
			$oldpassword = $_POST['oldpassword'];
			$newpassword = $_POST['newpassword']; /* Checking whether this and -2 are the same is javascript land */
			$csrf_f = $_POST['csrf'];
			/* Check whether the old password is correct */
			if ($l->check_password ($uid, $oldpassword) != true) {
				/* Sorry */
				$u_info = $db->select_user ($uid);
				echo $p->g_account ($csrf, $u_info['username'], $u_info['email'], array (), '<div class="login-form message"><img src="'.$p->iconset.'warning.gif" class="login-form icon" alt="Message" /><span class="message">Wachtwoord onjuist.</span></div>');
				exit (0);
			}
			exit (0);
		}
		/* Get user info */
		$u_info = $db->select_user ($uid);
		/* Check whether the returned information is indeed valid for this user */
		if ($_SESSION['user'] != hash ('sha512', $u_info['id'])) {
			$m = '<span class="site-error error">An error occured (<span class="code">uid</span> doesn\'t match</span>)!</span>';
			echo $p->skin->create_base_page ('Gebruikersrechtenbeheer', $m);
			exit (0);
		}
		echo $p->g_account ($csrf, $u_info['username'], $u_info['email']);
		exit (0);
	break;
}

?>