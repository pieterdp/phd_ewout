<?php

/*
 * Additional function to parse dates (hide some of the complexity of DateTime)
 * All functions return DateTime (except when indicated otherwise)
 */

class date_parser {

	public $dt; /* DateTime object */
	public $dt_string; /* String */

	function __construct () {
	}

	/*
	 * Convert a MYSQL DATE/TIME-stamp to DateTime
	 * @param string $mysql_string
	 */
	public function fromMYSQL ($mysql_string) {
		$this->dt = DateTime::createFromFormat ('Y-m-d H:i:s', $mysql_string);
		if (!$this->dt instanceof DateTime) {
			throw new Exception ("Error: failed to convert $mysql_string to DateTime!");
			return false;
		}
		return $this->dt;
	}

	/*
	 * Convert a DateTime to a MYSQL DATE/TIME-stamp
	 * @param DateTime $dateTime
	 * @return string $mysql_string
	 */
	public function toMYSQL ($dateTime) {
		if (!$dateTime instanceof DateTime) {
			throw new Exception ("Error: $dateTime is not of type DateTime!");
			return false;
		}
		$this->dt_string = $dateTime->format ('o-m-d H:i:s');
		return $this->dt_string;
	}

	/*
	 * Parse an input date (user-input); all fields except the year are optional
	 * Values are numeric, but need not to be zeropadded (we'll do that when necessary)
	 * Years must be full
	 * @param array $input_date = array ('y' =>, 'm' =>, 'd' =>, 'h' =>, 'i' =>, 's' =>)
	 */
	public function parseInputDate ($input_date) {
		if (!isset ($input_date['y'])) {
			throw new Exception ("Error: \$input_date has no index y (year).");
			return false;
		}
		$parsable_date = '%s-%s-%s %s:%s:%s';
		$date_parts = array ('y', 'm', 'd', 'h', 'i', 's');
		$date_parsed = array ();
		foreach ($date_parts as $date_part) {
			if (!isset ($input_date[$date_part])) {
				/* H:M:S can be 00, but m-d cannot! */
				if ($date_part == 'm' || $date_part == 'd') {
					$date_parsed[$date_part] = '01';
				} else {
					$date_parsed[$date_part] = '00';
				}
				continue;
			}
			$parsed_input = $input_date[$date_part];
			if (strlen ($parsed_input) < 2 && $date_part != 'y') {
				/* Years with one (or less) digits exist */
				$parsed_input = str_pad ($parsed_input, 2, '0', STR_PAD_LEFT);
			}
			$date_parsed[$date_part] = $parsed_input;
		}
		$parsed_date = sprintf ($parsable_date,
									$date_parsed['y'],
									$date_parsed['m'],
									$date_parsed['d'],
									$date_parsed['h'],
									$date_parsed['i'],
									$date_parsed['s']);
		$this->dt = DateTime::createFromFormat ('Y-m-d H:i:s', $parsed_date);
		return $this->dt;
	}
}

?>
