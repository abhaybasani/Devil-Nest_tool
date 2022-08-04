def X():
    import speech_recognition
    import pyttsx3

    while True:
        recognizer=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.1)
                print("Speak.....!")

                audio=recognizer.listen(mic)
                print("Convert voice to text.......")
                text=recognizer.recognize_google(audio)
                print()
                text=text.lower()
                print(f"Recognized:> {text}")
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            continue
        except TypeError:
            print("type error")
        except:
            print("program is finished")


X()
