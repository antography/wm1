import socket, asyncio
from wm1 import app

revshell = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#revshell.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
revshell.bind(("0.0.0.0", app.config["revshell_port"]))
revshell.setblocking(0)
revshell.listen(1)

app.revshell = {
	"status": "disconnected",
	"sock": revshell,
	"client": None
}
