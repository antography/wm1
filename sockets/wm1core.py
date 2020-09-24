import json, psutil, socket
from wm1 import socketio, app

lastdata = None

#Serves as an event loop
@socketio.on('update')
def update():
  global lastdata
  cpuusg = psutil.cpu_percent()
  memusg = psutil.virtual_memory().percent

  #If the revshell is connected, check if it's still
  if app.revshell["status"] == "connected":
    try:
      data = app.revshell["client"].recv(1024, socket.MSG_PEEK)
      if len(data) == 0 or lastdata == data:
        app.revshell["status"] = "disconnected"
        app.revshell["client"] = None
      else: lastdata = data
    except: pass
  
  #Try to connect the revshell
  else:
    try:
      client, _ = app.revshell["sock"].accept()
      client.setblocking(0)
      print("received revshell conn")
      app.revshell["status"] = "connected"
      app.revshell["client"] = client
    except: pass

  socketio.emit('update', {
    'cpuusage' : cpuusg,
    'memusage' : memusg,
    'revshell' : {
      'status': app.revshell["status"]
    }
  })
