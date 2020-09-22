from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["fd"] = None
app.config["child_pid"] = None
app.config["cmd"] = 'sh'
app.config["nmap_child"] = None

socketio = SocketIO(app)

from paths import main as modules
app.register_blueprint(modules, url_prefix='/module')

@app.route('/')
def index():
    return render_template('index.html')

# import all the websocket files
from sockets.wm1core import *
from sockets.terminal import *
from sockets.nmap import *

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5050)