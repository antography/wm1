from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/proxy')
def proxy():
    return render_template('proxy.html')

