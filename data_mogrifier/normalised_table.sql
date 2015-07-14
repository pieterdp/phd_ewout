/* Create */
DROP TABLE IF EXISTS `prisoner_Phase1`;
CREATE TABLE IF NOT EXISTS `prisoner_Phase1` (
`id` int(16) NOT NULL,
  `pp_id` int(16) NOT NULL,
  `p_ID` int(16) DEFAULT NULL,
  `v_ID` int(16) DEFAULT NULL,
  `Naam` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Voornaam` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Geslacht` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Leeftijd` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Lichaamslengte` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Inschrijvingsdatum` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Rolnummer` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Ontslagdatum` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Burgerlijke_staat` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Geletterdheid` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Pokkenletsel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Verminkingen` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Beroep_letterlijk` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Beroep_vertaling` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Beroep_cat` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `HISCO` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Misdrijf_letterlijk` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Misdrijf_vertaling` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Misdrijf_cat` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Rechtbank_plaats` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Rechtbank_soort` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Archief_bestand` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Archief_toegang` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Woonplaats_vertaling` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Woonplaats_NIS` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Woonplaats_8` int(16) DEFAULT NULL,
  `Woonplaats_1846` int(16) DEFAULT NULL,
  `Woonplaats_1876` int(16) DEFAULT NULL,
  `Geboorteplaats_vertaling` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Geboorteplaats_NIS` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Geboorteplaats_8` int(16) DEFAULT NULL,
  `Geboorteplaats_1846` int(16) DEFAULT NULL,
  `Geboorteplaats_1876` int(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
ALTER TABLE `prisoner_Phase1`
 ADD PRIMARY KEY (`id`), ADD KEY `p_ID` (`p_ID`), ADD KEY `v_ID` (`v_ID`), ADD KEY `pp_id` (`pp_id`);
ALTER TABLE `prisoner_Phase1`
MODIFY `id` int(16) NOT NULL AUTO_INCREMENT;
/***/

INSERT INTO `prisoner_Phase1` (pp_id, n_id, p_ID_old)
SELECT n.id, n.id, n.p_ID FROM prisonerBigTable_normalised n;


UPDATE `prisoner_Phase1` p , prisonerBigTable_normalised n, big_match b SET p.`pp_id`=n.`id`, p.p_ID=n.p_ID WHERE
p.n_id = b.id_match AND
n.id = b.id_matched;

/* Nu zitten ze er allemaal in */

UPDATE `prisoner_Phase1` r, Verblijf v, Gedetineerde d, prisonerBigTable_normalised p SET r.`p_ID`= d.Id_gedetineerde, r.`Naam`=d.Naam, r.`Voornaam`=d.Voornaam, r.`Geslacht`=d.Geslacht
WHERE 
d.Id_gedetineerde = v.Id_ged AND
p.p_ID = d.Id_gedetineerde AND
r.pp_id = p.id;

/* 2 */
UPDATE `prisoner_Phase1` r, Verblijf v, Gedetineerde d, prisonerBigTable_normalised p SET r.`v_ID`=v.Id_verblijf,
r.`Leeftijd`=v.Leeftijd, r.`Lichaamslengte`=v.Lichaamslengte_m, r.`Inschrijvingsdatum`=STR_TO_DATE(CONCAT_WS('-', v.Inschrijvingsdatum_d, v.Inschrijvingsdatum_m, v.Inschrijvingsdatum_j), '%e-%c-%Y'), r.`Rolnummer`=v.Rolnummer, r.`Ontslagdatum`=STR_TO_DATE(CONCAT_WS('-', v.Ontslagdatum_d, v.Ontslagdatum_m, v.Ontslagdatum_j), '%e-%c-%Y'), r.`Burgerlijke_staat`=v.Burgerlijke_staat, r.`Geletterdheid`=v.Geletterdheid, r.`Pokkenletsel`=v.Pokkenletsels, r.`Verminkingen`=v.Verminkingen
WHERE 
d.Id_gedetineerde = v.Id_ged AND
p.p_ID = d.Id_gedetineerde AND
r.n_id = p.id;

/* REST */
UPDATE prisoner_Phase1 r, Beroep b SET
r.Beroep_letterlijk=b.Beroep_letterlijk, r.Beroep_vertaling=b.Beroep_vertaling, r.Beroep_cat=b.Beroep_cat, r.HISCO=b.HISCO
WHERE
r.v_ID = b.Id_verb;

UPDATE prisoner_Phase1 r, Misdrijf m SET
r.Misdrijf_letterlijk=m.Misdrijf_letterlijk,
r.Misdrijf_vertaling=m.Misdrijf_vertaling,
r.Misdrijf_cat=m.Misdrijf_cat
WHERE
r.v_ID = m.Id_verbl;

UPDATE prisoner_Phase1 r, Rechtbank b SET
r.Rechtbank_plaats=b.Plaats,
r.Rechtbank_soort=b.Soort
WHERE
r.v_ID=b.Id_verb;

UPDATE prisoner_Phase1 r, Verblijf v, Archiefbestanden a SET
r.Archief_bestand=a.Archiefbestand,
r.Archief_toegang=a.Toegang
WHERE
r.v_ID=v.Id_verblijf AND
v.Id_archief=a.Id_archief;

UPDATE prisoner_Phase1 r, Woonplaats w, Geboorteplaats_UniekeWaarden g SET
r.Woonplaats_vertaling=w.Plaatsnaam_vertaling,
r.Woonplaats_NIS=g.NIS_CODE,
r.Woonplaats_8=g.`Jaar VIII`,
r.Woonplaats_1846=g.`1846`,
r.Woonplaats_1876=g.`1876`
WHERE
r.v_ID=w.Id_verbl AND
w.Plaatsnaam_vertaling=g.Plaatsnaam_vertaling;

UPDATE prisoner_Phase1 r, Geboorteplaats w, Geboorteplaats_UniekeWaarden g SET
r.Geboorteplaats_vertaling=w.Plaatsnaam_vertaling,
r.Geboorteplaats_NIS=g.NIS_CODE,
r.Geboorteplaats_8=g.`Jaar VIII`,
r.Geboorteplaats_1846=g.`1846`,
r.Geboorteplaats_1876=g.`1876`
WHERE
r.v_ID=w.Id_verbl AND
w.Plaatsnaam_vertaling=g.Plaatsnaam_vertaling;