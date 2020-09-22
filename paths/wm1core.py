from flask import session, redirect, url_for, render_template, request
import json

from . import main

extensionsconfig = open('./extensions.json')
extensions = json.load(extensionsconfig)

@main.route('/getext')
def getext():
    return extensions

@main.route('/dashboard')
def dashboard():
    return render_template('/core/dashboard.html')

@main.route('/terminal')
def termianl():
    return render_template('/base/terminal.html')

@main.route('/extmanager')
def extmanager():
    return render_template('/core/extmanager.html')

@main.route('/settings')
def settings():
    return render_template('/core/settings.html')
