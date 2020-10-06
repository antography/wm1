from flask import session, redirect, url_for, render_template, request, send_file
import json, os
import lxml.etree

from . import main

def getexts(inp):
    res = {}
    for module in inp:
        res[module[0].text]= {
            'name': module[0].text,
            'template': module[1].text,
            'blueprint': module[2].text,
            'path': module[3].text,
            'preload': module[4].text,
            'startpage': module[5].text,
            'disabled': module[6].text,
            'placeholder':module[7].text,
            'socket':module[8].text,
            'folder':module[9].text,
            'manifest':module[10].text,
            'class':module[11].text,
            'title': module[12].text,
            'onclick':module[13].text
        }
    return res

@main.route('/dashboard')
def dashboard():
    return render_template('/core/dashboard.html')

@main.route('/extmanager')
def extmanager():
    tree = lxml.etree.parse("./extensions.xml")

    wm1core = tree.xpath(".//class[text()='core']/..")
    wm1base = tree.xpath(".//class[text()='base']/..")
    wm1custom = tree.xpath(".//class[text()='custom']/..")
    wm1other = tree.xpath(".//class[text()='other']/..")

    rescore = getexts(wm1core)
    resbase = getexts(wm1base)
    rescustom = getexts(wm1custom)
    resother = getexts(wm1other)
    
    return render_template('/core/extmanager.html', wm1core=rescore, wm1base= resbase, wm1custom=rescustom, wm1other=resother)

@main.route('/settings')
def settings():
    return render_template('/core/settings.html')
