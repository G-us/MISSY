import spotipy
from spotipy.oauth2 import SpotifyOAuth
import apscheduler

sad = "spotify:track:6xCCgnYGGDWVXqfHzdMkCQ"
jazz = "spotify:track:2ifRmHoyg1f2pUtFhlqrn2"
waiting = "spotify:track:1ZlnsAT3J7vmf0xuOMHD9V"

scope = "user-library-read, streaming, user-read-playback-state, user-modify-playback-state, user-read-currently-playing"


def playSong(uri, fade, sp):
    if fade:
        startingVolume = sp.current_playback()["device"]["volume_percent"]
        for i in range(0, startingVolume):
            sp.volume(i)
        sp.start_playback(uris=[uri])


if __name__ == "__main__":

    sp.start_playback(uris=[waiting])

    mode = input("Enter mode: ")

    if mode == "watch":
        import getWatchData
