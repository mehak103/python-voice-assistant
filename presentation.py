import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia
import os

engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print("You:", query)
        return query.lower()
    except:
        speak("Sorry, I didn't understand. Please say again.")
        return ""

def process(query):

    # TIME
    if "time" in query or "what's the time" in query or "time kya" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        return

    # DATE
    if "date" in query or "aaj ki date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
        return

    # OPEN GOOGLE
    if "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return

    # OPEN YOUTUBE
    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return

    # OPEN WHATSAPP
    if "open whatsapp" in query or "whatsapp" in query:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
        return

    # SEARCH GOOGLE
    if "search" in query:
        q = query.replace("search", "")
        speak(f"Searching {q}")
        pywhatkit.search(q)
        return

    # PLAY SONG YOUTUBE
    if "play" in query or "song" in query:
        song = query.replace("play", "").replace("song", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        return

    # WIKIPEDIA
    if "who is" in query or "what is" in query or "wikipedia" in query:
        topic = query.replace("who is", "").replace("what is", "").replace("wikipedia", "")
        speak("Let me check...")
        try:
            info = wikipedia.summary(topic, sentences=2)
            speak(info)
        except:
            speak("Sorry, I couldn't find anything.")
        return

    # NOTEPAD
    if "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")
        return

    # CHROME
    if "open chrome" in query:
        speak("Opening Chrome")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
        else:
            speak("Chrome not found.")
        return

    # EXIT
    if "exit" in query or "stop" in query or "bye" in query:
        speak("Goodbye! Have a nice day.")
        exit()

    # DEFAULT – WIKI
    speak("Let me search that...")
    try:
        ans = wikipedia.summary(query, sentences=2)
        speak(ans)
    except:
        speak("Sorry, I didn't understand.")

def main():
    speak("Hello Mehak, I am your assistant. How can I help you?")
    while True:
        q = listen()
        process(q)

if __name__ == "__main__":
    main()
