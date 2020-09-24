from flask import session, redirect, url_for, render_template, request, send_file, Blueprint, Response
import json, os
import lxml.etree

helper = Blueprint('helpers', __name__ )

extensionsconfig = open('./extensions.json')
extensions = json.load(extensionsconfig)

@helper.route('/getext')
def getext():
    return extensions

@helper.route('/getwkspmods/<workspace>')
def getwksp(workspace):
    wksp = "./workspace/" + workspace+"/manifest.xml"
    tree = lxml.etree.parse(wksp)
    parent = tree.xpath("//workspace/*")
    res = []
    for i in parent:
        res.append(i.tag)
    return Response(','.join(res), mimetype = "text/plain")

@helper.route('/getactwksp')
def getactwksp():
  wksp = "./workspace/workspaces.xml"
  tree = lxml.etree.parse(wksp)
  parent = tree.xpath(".//active[text()='true']/..")

  wkspname = str(parent[0][0].text)
  return wkspname
