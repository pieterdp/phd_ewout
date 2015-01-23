<?php

include_once ('skin.php');
include_once ('lib/html_generator.php');

class admin_page extends skin {

	protected $iconset;

	function __construct () {
		$this->iconset = load_icons ();
		return parent::__construct ();
	}

	/*
	 * Create a menu bar
	 * @param array $menu_items (optional) $menu_items[i] = array (name =>, link =>, icon => (optional))
	 * @return string $menu_bar
	 */
	protected function create_menu_bar ($menu_items = null) {
		$menu_wrapper = '<div class="admin-menu">
%s
</div>';
		$menu_c = '';
		if ($menu_items === null) {
			$menu_items = array (
				array (
					'name' => 'Gebruikersbeheer',
					'link' => 'administration.php?action=user',
					'icon' => 'person.gif'
				),
				array (
					'name' => 'Paginabeheer',
					'link' => 'administration.php?action=page',
					'icon' => 'clipboard.gif'
				)
			);
		}
		$mi = '<div class="admin-menu-item">
	<a href="%s" id="admin-menu-link%d" class="admin-menu-link"><img src="%s" class="admin-menu-link-img" alt="%s" /></a>
</div>';
		$i = 0;
		foreach ($menu_items as $menu_item) {
			$i++;
			if (!isset ($menu_item['icon'])) {
				$menu_item['icon'] = 'checkbox.gif';
			}
			$menu_c = $menu_c.sprintf ($mi, $menu_item['link'], $i, $this->iconset.$menu_item['icon'], $menu_item['name']);
		}
		return sprintf ($menu_wrapper, $menu_c);
	}

	/*
	 * Create a admin page with $content and a menu
	 * @param string $title
	 * @param string $content
	 * @param string $menu menu bar (optional)
	 * @return $page
	 */
	public function create_admin_page ($title, $content, $menu = null) {
		if ($menu === null) {
			$menu = $this->create_menu_bar ();
		}
		return $this->create_base_page ($title, $menu."\n".$content, '<link href="lib/html/minimal/admin.css" rel="stylesheet"></link>');
	}
}

?>
