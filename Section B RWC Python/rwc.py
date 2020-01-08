from team import Team
from pool import Pool
from venue import Venue
from match import Match

class RWC:
    def __init__(self, new_year):
        self.year = new_year
        self.all_my_teams = []
        self.all_my_pools = []
        self.all_my_venues = []
        self.all_my_matches = []

    def add_team (self, new_name):
        a_team = Team(new_name)
        self.all_my_teams.append(a_team)

    def add_pool (self, new_pool):
        a_pool = Pool(new_pool)
        self.all_my_pools.append(a_pool)
        return a_pool

    def find_team (self, existing_team_name):
        return next((team for team in self.all_my_teams if team.name == existing_team_name), None)

    def find_pool (self, pool_name):
        return next((pool for pool in self.all_my_pools if pool.name == pool_name), None)

    def add_venue_if_new(self, new_venue_name, new_city):
        a_venue = Venue(new_venue_name, new_city)
        self.all_my_venues.append(a_venue)
        return a_venue

    def add_match(self, new_when, the_team_a, the_team_b, the_venue, the_pool):
        a_match = Match(new_when, the_team_a, the_team_b, the_venue, the_pool)
        self.all_my_matches.append(a_match)
        return a_match

    def sort_teams(self):
        self.all_my_teams = sorted(self.all_my_teams, key=lambda team: team.name)

    def sort_matches_by_date(self):
        self.all_my_matches = sorted(self.all_my_matches, key=lambda match: match.when)

    def sort_matches_by_venue(self):
        self.all_my_matches = sorted(self.all_my_matches, key=lambda match: match.the_venue.venue_name)

    def sort_matches_by_team(self):
        self.all_my_matches = sorted(self.all_my_matches, key=lambda match: match.my_team_a.name)

    def __str__(self):
        return f'{self.year}'

    def find_match(self, the_team_a ,the_team_b):
        return next((match for match in self.all_my_matches if match.my_team_a.name == the_team_a and match.my_team_b.name == the_team_b
                     or
                     match.my_team_a.name == the_team_b and match.my_team_b.name == the_team_a), None)

    def add_result(self, my_team_a, team_a_scores, team_a_tries, my_team_b, team_b_scores, team_b_tries):
        the_match = self.find_match(my_team_a, my_team_b)
        return

    def display_teams(self):
        result = ''
        self.sort_teams()
        for team_a in self.all_my_teams:
            result += str(team_a) + '\n'
        return result

    def display_pools(self):
        result = ''
        for a_pool in self.all_my_pools:
            result += str(a_pool) + '\n'
        return result

    def display_teams_by_pool(self):
        result = ''
        for a_pool in self.all_my_pools:
            result += '\n' + str(a_pool) + '\n'
            for existing_team_name in a_pool.all_my_teams:
                result += '\t' + str(existing_team_name)
        return result

    def display_matches_by_date(self):
        result = ''
        self.sort_matches_by_date()
        for a_match in self.all_my_matches:
            result += str(a_match) + '\n'
        return result

    def display_matches_by_venue(self):
        result = ''
        self.sort_matches_by_venue()
        for a_match in self.all_my_matches:
            result +=  str(a_match) + '\n'
        return result

    def display_matches_by_team(self):
        result = ''
        self.sort_matches_by_team()
        for a_match in self.all_my_matches:
            result += str(a_match) + '\n'
        return result