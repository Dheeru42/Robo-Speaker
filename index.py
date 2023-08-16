import win32com.client as wincom
if __name__ == '__main__':
    print("Welcome To Robo Speaker")
    while True:
        x = input("Enter your command:")
        speak = wincom.Dispatch("SAPI.SpVoice")
        if x == "q":
            speak.Speak("Bye Bye Friend")
            break
        command = x
        speak.Speak(command)
