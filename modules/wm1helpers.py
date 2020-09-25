from flask import session, redirect, url_for, render_template, request, send_file, Blueprint, Response
import json, os
import lxml.etree

helper = Blueprint('helpers', __name__ )

# Outputs json for compatability reasons
@helper.route('/getext')
def getext():
    exts = "./extensions.xml"
    tree = lxml.etree.parse(exts)
    parent = tree.xpath("//module")
    res = {}
    for module in parent:
        res[module[0].text]= {
            'template': module[1].text,
            'blueprint': module[2].text,
            'path': module[3].text,
            'preload': module[4].text,
            'startpage': module[5].text,
            'disabled': module[6].text
        }
    return res

@helper.route('/getwkspmods/<workspace>')
def getwksp(workspace):
    wksp = "./workspace/" + workspace+"/manifest.xml"
    tree = lxml.etree.parse(wksp)
    parent = tree.xpath("//workspace/*")
    res = []
    for i in parent:
        res.append(i.tag)
    return Response(','.join(res), mimetype = "text/plain")

@helper.route('/getworkspaces')
def getworkspaces():
    wksp = "./workspace/workspaces.xml"
    tree = lxml.etree.parse(wksp)
    parent = tree.xpath("//name")
    res = []
    for i in parent:
        res.append(i.text)
    return Response(','.join(res), mimetype = "text/plain")

@helper.route('/getactwksp')
def getactwksp():
  wksp = "./workspace/workspaces.xml"
  tree = lxml.etree.parse(wksp)
  parent = tree.xpath(".//active[text()='true']/..")

  wkspname = str(parent[0][0].text)
  return wkspname
