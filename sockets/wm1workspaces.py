
from wm1 import socketio, app

@socketio.on("setwksp", namespace="/wscommand")
def setwksp(data):
  print(data)
  
  socketio.send(data, namespace = "/notify")