from flask import Flask, render_template, request
from RealtimeSTT import AudioToTextRecorder
import ollama
client=ollama.Client()
model="llama3.2:1b"


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('startrecording.html')

@app.route('/recording', methods=['GET', 'POST'])
def recording():
    recorder = AudioToTextRecorder(language='en')

    result = {"text": ""}

    def process_text(text):
        response_text = client.generate(model=model, prompt=text)
        result["text"] = response_text
        recorder.stop()  
    recorder.text(process_text)
    return render_template('stoprecording.html', text=result["text"])

if __name__ == '__main__':
    app.run(debug=True)
