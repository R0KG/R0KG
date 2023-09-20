from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "8fcb36bc15784d9bb1de5011025dca2b"
CLIENT_SECRET = "da944860b6f843b09fc84fd979fc85e3"
wish_date = input("Which year do you want to travel to? Format YYYY-MM-DD: ")
website_url = f"https://www.billboard.com/charts/hot-100/{wish_date}/"

response = requests.get(url=website_url).text
soup = BeautifulSoup(response,"html.parser")
titles = soup.select("li ul li h3")
titles_music = [title.get_text().strip() for title in titles]
spot_header = {
    "Content-Type" : "application/x-www-form-urlencoded"
}
spot_params = {
    "grant_type" : "client_credentials",
    "client_id" : CLIENT_ID,
    "client_secret" : CLIENT_SECRET 
}

spotify_response = requests.post(url="https://accounts.spotify.com/api/token",headers=spot_header,data=spot_params).json()
auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:3000",scope="playlist-modify-public")
sp = spotipy.Spotify(auth_manager=auth_manager)

user_info = sp.current_user()
user_id = user_info['id']
0
playlist_name = f"Top 100 of the date {wish_date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name)
for track_name in titles_music:
    results = sp.search(q=track_name, type="track", limit=1)

    if results["tracks"]["items"]:
        track_uri = results["tracks"]["items"][0]["uri"]
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=[track_uri])
        print(f"Added {track_name} to the playlist.")
    else:
        print(f"No results found for track: {track_name}")

    
