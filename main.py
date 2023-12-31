import spotipy
from spotipy.oauth2 import SpotifyOAuth
import apscheduler
import asyncio
import websockets

sad = "spotify:track:6xCCgnYGGDWVXqfHzdMkCQ"
jazz = "spotify:track:2ifRmHoyg1f2pUtFhlqrn2"
waiting = "spotify:track:1ZlnsAT3J7vmf0xuOMHD9V"

scope = "user-library-read, streaming, user-read-playback-state, user-modify-playback-state, user-read-currently-playing"
print("Opening Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

state = 0


def useHeartData(heartRate, SpotifyPlay):
    global state
    if heartRate > 90 and state != 1:
        print("Heart rate is too high!")
        playSong("spotify:track:7cO24uuqaMv6YPImQinBgQ", fade=False, sp=SpotifyPlay)
        print(state)
        state = 1
        print(state)
    elif heartRate < 60 and state != 2:
        print("Heart rate is too low!")
        playSong("spotify:track:3qs1ozCx271UQqmzC7oNuj", fade=False, sp=SpotifyPlay)
        print(state)
        state = 2
        print(state)


async def receive_data():
    uri = "ws://localhost:3476"

    while True:
        # noinspection PyUnresolvedReferences
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    data = await websocket.recv()
                    print("Received:", data)
                    if "heartRate" in data:
                        heartRate = data.split(":")[1]
                        useHeartData(int(heartRate), sp)
        except websockets.exceptions.ConnectionClosed:
            print("Connection was closed. Reconnecting...")
        except Exception as e:
            print("An error occurred:", str(e))
        await asyncio.sleep(5)  # Wait for a few seconds before reconnecting


def playSong(uri, fade, sp):
    if fade:
        startingVolume = sp.current_playback()["device"]["volume_percent"]
        for i in range(startingVolume, 0):
            print(i)
            print("Raising volume")
            sp.volume(i)
        sp.start_playback(uris=[uri])


if __name__ == "__main__":

    mode = input("Enter mode: ")

    if mode == "watch":
        asyncio.get_event_loop().run_until_complete(receive_data())

state = 0
