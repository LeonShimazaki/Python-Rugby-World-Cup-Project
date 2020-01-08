class Pool:
    def __init__(self, new_name):
        self.name = new_name
        self.all_my_teams = []
        self.all_my_matches = []

    def add_team(self, a_team):
        self.all_my_teams.append(a_team)

    def add_match(self, a_match):
        self.all_my_matches.append(a_match)

    def __str__(self):
        return f' Pool {self.name}'