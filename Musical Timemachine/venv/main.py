from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load Spotify credentials
load_dotenv()

# ---------------- BILLBOARD SCRAPING ----------------
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url=billboard_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# Song titles
song_names_spans = soup.select("li h3#title-of-a-story")
song_names = [song.get_text(strip=True) for song in song_names_spans]

# Artists (a-no-trucate spans hold artist names)
artist_spans = soup.select("li span.a-no-trucate")
artists = [artist.get_text(strip=True) for artist in artist_spans]

songs = list(zip(song_names, artists))
print(f"🎶 Found {len(songs)} songs on Billboard for {date}")

# ---------------- SPOTIFY AUTH ----------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:3000/",   # must also be added in your Spotify Dev App
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print("✅ Logged in as:", user_id)

# ---------------- SEARCH SONGS ON SPOTIFY ----------------
song_uris = []
year = date.split("-")[0]

for title, artist in songs:
    uri = None

    # 1. Try track + artist + year
    result = sp.search(q=f"track:{title} artist:{artist} year:{year}", type="track", limit=1)
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]

    # 2. Try track + artist
    if not uri:
        result = sp.search(q=f"track:{title} artist:{artist}", type="track", limit=1)
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]

    # 3. Try track only
    if not uri:
        result = sp.search(q=f"track:{title}", type="track", limit=1)
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]

    # Save result
    if uri:
        song_uris.append(uri)
        print(f"✔️ Found: {title} - {artist}")
    else:
        print(f"❌ Not found: {title} - {artist}")

print(f"✅ Collected {len(song_uris)} Spotify URIs out of {len(songs)} songs")

# ---------------- CREATE PLAYLIST ----------------
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard Hot 100",
    public=False,
    description=f"Top 100 songs from Billboard on {date}"
)

print("🎧 Created Playlist:", playlist["name"])

# ---------------- ADD SONGS TO PLAYLIST ----------------
if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print(f"✅ Added {len(song_uris)} songs to playlist")
else:
    print("⚠️ No songs were added.")
