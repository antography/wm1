from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, send, emit
import pty
import os
import subprocess
import select
import termios
import struct
import fcntl
import shlex
import json, psutil

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["fd"] = None
app.config["child_pid"] = None
app.config["cmd"] = 'sh'
socketio = SocketIO(app)

from paths import main as modules
app.register_blueprint(modules, url_prefix='/module')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('getusg')
def getusg():
  cpuusg = psutil.cpu_percent()
  memusg = psutil.virtual_memory().percent
  emit('getusg', {
    'cpuusage' : cpuusg,
    'memusage' : memusg
  })

from sockets.terminal import *


# I dont know why this is here. clean this up unless there are plans for taking arguments
def main():
    socketio.run(app, host='0.0.0.0', port=5050)
if __name__ == '__main__':
    main()