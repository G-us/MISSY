from main import playSong

state = input("What is your state? ")

if state == "sad":
    playSong("sad", fade=True)
elif state == "jazz":
    playSong("jazz", fade=True)