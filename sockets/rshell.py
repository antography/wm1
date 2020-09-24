from wm1 import socketio, app

def read_and_forward():
	while True:
		socketio.sleep(.01)
		if app.revshell["status"] == "connected":
			try:
				data = app.revshell["client"].recv(1024)
				socketio.emit("rshell-update", {"status": "connected", "data": data.decode("utf-8") })
			except:
				socketio.emit("rshell-update", {"status": "connected", "data": ""})
				pass
		else:
			socketio.emit("rshell-update", {"status": "disconnected"})

@socketio.on("use_rvshell")
def use_rvshell():
	socketio.start_background_task(target=read_and_forward)

@socketio.on("rshell-input")
def rshell_input(input):
	if app.revshell["status"] == "connected":
		try:
			app.revshell["client"].send(input.encode())
		except: pass
