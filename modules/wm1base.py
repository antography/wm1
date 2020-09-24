from flask import session, redirect, url_for, render_template, request
import json

from . import main

@main.route('/terminal')
def termianl():
    return render_template('/base/terminal.html')

@main.route('/nmap')
def nmap():
    return render_template('/base/nmap.html')