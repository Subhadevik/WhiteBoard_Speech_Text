from flask import Flask, render_template, request, jsonify
import whisper
import os
import tempfile

app = Flask(__name__)
model = whisper.load_model("small")  # You can also try 'small'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        audio_path = temp_audio.name
        audio_file.save(audio_path)

    try:
        result = model.transcribe(audio_path)
        text = result['text']
    except Exception as e:
        text = f"Error: {e}"

    os.remove(audio_path)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
