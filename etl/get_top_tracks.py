import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os

CLIENT_ID = 'c4c83187bd324bb48b8928c3c12447f5'
CLIENT_SECRET = '80a317c6a79c443eb71ef0f14dc38176'
REDIRECT_URI = 'http://127.0.0.1:8888/callback' 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read"
))

def get_top_tracks():
    results = sp.current_user_top_tracks(limit=20, time_range='medium_term')
    tracks = []
    for item in results['items']:
        tracks.append({
            'Track': item['name'],
            'Artist': item['artists'][0]['name'],
            'Album': item['album']['name'],
            'Popularity': item['popularity'],
            'Release Date': item['album']['release_date']
        })
    df = pd.DataFrame(tracks)
    df.to_csv("data/top_tracks.csv", index=False)
    print("✅ Saved to data/top_tracks.csv")

if __name__ == "__main__":
    get_top_tracks()
