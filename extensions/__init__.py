from flask import Blueprint

main = Blueprint('main', __name__ )

from . import proxy, dashboard, extmanager, settings, nmap, terminal, credits