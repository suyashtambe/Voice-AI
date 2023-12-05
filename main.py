import speech_recognition as sr
import os
import pyttsx3
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_application(application_name):
    # Example for opening Notepad on Windows
    os.system(f"start {application_name}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not get that. Please repeat.")
            return ""

if __name__ == '__main__':
    print('Listening for "Start" command...')
    say("Hello, I am Friday. Waiting for your command.")

    while True:
        query = takecommand()

        if "start" in query.lower():
            say("Hello, how may I assist you, sir?")
            break

    while True:
        print("Listening...")
        query = takecommand()

        sites = [["YouTube", "https://www.youtube.com"],
                 ["Google", "https://www.google.com"],
                 ["Wikipedia", "https://www.wikipedia.com"],
                 ["Spotify", "https://open.spotify.com/playlist/33VReTZ7AHfx21HOjc4UJJ"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "stop" in query.lower():
            say("Stopping listening. Have a great day!")
            break

        if "open notepad" in query.lower():
            say("Opening Notepad sir....")
            open_application("notepad.exe")

        
        if "how are you" in query.lower():
            say("I'm doing well, thank you for asking!")

        if "tell me a joke" in query.lower():
            say("Why did the computer go to therapy? It had too many bytes of emotional baggage!")

        if "who is your creator" in query.lower():
            say("I was created by OpenAI. They are a team of talented developers!")

        if "Thank you" in query.lower():
            say("Welcome its my pleasure to help you!")
  
