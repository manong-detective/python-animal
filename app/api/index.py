from os.path import dirname, abspath

from flask import render_template, Flask


dir = dirname(abspath(__file__))

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


