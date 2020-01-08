import unittest
import controller
from match import Match


class TestAddMatches(unittest.TestCase):
	def test_a_display_match__str__exists(self):
		match = Match('when', 'team_a', 'team_b', 'venue', 'pool')
		self.assertTrue(type(match).__str__ is not object.__str__)

	def test_b_display_member__str__returns_string(self):
		match = Match('when', 'team_a', 'team_b', 'venue', 'pool')
		returned = str(match)
		self.assertTrue(isinstance(returned, str))

	def test_d_display_teams_correct_format(self):
		the_rwc = controller.setup()
		returned = the_rwc.display_teams()
		self.assertEqual(returned,
		                 "Argentina\nAustralia\nCanada\nEngland\nFiji\nFrance\nGeorgia\nIreland\nItaly\nJapan\nNamibia\nNew Zealand\nRussia\nSamoa\nScotland\nSouth Africa\nTonga\nUnited States\nUruguay\nWales\n")

	def test_e_display_pools_correct_format(self):
		the_rwc = controller.setup()
		returned = the_rwc.display_pools()
		self.assertEqual(returned, "A\nB\nC\nD\n")

	def test_f_display_pools_team_format(self):
		the_rwc = controller.setup()
		returned = the_rwc.display_teams_pools()
		self.assertEqual(returned,
		                 "A\nIreland\nScotland\nJapan\nRussia\nSamoa\nB\nNew Zealand\nSouth Africa\nItaly\nNamibia\nCanada\nC\nEngland\nFrance\nArgentina\nUnited States\nTonga\nD\nAustralia\nWales\nGeorgia\nFiji\nUruguay\n")

	def test_g_display_matches_date_format(self):
		the_rwc = controller.setup()
		returned = the_rwc.display_matches_date()
		self.assertEqual(returned,
		                 "2019-09-20 00:00:00 Japan Russia Tokyo Stadium, Chofu A\n2019-09-21 00:00:00 New Zealand South Africa International Stadium Yokohama, Yokohama B\n2019-09-21 00:00:00 France Argentina Tokyo Stadium, Chofu C\n2019-09-21 00:00:00 Australia Fiji Sapporo Dome, Sapporo D\n2019-09-22 00:00:00 Ireland Scotland International Stadium Yokohama, Yokohama A\n2019-09-22 00:00:00 Italy Namibia Hanazono Rugby Stadium, Higashiosaka B\n2019-09-22 00:00:00 England Tonga Sapporo Dome, Sapporo C\n2019-09-23 00:00:00 Wales Georgia City of Toyota Stadium, Toyota D\n2019-09-24 00:00:00 Russia Samoa Kumagaya Rugby Stadium, Kumagaya A\n2019-09-25 00:00:00 Fiji Uruguay Kamaishi Recovery Memorial Stadium, Kamaishi D\n2019-09-26 00:00:00 Italy Canada Fukuoka Hakatanomori Stadium, Fukuoka B\n2019-09-26 00:00:00 England United States Kobe Misaki Stadium, Kobe C\n2019-09-28 00:00:00 Japan Ireland Shizuoka Stadium Ecopa, Fukuroi A\n2019-09-28 00:00:00 South Africa Namibia City of Toyota Stadium, Toyota B\n2019-09-28 00:00:00 Argentina Tonga Hanazono Rugby Stadium, Higashiosaka C\n2019-09-29 00:00:00 Georgia Uruguay Kumagaya Rugby Stadium, Kumagaya D\n2019-09-29 00:00:00 Australia Wales Tokyo Stadium, Chofu D\n2019-09-30 00:00:00 Scotland Samoa Kobe Misaki Stadium, Kobe A\n2019-10-02 00:00:00 New Zealand Canada Oita Stadium, Oita B\n2019-10-02 00:00:00 France United States Fukuoka Hakatanomori Stadium, Fukuoka C\n2019-10-03 00:00:00 Ireland Russia Kobe Misaki Stadium, Kobe A\n2019-10-03 00:00:00 Georgia Fiji Hanazono Rugby Stadium, Higashiosaka D\n2019-10-04 00:00:00 South Africa Italy Shizuoka Stadium Ecopa, Fukuroi B\n2019-10-05 00:00:00 Japan Samoa City of Toyota Stadium, Toyota A\n2019-10-05 00:00:00 England Argentina Tokyo Stadium, Chofu C\n2019-10-05 00:00:00 Australia Uruguay Oita Stadium, Oita D\n2019-10-06 00:00:00 New Zealand Namibia Tokyo Stadium, Chofu B\n2019-10-06 00:00:00 France Tonga Kumamoto Stadium, Kumamoto C\n2019-10-08 00:00:00 South Africa Canada Kobe Misaki Stadium, Kobe B\n2019-10-09 00:00:00 Scotland Russia Shizuoka Stadium Ecopa, Fukuroi A\n2019-10-09 00:00:00 Argentina United States Kumagaya Rugby Stadium, Kumagaya C\n2019-10-09 00:00:00 Wales Fiji Oita Stadium, Oita D\n2019-10-11 00:00:00 Australia Georgia Shizuoka Stadium Ecopa, Fukuroi D\n2019-10-12 00:00:00 Ireland Samoa Fukuoka Hakatanomori Stadium, Fukuoka A\n2019-10-12 00:00:00 New Zealand Italy City of Toyota Stadium, Toyota B\n2019-10-12 00:00:00 England France International Stadium Yokohama, Yokohama C\n2019-10-13 00:00:00 Japan Scotland International Stadium Yokohama, Yokohama A\n2019-10-13 00:00:00 Namibia Canada Kamaishi Recovery Memorial Stadium, Kamaishi B\n2019-10-13 00:00:00 United States Tonga Hanazono Rugby Stadium, Higashiosaka C\n2019-10-13 00:00:00 Wales Uruguay Kumamoto Stadium, Kumamoto D\n")


if __name__ == '__main__':
	unittest.main(verbosity=3)
