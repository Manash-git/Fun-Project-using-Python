import pyttsx3

friend = pyttsx3.init()
# friend.say("Hi dude")

speech = input("Say: ")
friend.say(speech)

friend.runAndWait()