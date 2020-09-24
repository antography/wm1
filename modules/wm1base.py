from flask import session, redirect, url_for, render_template, request, Response
import json, os
import lxml.etree

from . import main

@main.route('/terminal')
def terminal():
    return render_template('/base/terminal.html')

@main.route('/rshell')
def rshell():
    return render_template('/base/rshell.html')

@main.route('/nmap/getdashrender/<workspace>')
def nmapgetscans(workspace):
    workspace = workspace
    wksp = "./workspace/" + workspace+"/manifest.xml"
    tree = lxml.etree.parse(wksp)
    parent = tree.xpath("//workspace/nmap/*")
    res = []
    for scan in parent:
        reqitem = "workspace/" + workspace + "/nmap/" + scan.text
        if not os.path.isfile(reqitem):
            return "File not found"
        fp = open(reqitem, 'r')
        lines = fp.read().replace('\n', '<br />')
        fp.close()
        out = '<article class=\"message\"><div class=\"message-header section-toggle\" onclick="toggleview(\'' \
            + scan.text+ '-toggle\')\"><p>' \
            + scan.text+'<p></div><div class=\"message-body\"  style=\"display: none;\" id=\"' \
            + scan.text+'-toggle\">'\
            + lines +'</div></article>'
        res.append(str(out))
    return Response(res, mimetype = "text/plain")

@main.route('/nmap')
def nmap():
    return render_template('/base/nmap.html')

