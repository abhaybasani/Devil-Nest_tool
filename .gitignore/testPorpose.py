# from pyfiglet import figlet_format
# text=figlet_format("Devil Nest",font='big')
# print(text)
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
    print("Speak.....!")
    audio = recognizer.listen(mic)
    print("Convert voice to text.......")
    print(0)
    text = recognizer.recognize_google(audio)
    print(1)
    text = text.lower()
    print(f"Recognized:> {text}")
