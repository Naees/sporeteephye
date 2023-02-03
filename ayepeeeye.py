import requests
import pandas as pd

# Step 1: Define your API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"

# Step 2: Retrieve an access token
auth_url = "https://accounts.spotify.com/api/token"
auth_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}
auth_response = requests.post(auth_url, data=auth_data)
access_token = auth_response.json()["access_token"]

# Step 3: Make API requests to retrieve playlist data
headers = {
    "Authorization": "Bearer {}".format(access_token)
}
playlist_url = "https://api.spotify.com/v1/playlists/{playlist_id}"
playlist_response = requests.get(playlist_url, headers=headers)
playlist_data = playlist_response.json()

# Step 4: Store the data in a pandas DataFrame
songs = playlist_data["tracks"]["items"]
song_data = []
for song in songs:
    song_info = {
        "track_name": song["track"]["name"],
        "artist_name": song["track"]["artists"][0]["name"],
    }
    song_data.append(song_info)
df = pd.DataFrame(song_data)

# Step 5: Categorize the songs based on their genres
# This step will vary depending on the specific classification method you choose to use.
