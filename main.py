
import apscheduler
import asyncio
import websockets

sad = "spotify:track:6xCCgnYGGDWVXqfHzdMkCQ"
jazz = "spotify:track:2ifRmHoyg1f2pUtFhlqrn2"
waiting = "spotify:track:1ZlnsAT3J7vmf0xuOMHD9V"



state = 0


def useHeartData(heartRate):
    global state
    if heartRate > 90 and state != 1:
        print("Heart rate is too high!")
        playSong("spotify:track:7cO24uuqaMv6YPImQinBgQ", fade=False)
        print(state)
        state = 1
        print(state)
    elif heartRate < 60 and state != 2:
        print("Heart rate is too low!")
        playSong("spotify:track:3qs1ozCx271UQqmzC7oNuj", fade=False)
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
                        useHeartData(int(heartRate))
        except websockets.exceptions.ConnectionClosed:
            print("Connection was closed. Reconnecting...")
        except Exception as e:
            print("An error occurred:", str(e))
        await asyncio.sleep(5)  # Wait for a few seconds before reconnecting


def playSong(uri, fade):
    if fade:

        for i in range(100, 0):
            print(i)
            print("Raising volume: " + str(i))
        print("Playing song: " + uri)


if __name__ == "__main__":

    mode = input("Enter mode: ")

    if mode == "watch":
        asyncio.get_event_loop().run_until_complete(receive_data())

state = 0
