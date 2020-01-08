import unittest
from rwc import RWC
from pool import Pool


class TestRWCCode(unittest.TestCase):

	def test_a_team_collection(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'all_my_teams'))
		self.assertTrue(type(rwc.all_my_teams) == list)

	def test_b_pool_collection(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'all_my_pools'))
		self.assertTrue(type(rwc.all_my_teams) == list)

	def test_c_venues_collection(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'all_my_venues'))
		self.assertTrue(type(rwc.all_my_venues) == list)

	def test_d_matches_collection(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'all_my_matches'))
		self.assertTrue(type(rwc.all_my_matches) == list)

	def test_f_sort_teams(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'sort_teams'))
		self.assertTrue(callable(getattr(rwc, 'sort_teams', None)))

	def test_f_sort_teams(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'sort_teams'))
		self.assertTrue(callable(getattr(rwc, 'sort_teams', None)))

	def test_g_add_pool(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'add_pool'))
		self.assertTrue(callable(getattr(rwc, 'add_pool', None)))

	def test_j_add_match(self):
		rwc = RWC(2019)
		self.assertTrue(hasattr(rwc, 'add_match'))
		self.assertTrue(callable(getattr(rwc, 'add_match', None)))


class TestStaringPoolCode(unittest.TestCase):
	def test_h_pool_properties(self):
		pool = Pool('New Zealand')
		self.assertTrue(hasattr(pool, 'name'))
		self.assertTrue(type(pool.all_my_matches) == list)


class TestStaringTeamCode(unittest.TestCase):
	def test_k_pool__str__exists(self):
		pool = Pool('pool')
		self.assertTrue(type(pool).__str__ is not object.__str__)

if __name__ == '__main__':
	unittest.main(verbosity=3)
