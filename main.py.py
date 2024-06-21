import pyttsx3
import speech_recognition as sr
import datetime
import cv2
import pandas as pd
import pytesseract
from PIL import Image  

from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

# Load the saved model
tokenizer = AutoTokenizer.from_pretrained('ner_model')
model = AutoModelForTokenClassification.from_pretrained('ner_model')
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)
pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index as per your system's available voices

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def listen_for_response():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for response...")
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio)
            print("You said: " + response)
            return response.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def extract_entities(text):
    # Perform Named Entity Recognition (NER) using Hugging Face pipeline
    ner_results = ner_pipeline(text)
    
    # Initialize lists to store extracted data
    persons = []
    organizations = []
    locations = []
    miscellaneous = []


    # Define a set of possible car colors


    # Extract entities and classify them into types
    for entity in ner_results:
        if entity['entity_group'] == 'PER':
            persons.append(entity['word'])
        elif entity['entity_group'] == 'ORG':
            organizations.append(entity['word'])
        elif entity['entity_group'] == 'LOC':
            locations.append(entity['word'])
        elif entity['entity_group'] == 'MISC':
            miscellaneous.append(entity['word'])



    # Ensure the lists are of the same length
    max_length = max(len(persons), len(organizations), len(locations), len(miscellaneous))
    persons += [''] * (max_length - len(persons))
    organizations += [''] * (max_length - len(organizations))
    locations += [''] * (max_length - len(locations))
    miscellaneous += [''] * (max_length - len(miscellaneous))


    # Create a Pandas DataFrame
    data = {
        'Person': persons,
        'Organization': organizations,
        'Location': locations,
        'Miscellaneous': miscellaneous

    }
    df = pd.DataFrame(data)

    return df
#------------------------------------------------------------------------------------------------ IMAGE DOC OCR---------------------------------------------------------------------
def ocr_from_document():
    # Load image from the local folder
    image_path = "input.jpg"
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image")
        return

    # Convert the image to PIL format
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(pil_image)
    print(text)

    # Speak the extracted text
    speak("Extracting entities from text.")
    print("---------------------------------------------------------------------------------------------------------")
    df = extract_entities(text)
    print(df)
    print("---------------------------------------------------------------------------------------------------------")
    # Speak the extracted entities
    # for col in df.columns:
    #     for item in df[col]:
    #         if item:
    #             speak(f"{col}: {item}")


    for col in df.columns:
        speak(f"{col}")
        for item in df[col]:
            if item:
                speak(f"{item}")

    # Save as CSV and Excel
    df.to_csv("extracted_entities.csv", index=False)
    speak("Data saved as CSV file.")
    df.to_excel("extracted_entities.xlsx", index=False)
    speak("Data saved as Excel file.")

    # Close the image window
    cv2.destroyAllWindows()

#------------------------------------------------------------------------------------------------------------ OCR from Webcam--------------------------------------------------------
def ocr_from_webcam():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open webcam")
        return
    
    speak("Ready for OCR, press c to capture and q to quit")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    while True:
        # Capture frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is corrupt or missing
        if not ret or frame is None:
            print("Error: Corrupt or missing frame")
            continue

        # Display the captured frame
        cv2.imshow('Webcam', frame)

        # Check for keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            # Convert the captured frame to PIL format
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Perform OCR using pytesseract
            text = pytesseract.image_to_string(pil_image)
            print(text)
            print("--------------------------------------------------------------------------------------------------------------------------------")
            # Speak the extracted text
            speak("Extracting entities from text.")
            df = extract_entities(text)
            print("--------------------------------------------------------------------------------------------------------------------------------")
            # Speak the extracted entities
            # for col in df.columns:
            #     for item in df[col]:
            #         if item:
            #             speak(f"{col}: {item}")

            for col in df.columns:
                speak(f"{col}")
                for item in df[col]:
                    if item:
                        speak(f"{item}")

            # Save as CSV and Excel
            df.to_csv("extracted_entities.csv", index=False)
            speak("Data saved as CSV file.")
            df.to_excel("extracted_entities.xlsx", index=False)
            speak("Data saved as Excel file.")

            break  # Exit after processing and saving

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def take_command(microphone_index):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=microphone_index) as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't understand. Can you please repeat?")
        return "None"
    return query

def perform_task_2(query):
    command = None
    query = query.lower()  # Convert query to lowercase for case-insensitive matching
    
    if 'function one' in query or 'function 1'  in query:
        ocr_from_webcam()
    elif 'function two' in query or 'function 2'or 'function too'  or 'function to' in query:
        ocr_from_document()
    
    if command:
        # Send the command to Unity via UDP
        sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
        print(f"Sent command: {command}")

# Main function
def main():
    greet()
    
    # Set the microphone index based on user's selection
    microphone_index = 0 # Keep it at 2 when using the Logitech Camera.
    
    while True:
        query = take_command(microphone_index).lower()
        if 'exit' in query:
            speak("Goodbye!")
            break
        perform_task_2(query)

if __name__ == "__main__":
    main()