from flask import Flask, request, jsonify, render_template
import pyttsx3
import os  
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("groceries_form.html")

@app.route('/button-click', methods=['POST'])
def text_to_speech():
    html_file_path = os.path.join("templates", "groceries_form.html") 
    with open(html_file_path, "r", encoding='utf-8') as file:
    # with open(html_file_path, 'r', encoding='utf-8') as file:
        # text = file.read()
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()
        # print(text)
        speak(text)
    

# Converting text to audio
def speak(audio_inp):
    c = pyttsx3.init()
    newVoiceRate = 145
    c.setProperty('rate', newVoiceRate)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM"
    c.setProperty('voice', voice_id)
    c.runAndWait()
    c.say(audio_inp)
    c.runAndWait()

if __name__ == '__main__':
        app.run(debug=True)
