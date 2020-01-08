class Match:
    def __init__(self, new_when, new_the_team_a, new_the_team_b, new_the_venue, new_the_pool):
        self.when = new_when
        self.my_team_a = new_the_team_a
        self.my_team_b = new_the_team_b
        self.the_venue = new_the_venue
        self.the_pool = new_the_pool

        #self.team_a_scores = new_team_a_scores
        #self.team_a_tries = new_team_a_tries
        #self.team_b_scores = new_team_b_scores
        #self.team_b_tries = new_team_b_tries

    def setResult(self, team_a_scores, team_a_tries, team_b_scores, team_b_tries):
        #add_result = Result(my_team_a, team_a_score, team_a_tries, my_team_b, team_b_score, team_b_tries)
        #self.all_my_results.append(add_result)
        pass

    def __str__(self):
        return f'{self.when}, {self.my_team_a}, {self.my_team_b}, {self.the_venue}, {self.the_pool}'