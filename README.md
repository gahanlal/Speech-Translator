Speech Translator App

Overview

The Speech Translator App is a real-time web application built with Flask. It leverages speech recognition to capture spoken input, translates the text between two selected languages using the Google Translator API (via the deep_translator library), and integrates text-to-speech functionality using gTTS. This project is ideal for enabling multi-lingual communication in a user-friendly interface.

Features

Real-time Speech Recognition: Capture audio input directly from your microphone.

Language Translation: Translate spoken words between two languages.

Text-to-Speech: (Planned Enhancement) Convert translated text into spoken words.

User-Friendly Interface: Simple web interface built using Flask and HTML templates.

Multi-Language Support: Choose from a wide range of languages.

Technologies Used
Flask
SpeechRecognition
deep_translator
gTTS

Installation

Clone the repository:

bash
Copy
Edit
git clone https://github.com/gahanlal/speech-translator-app.git
cd speech-translator-app

Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  

# On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, install the packages manually:

bash
Copy
Edit
pip install Flask SpeechRecognition deep_translator gTTS
Usage
Run the Flask Application:

bash
Copy
Edit
python app.py
Open Your Browser:

Navigate to http://127.0.0.1:5000/ to access the app.

Select Languages:

On the home page, choose the source and target languages from the provided dropdown menus.

Start the Conversation:

Click the appropriate buttons to initiate speech recognition.
The app will capture your speech, translate it into the selected target language, and display both the original and translated text.
Project Structure
pgsql
Copy
Edit
speech-translator-app/
├── app.py
├── templates/
│   ├── index.html
│   └── translate.html
├── requirements.txt
└── README.md

Future Enhancements
Text-to-Speech Integration: Extend the application to use gTTS for converting translated text into audio.
Improved Error Handling: Enhance error messages and gracefully manage exceptions.
User Interface Improvements: Upgrade the design and functionality of the UI.
Deployment: Provide deployment instructions for cloud platforms like Heroku or AWS.


Acknowledgements
Thanks to the developers and communities behind Flask, SpeechRecognition, deep_translator, and gTTS for their invaluable contributions.

