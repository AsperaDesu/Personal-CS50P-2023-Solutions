import wikipedia, wikipediaapi
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')

auth_manager=  SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager = auth_manager)


def main():
    menu = Menu(mainMenu = True, prompt = 'select an option from the menu : ', options = ['Search Artist', 'About', 'Exit'])
    while True:
        print('='*25)
        print('F E T C H T I F Y'.center(25))
        print('='*25)

        menu.initMenu()
        clear_terminal()

        match menu.choice:
            case '1':
                print('=' * 20)
                print('SEARCH ARTIST'.center(20))
                print('=' * 20)
                print()

                name = input('Artist Name: ')
                print()
                artist = Artist.searchArtist(name)
                clear_terminal()

                print()
                print(artist)
                print()
                artist.getTopTracks(5)

            case '2':
                print('=' * 20)
                print('ABOUT'.center(20))
                print('=' * 20)
                print()
                print('A fun Python project that lets you search for your favorite artists! Explore their Spotify profiles and discover their top tracks for a personalized musical journey.')
                print('''

Note : The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular.
       The artist's popularity is calculated from the popularity of all the artist's tracks.''')

            case '3':
                break

        input('\nPress Enter To Continue: ')
        clear_terminal()



class Menu():
    def __init__(self, options = [], choice = 1, mainMenu = False, prompt = ''):
        self.options = options
        self.choice = choice
        self.mainMenu = mainMenu
        self.prompt = prompt.title()

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, choice):
        self._choice = choice


    def initMenu(self):
        print('\n'.join([f'{num}. {option}'for num, option in enumerate(self._options, start = 1)]))
        self._choice = getChoice(prompt = self.prompt, limit = [1, len(self._options)] )



class Artist():
    keywords = ['musician', 'musical artist', 'singer', 'band','artist','music']

    def __init__(self, data : dict):
        self.URL = data['external_urls']['spotify']
        self.name = data['name']
        self.ID = data['id']
        self.genres = data['genres']
        self.followers = data['followers']['total']
        self.topTracks = sp.artist_top_tracks(self.ID)


    def getTopTracks(self, n : int) :
        for num, track in enumerate(self.topTracks['tracks'][:5], start = 1):
            print(f"{num}. {track['name']} (Released : {track['album']['release_date']})")
            print(f"    • Duration : {':'.join(convertToMinute(track['duration_ms']))}")
            print(f"    • Popularity : {track['popularity']}")
            print(f'    • Album : {track["album"]["name"]}')
            print(f"    • URL : {track['external_urls']['spotify']}")
            print()


    def getWikiPage(self):
        search = searchPage(self.name, self.keywords)

        if search:
            return search
        return '-'


    @classmethod
    def searchArtist(cls, name:str):
        search = sp.search(name, type='artist')

        artists = [artist for artist in search['artists']['items'][:5]]
        names = [artist['name'] for artist in artists]
        genres = [artist['genres'] for artist in artists]
        options = [f'{names[i]} ({(", ".join(genre)).title() if (genre := genres[i]) != [] else "-"})'
                   for i in range(5)]

        artistMenu = Menu(options, prompt = 'select the artist : ')
        artistMenu.initMenu()

        artistInfo = search['artists']['items'][int(artistMenu.choice) - 1]
        del artistMenu, options, genres, names, artists, search
        return cls(artistInfo)


    def __str__(self):
        return f'''{'=' * 30}
{self.name.center(30)}
{'=' * 30}
ID  : {self.ID}
URL : {self.URL}
Genres : {', '.join(self.genres).title()}
Followers : {self.followers:,.0f}

WIKIPEDIA PAGE :
{self.getWikiPage()}
'''



def convertToMinute(milliseconds : int):
    seconds = milliseconds // 1000

    minutes = seconds // 60
    remaining_seconds = seconds % 60

    return str(minutes), str(remaining_seconds).zfill(2)


def clear_terminal():
    # Clear terminal screen for Windows, Linux, and MacOS
    os.system('cls' if os.name == 'nt' else 'clear')


def matchList(match, matching):
    for i in match:
        for j in matching:
            if i in j:
                return True
    return False


def getChoice(limit = [], prompt = '> '):
    while True:
        try:
            choice = int(input(prompt))
            if limit != [] and len(limit) == 2:
                if limit[0] <= choice <= limit[1]:
                    return str(choice)

        except ValueError:
            pass


wiki = wikipediaapi.Wikipedia('Project (asperadesu@gmail.com)', 'en')
def searchPage(name : str, keywords = []):
    search = wikipedia.search(name)
    for title in search:
        try:
            page = wiki.page(title)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options(search)
            return searchPage(options)
        except Exception:
            page = wikipedia.page(title)

        categories = (page.categories)
        sections = (page.sections)

        try:
            if matchList(keywords, categories) or matchList(keywords, sections):
                return page.summary
        except TypeError:
            return


if __name__ == '__main__':
    main()