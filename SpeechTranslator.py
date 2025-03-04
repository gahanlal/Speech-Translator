from flask import Flask, render_template, request
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

LANGUAGES = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bn': 'Bengali', 'bg': 'Bulgarian', 'ca': 'Catalan', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
    'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'he': 'Hebrew',
    'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
    'kn': 'Kannada', 'ko': 'Korean', 'lv': 'Latvian', 'lt': 'Lithuanian', 'ms': 'Malay', 'ml': 'Malayalam', 'mr': 'Marathi',
    'ne': 'Nepali', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian',
    'sr': 'Serbian', 'sk': 'Slovak', 'sl': 'Slovenian', 'es': 'Spanish', 'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'cy': 'Welsh'
}

def recognize_speech(language_code):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language=language_code)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def translate_text(text, src_language, dest_language):
    try:
        translator = GoogleTranslator(source=src_language, target=dest_language)
        return translator.translate(text)
    except Exception as e:
        return f"Error during translation: {e}"

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    lang1 = request.form.get('lang1')
    lang2 = request.form.get('lang2')

    return render_template('translate.html', lang1=LANGUAGES[lang1], lang2=LANGUAGES[lang2], lang1_code=lang1, lang2_code=lang2)

@app.route('/speech', methods=['POST'])
def speech():
    lang1 = request.form.get('lang1')
    lang2 = request.form.get('lang2')

    # User 1 speaks
    text1 = recognize_speech(lang1)
    translated_text1 = translate_text(text1, src_language=lang1, dest_language=lang2)

    # User 2 speaks
    text2 = recognize_speech(lang2)
    translated_text2 = translate_text(text2, src_language=lang2, dest_language=lang1)

    # Return the conversation data
    return {
        "person1_said": text1,
        "person1_translated": translated_text1,
        "person2_said": text2,
        "person2_translated": translated_text2
    }



if __name__ == "__main__":
    app.run(debug=True)
