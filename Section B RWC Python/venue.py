class Venue:
    def __init__(self, new_venue_name, new_city):
        self.venue_name = new_venue_name
        self.city = new_city

    def __str__(self):
        return f'{self.venue_name}, {self.city}'