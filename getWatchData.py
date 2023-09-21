import asyncio
import websockets
import useWatchUtilities as uWu


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
                        uWu.useHeartData(int(heartRate))
        except websockets.exceptions.ConnectionClosed:
            print("Connection was closed. Reconnecting...")
        except Exception as e:
            print("An error occurred:", str(e))
        await asyncio.sleep(5)  # Wait for a few seconds before reconnecting


asyncio.get_event_loop().run_until_complete(receive_data())
