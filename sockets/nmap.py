import pty, os, subprocess, select, termios, struct, fcntl, shlex
import uuid
from wm1 import socketio, app

@socketio.on("nmapcall", namespace="/nmap")
def nmapcall(data):
  if app.config["nmap_child"]:
    socketio.send("nmap already running", namespace="/notify")
    return
  host = data['host']
  args = data['args'].split(' ')
  workspace = data['workspace']
  if not host:
    socketio.send("no host set", namespace="/notify")
    return
  final = ['nmap'] + args + [host]
  
  with subprocess.Popen(final,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE,
          bufsize=1,
          universal_newlines=True) as process:
    app.config["nmap_child"] = process.pid
    nmapofname = str(uuid.uuid4().hex)+ "-" + str(process.pid) +".nmap"
    nmapoutfile = open("/data/Projects/wm1/workspace/"+workspace+"/nmap/temp/" + str(nmapofname), "a")

    for line in process.stdout:
        line = line.rstrip()
        socketio.emit("nmapout", {"output": line}, namespace="/nmap")
        nmapoutfile.write(line + "\n")
        if "Nmap done:" in line:
            app.config["nmap_child"] = None
            socketio.send("nmap done", namespace="/notify")
    socketio.emit("nmapfname",nmapofname, namespace="/nmap")
    socketio.send("File written to: " + nmapofname, namespace="/notify")
    nmapoutfile.close()
            