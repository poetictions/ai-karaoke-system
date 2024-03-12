import requests

def fetch_top_songs(country='India', limit=20):
    # Last.fm API endpoint for fetching top tracks
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Parameters for the API request
    params = {
        'method': 'geo.gettoptracks',
        'country': country,
        'limit': limit,
        'api_key': 'e84b52ceb87cc110a392a2008b2fbbad',  # Replace 'YOUR_API_KEY' with your actual Last.fm API key
        'format': 'json'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the top tracks from the response
        top_tracks = data['tracks']['track']

        # Extract track names from the top tracks
        top_song_names = [track['name'] for track in top_tracks]

        return top_song_names
    else:
        print('Failed to fetch top songs:', response.text)
        return None

# Fetch the top 20 songs in India
top_songs = fetch_top_songs(country='India', limit=20)
if top_songs:
    print("Top 20 Songs in India:")
    for i, song in enumerate(top_songs, start=1):
        print(f"{i}. {song}")
else:
    print("Failed to fetch top songs.")

import requests

def get_top_karaoke_songs(country='India', limit=50):
    api_key = 'e84b52ceb87cc110a392a2008b2fbbad'
    url = f'http://ws.audioscrobbler.com/2.0/?method=geo.getTopTracks&country=India&limit=50&api_key=e84b52ceb87cc110a392a2008b2fbbad&format=json'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        top_tracks = data['tracks']['track']
        karaoke_songs = [track['name'] for track in top_tracks]
        return karaoke_songs
    else:
        print("Failed to fetch data from Last.fm API")
        return []

if __name__ == "__main__":
    top_karaoke_songs = get_top_karaoke_songs()
    if top_karaoke_songs:
        print("Top 50 Karaoke Songs in India:")
        for i, song in enumerate(top_karaoke_songs, 1):
            print(f"{i}. {song}")
    else:
        print("No karaoke songs found.")

import requests

def fetch_top_karaoke_songs():
    api_key = "YOUR_LASTFM_API_KEY"
    endpoint = "http://ws.audioscrobbler.com/2.0/"

    params = {
        "method": "chart.getTopTracks",
        "api_key": "e84b52ceb87cc110a392a2008b2fbbad",
        "format": "json",
        "limit": 50,
        "country": "India",
        "lang": "hi",
        "tag": "karaoke"
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()
        if "tracks" in data and "track" in data["tracks"]:
            top_songs = data["tracks"]["track"]
            for index, song in enumerate(top_songs, start=1):
                print(f"{index}. {song['name']} by {song['artist']['name']}")
        else:
            print("No karaoke songs found.")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_top_karaoke_songs()

import requests

def fetch_popular_songs(artist_name, limit):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "artist.getTopTracks",
        "artist": "Harry Styles",
        "limit": 100,
        "api_key": "e84b52ceb87cc110a392a2008b2fbbad",
        "format": "json",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        top_tracks = response.json()["toptracks"]["track"]
        return top_tracks
    else:
        print("Failed to fetch data from Last.fm API")
        return []

# Example usage
artist_name = "Harry Styles"
limit = 100


top_tracks = fetch_popular_songs(artist_name, limit)
if top_tracks:
    print(f"Top {limit} popular songs by {artist_name}:")
    for index, track in enumerate(top_tracks, start=1):
        print(f"{index}. {track['name']}")
else:
    print("No popular songs found for the artist.")

import requests

def fetch_popular_songs(artist_name, limit):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "artist.getTopTracks",
        "artist": "One Direction",
        "limit": 100,
        "api_key": "e84b52ceb87cc110a392a2008b2fbbad",
        "format": "json",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        top_tracks = response.json()["toptracks"]["track"]
        return top_tracks
    else:
        print("Failed to fetch data from Last.fm API")
        return []

# Example usage
artist_name = "One Direction"
limit = 100


top_tracks = fetch_popular_songs(artist_name, limit)
if top_tracks:
    print(f"Top {limit} popular songs by {artist_name}:")
    for index, track in enumerate(top_tracks, start=1):
        print(f"{index}. {track['name']}")
else:
    print("No popular songs found for the artist.")

import requests

def fetch_top_tracks(artist_name, limit=100):
    api_key = 'e84b52ceb87cc110a392a2008b2fbbad'
    username = 'harrystyles'
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=harrystyles&api_key=e84b52ceb87cc110a392a2008b2fbbad&format=json&limit=100'

    response = requests.get(url)
    data = response.json()

    top_tracks = []
    for track in data['toptracks']['track']:
        track_name = track['name']
        artist = track['artist']['name']
        play_count = int(track['playcount'])
        top_tracks.append({'track_name': track_name, 'artist': artist, 'play_count': play_count})

    return top_tracks

if __name__ == '__main__':
    top_tracks = fetch_top_tracks('harrystyles', limit=100)
    print("Top 100 Songs by Harry Styles:")
    for i, track in enumerate(top_tracks, 1):
        print(f"{i}. {track['track_name']} by {track['artist']} - {track['play_count']} streams")