import spotipy
from spotipy.oauth2 import SpotifyOAuth

sad = "spotify:track:6xCCgnYGGDWVXqfHzdMkCQ"
jazz = "spotify:track:2ifRmHoyg1f2pUtFhlqrn2"
waiting = "spotify:track:4qkYiZablQoG7f0Qu4Nd1c"

scope = "user-library-read, streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

sp.start_playback(uris=[waiting])

mode = input("What does your heart desire? ")

if mode == "user":
    import userDecides
else:
    print("not valid")

def playSong(state):
    if state == "sad":
        sp.start_playback(uris=[sad])
    elif state == "jazz":
        sp.start_playback(uris=[jazz])
    else:
        print("what")
