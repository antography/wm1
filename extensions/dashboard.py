from flask import session, redirect, url_for, render_template, request
from . import main
import json

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

