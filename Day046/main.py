import requests
from bs4 import BeautifulSoup
import spotipy # The documentation for the spotify API is awful
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

### Step 1 - Scraping the Billboard Hot 100 ###
billboard_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{billboard_date}")
response.raise_for_status()
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")

song_titles = [song_tile.get_text().strip() for song_tile in soup.select(selector="li ul li #title-of-a-story")]

### Step 2 - Authentication with Spotify ###
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_UI")
USERNAME = os.getenv("SPOTFIY_USERNAME")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME, 
    )
)

user_id = sp.current_user()["id"]

###  Step 3 - Search Spotify for the Songs from Step 1 ###
song_uris = []
year = billboard_date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

### Step 4 - Creating and Adding to Spotify Playlist ###
playlist = sp.user_playlist_create(user=user_id, name=f"{billboard_date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
