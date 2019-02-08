from flask import Flask, render_template, request

app = Flask(__name__)

# If not working
# windows (Run as Administrator)
    # pip install flask
# linux
    # sudo apt install python3-pip
    # pip3 install flask
# else
# In terminal
    # windows (Run as Administrator)
        # python app.py
    # linux or mac
        # python3 app.py

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# http://localhost:2000/get?name=lol&section=b
@app.route('/POST')
def get():
    name = request.args['name']
    sem = request.args['sem']
    return "Hello I'm <b>" + name + "</b> from <b>" + sem + "</b> sem"

app.run(port=2000)
