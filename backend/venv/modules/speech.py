import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

            text = recognizer.recognize_google(audio)

            print("You said:", text)

            return text.lower()

    except sr.WaitTimeoutError:

        print("No speech detected")

        return ""

    except sr.UnknownValueError:

        print("Could not understand audio")

        return ""

    except sr.RequestError as e:

        print("API Error:", e)

        return ""

    except Exception as e:

        print("Error:", str(e))

        return ""