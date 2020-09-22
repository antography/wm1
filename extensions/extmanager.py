from flask import session, redirect, url_for, render_template, request
from . import main
import json

extensionsconfig = open('./extensions.json')
extensions = json.load(extensionsconfig)

@main.route('/extmanager')
def extmanager():
    return render_template('extmanager.html')

