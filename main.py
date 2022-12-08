from requests import get
from pprint import PrettyPrinter


BASE_URL = 'https://data.nba.net'
ALL_JSON = '/prod/v1/today.json'


p = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links_array = data['links']
    return links_array

def get_scoreboard():
    scoreboard_URL = get_links()['currentScoreboard']
    scoreboard = get(BASE_URL + scoreboard_URL).json()['games']
    for game in scoreboard:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        venue = game['arena']['name']
        city =  game['arena']['city']
        if game['period']['isHalftime']:
            pd = "Halftime!"
        elif game['period']['current'] == 0: 
            pd = f"starts at {game['startTimeEastern']}"
        else:
            pd = f"period {game['period']['current']}"
        print('-----------------------------------------------')
        print(f"{home_team['triCode']} vs {away_team['triCode']} @ {venue} ({city}) - {pd} {clock}")
        if  game['period']['current'] != 0: 
            print(f"{home_team['score']} - {away_team['score']}")


def main():
    get_scoreboard()

    # p.pprint(get_links())


    return 0



if __name__ == "__main__":
    main()