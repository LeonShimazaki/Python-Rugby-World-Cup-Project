from datetime import datetime
import json
from rwc import RWC
import matplotlib.pyplot as plt

def  setup():
    json_as_text = open('rwc.json', 'r').read()
    #print(json_as_text)
    rwc_json = json.loads(json_as_text)
    rwc = RWC(2019)
    team_names = rwc_json["teams"]
    team_names.sort()
    for new_name in team_names:
        #print(new_name)
        rwc.add_team(new_name)

    for new_name in rwc_json["pools"]:
        #print("Pool " + new_name)
        a_pool = rwc.add_pool(new_name)
        for existing_team_name in rwc_json["pools"][new_name]:
            #print('\t', existing_team_name)
            a_team = rwc.find_team(existing_team_name)
            a_pool.add_team(a_team)

    for match in rwc_json["round-robin"]:
        pool_name = match['pool']
        the_pool = rwc.find_pool(pool_name)
        new_when = datetime.strptime(match['when'], '%d %B %Y')
        existing_team_a_name = match['team_a']
        existing_team_b_name = match['team_b']
        venue_name = match['venue']
        city = match['city']
        #print("\n", new_when.date(), "\n", existing_team_a_name,"vs", existing_team_b_name, "\n",venue_name,",", city)
        the_team_a = rwc.find_team(existing_team_a_name)
        the_team_b = rwc.find_team(existing_team_b_name)
        the_venue = rwc.add_venue_if_new(venue_name, city)
        a_match = rwc.add_match(new_when, the_team_a, the_team_b, the_venue, the_pool)
        the_pool.add_match(a_match)

    #print(str(rwc))


    rwc.add_result('Russia', 10, 1, 'Japan', 30, 4)
    rwc.add_result('Ireland', 27, 4, 'Scotland', 3, 0)
    rwc.add_result('England', 35, 4, 'Tonga', 3, 0)
    rwc.add_result('Russia', 9, 0, 'Samoa', 34, 6)
    rwc.add_result('Japan', 19, 1, 'Ireland', 12, 2)
    rwc.add_result('Scotland', 34, 2, 'Samoa', 0, 0)
    rwc.add_result('Ireland', 35, 5, 'Russia', 0, 0)
    rwc.add_result('Japan', 38, 4, 'Samoa', 19, 1)
    rwc.add_result('Scotland', 61, 9, 'Russia', 0, 0)
    rwc.add_result('Ireland', 47, 7, 'Samoa', 5, 1)
    rwc.add_result('Japan', 28, 4, 'Scotland', 21, 3)

    rwc.add_result('New Zealand', 23, 2, 'South Africa', 13, 1)
    rwc.add_result('Italy', 47, 6, 'Namibia', 22, 3)
    rwc.add_result('Italy', 48, 6, 'Canada', 7, 1)
    rwc.add_result('South Africa', 57, 9, 'Namibia', 3, 0)
    rwc.add_result('New Zealand', 63, 8, 'Canada', 0, 0)
    rwc.add_result('South Africa', 49, 7, 'Italy', 3, 0)
    rwc.add_result('New Zealand', 71, 11, 'Namibia', 9, 0)
    rwc.add_result('South Africa', 66, 10, 'Canada', 7, 1)
    rwc.add_result('New Zealand', 0, 0, 'Italy', 0, 0)
    rwc.add_result('Namibia', 0, 0, 'Canada', 0, 0)


    rwc.add_result('France', 23, 2, 'Argentina', 21, 2)
    rwc.add_result('England', 35, 4, 'Tonga', 3, 0)
    rwc.add_result('England', 45, 6, 'United States', 7, 1)
    rwc.add_result('Argentina', 28, 4, 'Tonga', 12, 2)
    rwc.add_result('France', 33, 5, 'United States', 9, 0)
    rwc.add_result('England', 39, 6, 'Argentina', 10, 1)
    rwc.add_result('France', 23, 2, 'Tonga', 21, 3)
    rwc.add_result('Argentina', 47, 7, 'United States', 17, 3)
    rwc.add_result('England', 0, 0, 'France', 0, 0)
    rwc.add_result('United States', 19, 3, 'Tonga', 31, 4)

    rwc.add_result('Australia', 39, 6, 'Fiji', 21, 2)
    rwc.add_result('Wales', 43, 6, 'Georgia', 14, 2)
    rwc.add_result('Fiji', 27, 5, 'Uruguay', 30, 3)
    rwc.add_result('Georgia', 33, 5, 'Uruguay', 7, 1)
    rwc.add_result('Australia', 25, 3, 'Wales', 29, 2)
    rwc.add_result('Georgia', 10, 1, 'Fiji', 45, 7)
    rwc.add_result('Australia', 45, 3, 'Uruguay', 10, 1)
    rwc.add_result('Wales', 29, 4, 'Fiji', 17, 2)
    rwc.add_result('Australia', 27, 4, 'Georgia', 8, 1)
    rwc.add_result('Wales', 35, 4, 'Uruguay', 13, 1)

    return rwc

if __name__ == '__main__':
    the_rwc = setup()

    print(str(the_rwc.display_teams()))
    print(str(the_rwc.display_pools()))
    print(str(the_rwc.display_teams_by_pool()))
    print(str(the_rwc.display_matches_by_date()))
    print(str(the_rwc.display_matches_by_venue()))
    print(str(the_rwc.display_matches_by_team()))

    x = ""
    Y = ""
    x=[(str(the_rwc.display_teams()))]
    y=[(str(the_rwc.display_teams()))]
    plt.plot(x,y)
    plt.show()