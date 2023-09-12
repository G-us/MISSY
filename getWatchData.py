import asyncio
import websockets

import main


# States = 0: resting, 1: high heart rate, 2: low heart rate
state = 0
def useHeartData(heartRate):
    global state
    if heartRate > 80 and state != 1:
        print("Heart rate is too high!")
        main.playSong("spotify:track:7cO24uuqaMv6YPImQinBgQ", fade=True)
        print(state)
        state = 1
        print(state)
    elif heartRate < 75 and state != 2:
        print("Heart rate is too low!")
        main.playSong("spotify:track:3qs1ozCx271UQqmzC7oNuj", fade=True)
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

asyncio.get_event_loop().run_until_complete(receive_data())




