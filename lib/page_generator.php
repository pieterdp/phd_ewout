<?php

include_once ('html_generator.php');

class page_generator {

	public $skin;
	public $iconset;
	public $admin;

	function __construct ($skin = null, $iconset = null) {
		$this->skin = include_skin ($skin);
		$this->iconset = load_icons ($iconset);
		$this->admin = new admin_page ();
	}

	/*
	 * Create a login page
	 * @param string $csrf
	 * @param string $referrer
	 * @param string $message
	 * @return string $page
	 */
	public function g_login ($csrf, $referrer = null, $message = null) {
		$login_wrapper = '<div class="login-wrapper">
	%s
</div>';
		$login_form = '<form class="login-form" id="login-form" method="post" action="login.php?return-to=%s">
	%s
	<div class="spacer"></div>
	<div class="login-form username"><img src="'.$this->iconset.'person.gif'.'" class="login-form icon" alt="Gebruiker" /><label for="username">%s</label>&nbsp;<input type="text" id="username" name="username" class="login-form" /></div>
	<div class="spacer"></div>
	<div class="login-form password"><img src="'.$this->iconset.'key.gif'.'" class="login-form icon" alt="Wachtwoord" /><label for="password">%s</label>&nbsp;<input type="password" id="password" name="password" class="login-form" /></div>
	<div class="login-form submit"><input type="hidden" name="submit" value="1" /><input type="hidden" name="csrf" value="'.$csrf.'" /><input type="submit" value="Aanmelden" /></div>
</form>';
		/* $this->lang->string ('username') */
		if ($referrer === null) {
			$referrer = 'index.php';
		}
		$referrer = urlencode ($referrer);
		$m = '<!-- Login form -->';
		if ($message != null) {
			$m = '<div class="login-form message"><img src="'.$this->iconset.'warning.gif" class="login-form icon" alt="Message" /><span class="message">'.htmlentities ($message).'</span></div>';
		}
		$lc = sprintf ($login_wrapper, sprintf ($login_form, $referrer, $m, 'Gebruikersnaam', 'Wachtwoord'));
		return $this->skin->create_base_page ('Aanmelden', $lc); 
	}

	/*
	 * Create a user account settings page
	 * @param string $csrf
	 * @param string $username, $email
	 * @optional param array $account_information [key = value]
	 * @optional param string $message
	 * @return string $page
	 */
	public function g_account ($csrf, $username, $email, $account_information = array (), $message = null) {
		$settings_wrapper = '<div class="settings-wrapper">
	%s
	%s
</div>';
		$form = '<form class="settings-form" id="settings-form" method="post" action="user.php?action=g_account">
	<label for="username" class="settings-form">%s</label><input type="text" id="username" name="username" class="settings-form" value="%s" readonly="readonly" />
	<fieldset class="settings-form" id="identifying-information">
	<legend class="settings-form">%s</legend>
	<label for="email" class="settings-form">%s</label><input type="text" id="email" name="email" class="settings-form" value="%s" />
	</fieldset>
	<fieldset class="settings-form" id="password-change">
	<legend class="settings-form">%s</legend>
	<label for="oldpassword" class="settings-form">%s</label><input type="password" id="oldpassword" name="oldpassword" class="settings-form" />
	<label for="newpassword" class="settings-form">%s</label><input type="password" id="newpassword" name="newpassword" class="settings-form" />
	<label for="newpassword-2" class="settings-form">%s</label><input type="password" id="newpassword-2" name="newpassword-2" class="settings-form" />
	</fieldset>
	<input type="hidden" name="submit" value="1" /><input type="hidden" name="csrf" value="%s" /><input type="submit" value="Update" />
</form>';
		$ac = sprintf ($settings_wrapper, $message, sprintf ($form,
			'Gebruikersnaam', $username,
			'Persoonlijke gegevens',
			'E-mailadres', $email,
			'Wachtwoord',
			'Oud wachtwoord',
			'Nieuw wachtwoord',
			'Nieuw wachtwoord opnieuw invoeren',
			$csrf
		));
		return $this->admin->create_admin_page ('Gebruikersaccountbeheer', $ac);
	}
}

?>