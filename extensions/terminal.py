from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/terminal')
def termianl():
    return render_template('terminal.html')

