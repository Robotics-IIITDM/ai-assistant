from flask import *

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('startrecording.html')

@app.route('/recording', methods=['POST','GET'])
def recording():
    return render_template('stoprecording.html')

if __name__ == '__main__':
    app.run(debug=True)