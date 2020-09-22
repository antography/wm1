import json, psutil
from wm1 import socketio, app

@socketio.on('getusg')
def getusg():
  cpuusg = psutil.cpu_percent()
  memusg = psutil.virtual_memory().percent
  socketio.emit('getusg', {
    'cpuusage' : cpuusg,
    'memusage' : memusg
  })
