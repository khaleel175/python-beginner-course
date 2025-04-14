import os
import webbrowser
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None
        except sr.WaitTimeoutError:
            speak("You took too long to respond.")
            return None

def execute_command(command):
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open browser" in command:
        speak("Opening browser")
        webbrowser.open("https://www.google.com")
    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    speak("Voice control activated. How can I assist you?")
    while True:
        command = take_command()
        if command:
            execute_command(command)