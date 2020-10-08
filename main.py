import appcode
import json
from bottle import route, static_file, run,  post



@route("/")
def htmlPage():
  return static_file("index.html", root = "")

@route("/frontend.js")
def frontEnd():
  return static_file("frontend.js", root = "")

@route("/pieChart") 
def pieChart():
  #print(dir(post))
  return json.dumps(appcode.pieChartdata())

@route("/table")
def table():
  return json.dumps(appcode.tableData())

@post("/POSTpieChart")
def postPiechart():
  return json.dumps(appcode.pieChartyearData())






run(host = "0.0.0.0", port = 8080, debug = True)