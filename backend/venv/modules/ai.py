import webbrowser
import os
import pywhatkit
import requests
import wikipediaapi

from datetime import datetime


def ask_ai(prompt):

    prompt = prompt.lower()

    # greetings
    if "hello" in prompt:
        return "Hello Yashraj, how can I help you?"

    elif "your name" in prompt:
        return "I am Nova, your AI assistant."

    # weather
    elif "weather" in prompt:

        try:

            city = "Bhubaneswar"

            url = f"https://wttr.in/{city}?format=3"

            response = requests.get(url)

            return response.text

        except Exception as e:

            print("Weather Error:", e)

            return "Weather service unavailable."

    # time
    elif "time" in prompt:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}"

    # websites
    elif "open youtube" in prompt:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    elif "open google" in prompt:

        webbrowser.open("https://google.com")

        return "Opening Google"

    elif "open github" in prompt:

        webbrowser.open("https://github.com")

        return "Opening GitHub"

    # apps
    elif "open chrome" in prompt:

        os.system("start chrome")

        return "Opening Chrome"

    elif "open vscode" in prompt:

        os.system("code")

        return "Opening Visual Studio Code"

    # play song
    elif "play" in prompt:

        song = prompt.replace("play", "").strip()

        pywhatkit.playonyt(song)

        return f"Playing {song} on YouTube"

    # wikipedia
    elif "who is" in prompt or "what is" in prompt:

        try:

            topic = prompt.replace("who is", "")
            topic = topic.replace("what is", "")
            topic = topic.strip()

            wiki = wikipediaapi.Wikipedia(
                language='en',
                user_agent='NovaAI/1.0'
            )

            page = wiki.page(topic)

            if page.exists():

                summary = page.summary[:400]

                return summary

            else:

                return "Sorry, I could not find information."

        except Exception as e:

            print("Wikipedia Error:", e)

            return "Wikipedia service unavailable."

    # stop
    elif "stop" in prompt or "bye" in prompt:

        return "Goodbye Yashraj"

    else:

        return "Sorry, I do not know that yet."