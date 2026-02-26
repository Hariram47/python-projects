import webbrowser
import pywhatkit
import wikipedia
import datetime
import requests
import os
from speech_engine.speaker import speak

API_KEY = "aaf1458880b586017226133162d53966"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            speak("City not found.")
            return

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        speak(f"The temperature in {city} is {temperature} degree Celsius with {description}")
    except:
        speak("Unable to fetch weather information.")


def handle_command(command):

    command = command.lower()

    if any(word in command for word in ["stop", "exit", "quit", "that's all"]):
        speak("Goodbye Hariram")
        exit()

    if "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
        return

    if "date" in command or "today" in command:
        today = datetime.date.today()
        formatted_date = today.strftime("%B %d, %Y")
        speak(f"Today is {formatted_date}")
        return

    if "weather" in command:
        words = command.split()
        if "in" in words:
            city_index = words.index("in") + 1
            city = " ".join(words[city_index:])
            get_weather(city)
            return
        else:
            speak("Please specify the city name.")
            return

    if "play" in command and "youtube" in command:
        try:
            song = command.replace("play", "").replace("in youtube", "").replace("youtube", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            return
        except:
            speak("Unable to play on YouTube.")
            return

    if "open" in command:

        if "chrome" in command:
            os.system("start chrome")
            speak("Opening Chrome")
            return

        if "edge" in command:
            os.system("start msedge")
            speak("Opening Edge")
            return

        if "notepad" in command:
            os.system("start notepad")
            speak("Opening Notepad")
            return

        if "calculator" in command:
            os.system("start calc")
            speak("Opening Calculator")
            return

        words = command.split()
        try:
            index = words.index("open")
            site = words[index + 1]
            url = f"https://www.{site}.com"
            webbrowser.open(url)
            speak(f"Opening {site}")
            return
        except:
            speak("Please specify a valid website.")
            return

    if any(phrase in command for phrase in ["explain", "what is", "who is", "where is"]):
        try:
            topic = command.replace("explain", "") \
                          .replace("what is", "") \
                          .replace("who is", "") \
                          .replace("where is", "") \
                          .strip()

            speak(f"Searching for {topic}")
            results = wikipedia.search(topic)

            if not results:
                speak("I could not find anything on Wikipedia.")
                return

            page_title = results[0]
            summary = wikipedia.summary(page_title, sentences=2)

            speak(summary)

            page = wikipedia.page(page_title)
            webbrowser.open(page.url)

            return

        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please be more specific.")
            return

        except Exception as e:
            print(e)
            speak("Sorry, I could not retrieve information.")
            return

    speak("Command not recognized.")