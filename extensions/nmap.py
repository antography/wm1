from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/nmap')
def nmap():
    return render_template('nmap.html')

