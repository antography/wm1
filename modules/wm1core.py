from flask import session, redirect, url_for, render_template, request, send_file
import json, os

from . import main

@main.route('/dashboard')
def dashboard():
    return render_template('/core/dashboard.html')

@main.route('/extmanager')
def extmanager():
    return render_template('/core/extmanager.html')

@main.route('/settings')
def settings():
    return render_template('/core/settings.html')
