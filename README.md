OCR and Named Entity Recognition (NER) Project
This project combines Optical Character Recognition (OCR) and Named Entity Recognition (NER) to extract text from images or webcam captures and identify entities such as persons, organizations, locations, and miscellaneous items. The extracted entities are saved as CSV and Excel files, and the text can also be sent to Unity for further processing.

Table of Contents
Features
Requirements
Installation
Usage
Running the Project
Functions
Project Structure
Acknowledgments
Features
Extract text from images using OCR with Tesseract.
Perform Named Entity Recognition (NER) on the extracted text using a pre-trained model.
Save the extracted entities as CSV and Excel files.
Integrate with Unity to send the OCR text for further processing.
Voice interaction for command inputs and reading results using text-to-speech.
Requirements
Python 3.6+
OpenCV
PyTesseract
PIL (Pillow)
Pyttsx3
SpeechRecognition
Transformers (Hugging Face)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ocr-ner-project.git
cd ocr-ner-project
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download and install Tesseract OCR from here and ensure it's added to your system path.

Usage
Running the Project
Ensure you have a compatible microphone and webcam connected.
Place an image named input.jpg in the project directory for the document OCR function.
Run the main script:
bash
Copy code
python main.py
Functions
Function 1: OCR from Webcam

Captures an image from the webcam and performs OCR to extract text.
Performs NER on the extracted text and saves the entities as CSV and Excel files.
Function 2: OCR from Document

Loads an image from the project directory and performs OCR to extract text.
Performs NER on the extracted text and saves the entities as CSV and Excel files.
Voice Commands
The application will greet you and ask for a command.
Say "Function one" or "Function 1" to use OCR from the webcam.
Say "Function two" or "Function 2" to use OCR from a document image.
Say "Exit" to terminate the application.
Project Structure
plaintext
Copy code
ocr-ner-project/
├── main.py                  # Main script to run the project
├── requirements.txt         # Python dependencies
├── ner_model/               # Directory containing the NER model files
├── input.jpg                # Sample input image for document OCR
├── extracted_entities.csv   # Output CSV file with extracted entities
├── extracted_entities.xlsx  # Output Excel file with extracted entities
Acknowledgments
Tesseract OCR
Hugging Face Transformers
OpenCV
PyTesseract
Pillow (PIL)
Pyttsx3
SpeechRecognition
Feel free to contribute to this project by submitting issues or pull requests. For any queries, contact your-email@example.com
