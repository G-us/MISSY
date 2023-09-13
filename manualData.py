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


while True:
    heartRate = input("Enter heart rate: ")
    useHeartData(int(heartRate))
