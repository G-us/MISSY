import asyncio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import websockets

import main

# States = 0: resting, 1: high heart rate, 2: low heart rate
scope = "user-library-read, streaming, user-read-playback-state, user-modify-playback-state, user-read-currently-playing"







