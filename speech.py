import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen through microphone and convert speech to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen().lower()
        if "hello" in command:
            speak("Hi there! How are you?")
        elif "your name" in command:
            speak("I am your Python voice assistant.")
        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a nice day.")
            break
        elif command:
            speak("You said " + command)
