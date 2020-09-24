from flask import session, redirect, url_for, render_template, request, send_file, Blueprint
import json, os
import lxml.etree

helper = Blueprint('helpers', __name__ )

extensionsconfig = open('./extensions.json')
extensions = json.load(extensionsconfig)

@helper.route('/getext')
def getext():
    return extensions

@helper.route('/getwksp')
def getwksp(workspace, item):
    workspaces = json.load(open('./workspaces.json'))
    return workspaces

@helper.route('/getactwksp')
def getactwksp():
  wksp = "./workspace/workspaces.xml"
  tree = lxml.etree.parse(wksp)
  parent = tree.xpath(".//active[text()='true']/..")

  wkspname = str(parent[0][0].text)
  return wkspname

@helper.route('/getwkspitem/<workspace>/<module>/<item>')
def getwkspitem(workspace,module, item):
    reqitem = "workspace/" + workspace + "/" + module + "/" + item
    if os.path.isfile(reqitem):
        return send_file(reqitem)
    else:
        return "fail"