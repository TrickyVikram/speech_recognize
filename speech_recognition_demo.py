import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to capture and recognize speech
def recognize_speech():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to the speech input

    try:
        # Recognize speech using Google's free speech recognition API
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Save recognized text to a file
        with open("recognized_text.txt", "w") as file:
            file.write(text)
        print("Text has been saved to 'recognized_text.txt'")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the function
if __name__ == "__main__":
    recognize_speech()
