import requests
import spotipy
import os
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

ID = os.environ["CLIENT_ID_SPOTIFY"]
SECRET = os.environ["CLIENT_SECRET_SPOTIFY"]

# Scraping Billboard 100
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
URL = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=ID,
        client_secret=SECRET,
        scope="playlist-modify-private",
        redirect_uri="https://www.example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Yeon"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billiboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)