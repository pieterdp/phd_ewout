<?php

class db_connect {
	
	protected $c;
	protected $d; /* Name of the database */

	function __construct () {
		if (file_exists ('etc/config.php')) {
			include ('etc/config.php');
		} else {
			die ("Error: configuration file not found.");
		}
		$this->c = new mysqli ($db['host'], $db['username'], $db['password'], $db['database']);
		$this->d = $db['database'];
	}

	/*
	 * Function to get user information via user_id
	 * @param int $uid
	 * @return array $info
	 */
	public function select_user ($uid) {
		$q = "SELECT u.username, u.id, u.email FROM users u WHERE u.id = ?";
		$st = $this->c->prepare ($q);
		$st->bind_param ('d', $uid);
		$st->execute ();
		$st->bind_result ($username, $id, $email);
		$st->fetch ();
		$info = array ('username' => $username, 'id' => $id, 'email' => $email);
		$st->close ();
		$st = null;
		return $info;
	}
}

?>
