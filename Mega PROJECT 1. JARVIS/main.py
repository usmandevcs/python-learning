import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import datetime
import wikipedia
import pyjokes
import os
import subprocess
import psutil
import pyautogui
import speedtest
import requests
import random

class JarvisAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def process_command(self, c):
        c = c.lower().strip()
        if "open google" in c:
            self.speak("opening google")
            webbrowser.open("http://google.com")
        elif "open instagram" in c:
            self.speak("opening instagram")
            webbrowser.open("http://instagram.com")
        elif "open facebook" in c:
            self.speak("opening facebook")
            webbrowser.open("http://facebook.com")
        elif "open youtube" in c:
            self.speak("opening youtube")
            webbrowser.open("http://youtube.com")
        elif "play" in c:
            query = c.split("play", 1)[1].strip()
            
            # Check if the user specifically asked for youtube
            if "on youtube" in c:
                youtube_query = query.replace("on youtube", "").strip()
                self.speak(f"Playing {youtube_query} on YouTube")
                import pywhatkit
                pywhatkit.playonyt(youtube_query)
                return

            # Check hardcoded library
            if query in music_library.music:
                webbrowser.open(music_library.music[query])
            else:
                # Fallback to youtube search if not in library
                self.speak(f"Playing {query} on YouTube")
                import pywhatkit
                pywhatkit.playonyt(query)
            return

        # New Features
        elif "time" in c:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"Sir, the time is {time_str}")
        elif "date" in c:
            date_str = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Sir, today's date is {date_str}")
        elif "wikipedia" in c:
            self.speak("Searching Wikipedia...")
            query = c.split("wikipedia", 1)[1].strip()
            try:
                import warnings
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                self.speak("There are multiple results for this query. Please be more specific.")
            except wikipedia.exceptions.PageError:
                self.speak("I couldn't find any results for this query on Wikipedia.")
            except Exception:
                self.speak("An error occurred while fetching information from Wikipedia.")
        elif "joke" in c:
            joke = pyjokes.get_joke()
            print(joke)
            self.speak(joke)
        elif "take a note" in c or "write this down" in c or "remember this" in c:
            self.speak("What should I write, sir?")
            try:
                with sr.Microphone() as source:
                    print("listening for note...")
                    audio_note = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                note_text = self.recognizer.recognize_google(audio_note)
                with open("notes.txt", "a") as f:
                    f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {note_text}\n")
                self.speak("I have noted that down, sir.")
            except sr.UnknownValueError:
                self.speak("I didn't catch that, sir.")
            except sr.RequestError:
                self.speak("Sorry, my speech service is down.")
            except Exception as e:
                self.speak("Sorry, I couldn't write the note.")
                print(f"Error saving note: {e}")
        elif "open notepad" in c:
            self.speak("Opening Notepad")
            # For Windows
            try:
                subprocess.Popen("notepad.exe")
            except Exception as e:
                print(f"Failed to open notepad: {e}")
                self.speak("I failed to open notepad")
        elif "open calculator" in c:
            self.speak("Opening Calculator")
            try:
                subprocess.Popen("calc.exe")
            except Exception as e:
                print(f"Failed to open calculator: {e}")
                self.speak("I failed to open calculator")
        elif "open command prompt" in c or "open cmd" in c:
            self.speak("Opening Command Prompt")
            os.system("start cmd")
        elif "open word" in c or "microsoft word" in c:
            self.speak("Opening Microsoft Word")
            try:
                os.system("start winword")
            except Exception as e:
                self.speak("I couldn't find Microsoft Word on your system.")
        elif "open excel" in c or "microsoft excel" in c:
            self.speak("Opening Microsoft Excel")
            try:
                os.system("start excel")
            except Exception as e:
                self.speak("I couldn't find Microsoft Excel on your system.")
        elif "open spotify" in c:
            self.speak("Opening Spotify")
            try:
                os.system("start spotify")
            except Exception as e:
                self.speak("I couldn't find Spotify on your system.")
        
        # OS Control Integration
        elif "battery" in c:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "plugged in" if battery.power_plugged else "not plugged in"
                self.speak(f"Sir, the system is at {battery.percent} percent battery and is currently {plugged}.")
            else:
                self.speak("Sorry sir, I cannot read the battery status.")
        elif "shutdown" in c or "shut down" in c:
            self.speak("Shutting down the system. Goodbye sir.")
            os.system("shutdown /s /t 5")
        elif "restart" in c:
            self.speak("Restarting the system.")
            os.system("shutdown /r /t 5")
        elif "lock system" in c or "lock the screen" in c:
            self.speak("Locking the screen.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "volume up" in c:
            self.speak("Turning volume up.")
            pyautogui.press("volumeup", presses=5)
        elif "volume down" in c:
            self.speak("Turning volume down.")
            pyautogui.press("volumedown", presses=5)
        elif "mute" in c or "unmute" in c:
            self.speak("Toggling mute.")
            pyautogui.press("volumemute")
            
        elif "weather" in c:
            self.speak("Checking the weather...")
            try:
                res = requests.get("https://wttr.in/?format=3")
                self.speak(f"The current weather is {res.text}")
                print(res.text)
            except Exception:
                self.speak("Sorry, I couldn't get the weather information.")
        elif "screenshot" in c:
            self.speak("Taking a screenshot...")
            try:
                filename = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                pyautogui.screenshot(filename)
                self.speak("Screenshot saved.")
            except Exception:
                self.speak("I couldn't take a screenshot.")
        elif "internet speed" in c or "speed test" in c:
            self.speak("Testing internet speed, please wait a moment...")
            try:
                st = speedtest.Speedtest()
                download_speed = st.download() / 1_000_000
                upload_speed = st.upload() / 1_000_000
                self.speak(f"Download speed is {download_speed:.2f} Mbps, and upload speed is {upload_speed:.2f} Mbps.")
            except Exception:
                self.speak("I couldn't complete the speed test.")
                
        elif "where am i" in c or "my location" in c:
            self.speak("Let me track our location...")
            try:
                ipAdd = requests.get('https://api.ipify.org', timeout=5).text
                url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                geo_requests = requests.get(url, timeout=5)
                geo_data = geo_requests.json()
                city = geo_data.get('city', 'an unknown city')
                country = geo_data.get('country', 'an unknown country')
                self.speak(f"Sir, based on our IP, we are currently in {city}, {country}.")
            except Exception as e:
                self.speak("Sorry sir, I couldn't fetch our location.")
                print(f"Location error: {e}")
                
        elif "system status" in c or "cpu usage" in c:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
            self.speak(f"Sir, the CPU is at {cpu_usage} percent, and RAM usage is at {ram_usage} percent.")
            
        elif "flip a coin" in c or "toss a coin" in c:
            result = random.choice(["heads", "tails"])
            self.speak(f"The coin landed on {result}.")
            
        elif "roll a dice" in c or "roll a die" in c:
            result = random.randint(1, 6)
            self.speak(f"You rolled a {result}.")

        elif "exit" in c or "stop" in c or "quit" in c:
            self.speak("Goodbye sir, having a good day.")
            exit()
        else:
            self.speak("I am sorry sir, I did not understand that command.")

    def run(self):
        self.speak("Initializing Jarvis.....")
        print("Hi!....")
        
        while True:
            try:
                with sr.Microphone() as source:
                    print("\nlistening....")
                    self.recognizer.adjust_for_ambient_noise(source, duration=1.0)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
                word = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {word}")
                
                if "jarvis" in word:
                    self.speak("yes sir!")
                    print("Activated!..")
                    with sr.Microphone() as source:
                        print("Waiting for command...")
                        self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio2 = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
                    command = self.recognizer.recognize_google(audio2)
                    print(f"Command: {command}")
                    self.process_command(command)

            except sr.UnknownValueError:
                pass # Ignore background noise when waiting for wake word
            except sr.WaitTimeoutError:
                pass # Ignore timeouts when no one is speaking
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                pass # Ignore other minor exceptions to keep the loop running

if __name__ == "__main__":
    assistant = JarvisAssistant()
    assistant.run()