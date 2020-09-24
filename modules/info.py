from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/credits')
def credits():
    return render_template('/custom/credits.html')

@main.route('/roadmap')
def roadmap():
    return render_template('/custom/roadmap.html')

