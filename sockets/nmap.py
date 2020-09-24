import pty, os, subprocess, select, termios, struct, fcntl, shlex
import uuid, shutil, lxml.etree
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
    nmapoutfile = open("./workspace/"+workspace+"/temp/" + str(nmapofname), "a")

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

@socketio.on("nmapsave", namespace="/nmap")
def nmapsave(data):
  reqfile = "workspace/" + data['workspace'] + "/temp/" + data['file']
  destfile = "workspace/" + data['workspace'] + "/nmap/" + data['file']
  if not os.path.isfile(reqfile):
    socketio.send("Requested Save on unknown file.", namespace="/notify")
    return

  shutil.move(reqfile, destfile)
  manifest = "./workspace/" +  data['workspace'] + "/manifest.xml"
  tree = lxml.etree.parse(manifest)
  parent = tree.xpath(".//nmap")
  lxml.etree.SubElement(parent[0], 'scan').text = data['file']

  # this has a filthy output. xml beautification is required to make the manifest readable
  tree.write(manifest, pretty_print=True, xml_declaration=True, encoding="utf-8")
  socketio.send("File saved to workspace", namespace="/notify")

@socketio.on("nmapdel", namespace="/nmap")
def nmapdel(data):
  reqfile = "workspace/" + data['workspace'] + "/temp/" + data['file']
  if not os.path.isfile(reqfile):
    socketio.send("Requested Delete on unknown file.", namespace="/notify")
    return
  os.remove(reqfile) 
  socketio.send("File removed", namespace="/notify")