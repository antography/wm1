import pty
import os
import subprocess
import select
import termios
import struct
import fcntl
import shlex
from wm1 import socketio, app

@socketio.on("nmapcall", namespace="/nmap")
def nmapcall(data):
 
  if app.config["nmap_child"]:
    socketio.send("map already running", namespace="/nmap")
    return
  host = data['host']
  args = data['args'].split(' ')

  if not host:
    socketio.send("no host set", namespace="/nmap")
    return
  final = ['nmap'] + args + [host]

  print(final)
  with subprocess.Popen(final,
                          stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          bufsize=1,
                          universal_newlines=True) as process:
    app.config["nmap_child"] = process.pid
    print(app.config['nmap_child'])
    for line in process.stdout:
        line = line.rstrip()
        socketio.emit("nmapout", {"output": line}, namespace="/nmap")