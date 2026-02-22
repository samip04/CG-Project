import speech_recognition as sr
import pyttsx3
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen through microphone and convert speech to text using Google API"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
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

def ask_openai(question):
    """Get answer from OpenAI GPT"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user", "content": question}]
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {e}"

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your online voice assistant. Ask me anything.")

    while True:
        command = listen().lower()

        if "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a nice day.")
            break
        elif command:
            answer = ask_openai(command)
            speak(answer)
