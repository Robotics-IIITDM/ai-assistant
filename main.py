from flask import Flask, render_template, request
from RealtimeSTT import AudioToTextRecorder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('startrecording.html')

@app.route('/recording', methods=['GET', 'POST'])
def recording():
    recorder = AudioToTextRecorder(language='en')

    result = {"text": ""}

    def process_text(text):
        result["text"] = text
        recorder.stop()  
    recorder.text(process_text)
    return render_template('stoprecording.html', text=result["text"])

if __name__ == '__main__':
    app.run(debug=True)
