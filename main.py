
import apscheduler
import asyncio
import websockets

sad = "spotify:track:6xCCgnYGGDWVXqfHzdMkCQ"
jazz = "spotify:track:2ifRmHoyg1f2pUtFhlqrn2"
waiting = "spotify:track:1ZlnsAT3J7vmf0xuOMHD9V"



state = 0


def playSong(uri, fade):
    if fade:
        for i in range(100):
            print(i)
            print("Raising volume: " + str(i))
        print("Playing song: " + uri)










if __name__ == "__main__":

    mode = input("Enter mode: ")

    if mode == "w":
        import getWatchData
    elif mode == "m":
        import manualData

state = 0
