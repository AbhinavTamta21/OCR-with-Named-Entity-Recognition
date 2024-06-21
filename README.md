# OCR and Named Entity Recognition (NER) Project

This project combines Optical Character Recognition (OCR) and Named Entity Recognition (NER) to extract text from images or webcam captures and identify entities such as persons, organizations, locations, and miscellaneous items. The extracted entities are saved as CSV and Excel files, and the text can also be sent to Unity for further processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Project](#running-the-project)
  - [Functions](#functions)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Features

- Extract text from images using OCR with Tesseract.
- Perform Named Entity Recognition (NER) on the extracted text using a pre-trained model.
- Save the extracted entities as CSV and Excel files.
- Integrate with Unity to send the OCR text for further processing.
- Voice interaction for command inputs and reading results using text-to-speech.

## Requirements

- Python 3.6+
- OpenCV
- PyTesseract
- PIL (Pillow)
- Pyttsx3
- SpeechRecognition
- Transformers (Hugging Face)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ocr-ner-project.git
    cd ocr-ner-project
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract) and ensure it's added to your system path. Download the NER model from Hugging Face

## Usage

### Running the Project

1. Ensure you have a compatible microphone and webcam connected.
2. Place an image named `input.jpg` in the project directory for the document OCR function.
3. Run the main script:
    ```bash
    python main.py
    ```

### Functions

- **Function 1: OCR from Webcam**
  - Captures an image from the webcam and performs OCR to extract text.
  - Performs NER on the extracted text and saves the entities as CSV and Excel files.

- **Function 2: OCR from Document**
  - Loads an image from the project directory and performs OCR to extract text.
  - Performs NER on the extracted text and saves the entities as CSV and Excel files.

### Voice Commands

- The application will greet you and ask for a command.
- Say "Function one" or "Function 1" to use OCR from the webcam.
- Say "Function two" or "Function 2" to use OCR from a document image.
- Say "Exit" to terminate the application.

### Acknowledgments
- Tesseract OCR
- Hugging Face Transformers
- OpenCV
- PyTesseract
- Pillow (PIL)
- Pyttsx3
- SpeechRecognition

Feel free to contribute to this project by submitting issues or pull requests. 
