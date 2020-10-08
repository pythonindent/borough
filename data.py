import json
import sqlite3
import urllib.request
#import pandas as pd

#def x(q,con):
  #a = pd.read_sql_query(q,con)
  #con.close()
  #return a



def loadData():
  conn = sqlite3.connect('homelesspeeps.db')
  cur = conn.cursor()
  uri = "https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.json?accessType=DOWNLOAD"
  response = urllib.request.urlopen(uri)
  content_string = response.read().decode()
  content = json.loads(content_string)
  cur.execute('CREATE TABLE IF NOT EXISTS boi(borough TEXT, population TEXT, year TEXT)')
  #print(3)
  #print(content)
  #print(content["data"])
  for aLst in content["data"]:
    #print(aLst)
    #print(len(content["data"]))
    cur.execute('INSERT INTO boi(borough, population, year) VALUES(?,?,?)' ,(aLst[9], aLst[10], aLst[8]))
    #print(aLst[9], aLst[10], aLst[8])
  conn.commit()
  conn.close()
#loadData()

def pullDataborough(borough):
  retVal = []
  conn = sqlite3.connect('homelesspeeps.db')
  cur = conn.cursor()
  s = '"Surface Area - ' + borough +  ' "'
  #print(s)
  rows = cur.execute('SELECT * FROM boi WHERE borough = ' + s)
  for row in rows:
    #print(row)
    retVal.append(row)
  #print(retVal)
  return retVal

def addTotalPop(borough):
  listOflists = pullDataborough(borough)
  #print(listOflists)
  totalPop = 0
  for lst in listOflists:
    totalPop = int(lst[1]) + totalPop
  return totalPop




def pieChartdata():
  retVal = {}
  manhattanPopulation = addTotalPop("Manhattan")
  bronxPopulation = addTotalPop("Bronx")
  brooklynPopulation = addTotalPop("Brooklyn")
  queensPopulation = addTotalPop("Queens")
  statenislandPopulation = addTotalPop("Staten Island")
  retVal["Manhattan"] = manhattanPopulation
  retVal["Bronx"] = bronxPopulation
  retVal["Brooklyn"] = brooklynPopulation
  retVal["Queens"] = queensPopulation
  retVal["Staten Island"] = statenislandPopulation

  print(retVal)
  return retVal


pieChartdata()

def tableData():
  manhattanPopulation = addTotalPop("Manhattan")
  pass
  #print(manhattanPopulation)
  
tableData()
  


#def manhattanListvalues():
  #retVal = []
  #conn = sqlite3.connect('homelesspeeps.db')
  #cur = conn.cursor()
  #rows = cur.execute('SELECT * FROM boi')
  #for row in rows:
    #if row[0] = "Surface Area- Manhattan":
    #print(row[0])
#manhattanListvalues()

  #print(retVal)

#def makeBoroughdictionary():

pullDataborough("Manhattan")
pullDataborough("Bronx")
pullDataborough("Brooklyn")
pullDataborough("Queens")
pullDataborough("Staten Island")

  
    #AJAXgetrequests use the database function

    #cur.execute('SELECT * FROM boi')

#print(x('SELECT * FROM boi', sqlite3.connect('homelesspeeps.db')))

  #if not os.path.isfile(csvFile):
       #params = urllib.parse.urlencode({"$limit":howMany})
       #uri = "https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.json?accessType=DOWNLOAD" #% params
       #writeDataToCSVFile(csvFile,content,['apno','aptype','issued', 'value'],True)
       #cur.execute( \  'CREATE TABLE IF NOT EXISTS ' + \'movies (title,year)')
       






  #print(6)
  #print(pythonHomelessdata)
  #print(3)
  #print(pythonHomelessdata["data"])
  #for lst in pythonHomelessdata:
    #print(lst)
    #lst["data"]
  #print(2)

#dataProcessing("homelessPeeps.json")
#with open("homelessPeeps.json", "r") as f:
  #print(f.read())

#def getPieData(listOflists):
  #retVal = {}
  #dataLists = listOflists["data"]
  #print(data)
  #for lst in dataLists:
    #print(lst[9])
    #manhattenPopulation = 0
    #bronxPopulation = 0
    #brooklynPopulation = 0
    #queensPopulation=0
    #statenislandPopulation = 0
    #if lst[9] == "Surface Area- Manhatten":
      #manhattenPopulation = manhattenPopulation + lst[10]
      #print(manhattenPopulation)
      #retVal["manhattenPopulation"] = manhattenPopulation
      #print(retVal)
    



      


    
    #print(lst)
    #print(lst[9])
    #print(lst[10])
  #we want to add each homeless estimate for the surface area of Manhatten
  #we want to add each homeless estimate for the surface area of Bronx 
  #we want to add each homeless estimate for the surface area of Brooklyn 
  #we want to add each homeless estimate for the surface area of Queens 
  #we want to add each homeless estimate for the surface area of Queens 

  #print(data)
  
  #for lst in listOflists:
    #if lst.contain 


#def dataProcessing():
  #with open("homelessPeeps.json", "r") as f:
    #pythonHomelessdata = json.loads(f.read())
    #print(pythonHomelessdata)
    #for i in pythonHomelessdata.keys():
      #print(i)
    #getPieData(pythonHomelessdata)

#dataProcessing()