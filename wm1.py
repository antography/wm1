from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, send, emit
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!2'
app.config["workspace"] = None
app.config["fd"] = None
app.config["child_pid"] = None
app.config["cmd"] = 'bash'
app.config["nmap_child"] = None
app.config["revshell_port"] = 7777

socketio = SocketIO(app)

from modules import main as extensions
from modules.wm1helpers import helper
app.register_blueprint(extensions, url_prefix='/module')
app.register_blueprint(helper, url_prefix='/helper')

@app.route('/')
def index():
    return render_template('index.html')

# import all the websocket files
from sockets.wm1core import *
from sockets.wm1workspaces import *
from sockets.terminal import *
from sockets.nmap import *
from sockets.rshell import *

import revshell

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5050)
