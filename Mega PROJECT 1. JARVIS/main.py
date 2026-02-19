import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def proccesscommand(c):
    c = c.lower().strip()
    if "open google" in c:
        speak("opening google")
        webbrowser.open("http://google.com")
    elif "open instagram" in c:
        speak("opening instagram")
        webbrowser.open("http://instagram.com")
    elif "open facebook" in c:
        speak("opening facebook")
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c:
        speak("opening youtube")
        webbrowser.open("http://youtube.com")
    elif c.startswith("play"):
        words = c.split()[1:]
        query = " ".join(words).strip()
        if query in music_library.music:
            webbrowser.open(music_library.music[query])
        return

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    r = sr.Recognizer()
    print("Hi!....")
    while True:
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
            word = r.recognize_google(audio).lower()
            print(f"You said: {word}")
            if word.lower() == "jarvis":
                speak("yes sir!")
                print("Activated!..")
                with sr.Microphone() as source:
                    print("Waiting for command...")
                    audio2 = r.listen(source, timeout=5, phrase_time_limit=4)
                command = r.recognize_google(audio2)
                print(f"Command: {command}")
                proccesscommand(command)
        except Exception as e:
            print("Error; {0}".format(e))