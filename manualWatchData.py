import main
import useWatchUtilities as uWu

while True:
    heartRate = input("Enter heart rate: ")
    uWu.useHeartData(int(heartRate))
