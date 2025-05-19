import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Connect to the API
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Choose artist
oliver_heldens_uri = 'spotify:artist:5nki7yRhxgM509M5ADlN1p'

# Get top 10 songs according to Documentation
results = spotify.artist_top_tracks(oliver_heldens_uri)

# Select tracks from dictionary and transform into DataFrame
tracks = results['tracks']
df = pd.DataFrame(tracks)

# Sort by top songs
top_songs = df[['name', 'popularity']].sort_values(by='popularity', ascending=False).head(9)

# Print Top 3 Songs by Oliver Heldens by popularity
print(top_songs.head(3))

# If we need to check column names we use: print(df.columns)

plt.figure(figsize=(8, 5))
plt.scatter(df['duration_ms'], df['popularity'], alpha=0.7, color='mediumseagreen')
plt.title('Duration vs Popularity of Oliver Heldens Tracks')
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.grid(True)
plt.tight_layout()
plt.show()

print('We can observer that there is no direct correlation between the duration of the song and it's popularity, leading us to think that these to variables are independent and irrelevant to one another. My point is that there are much more variables in play when determining the success of a song, so with only two variables we can't do much')