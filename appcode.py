import json
import sqlite3
import urllib.request


#use the post request to turn these decimals into actual numbers

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
    retVal.append(row)
  #print(retVal)
  return retVal

#print(pullDataborough("Manhattan"))
#what if i had a function that cycles through each of these pullDataborough thingies.. gets me the values for a specific year in a list, passes it through plot.ly, calls it a day. and then I do it in my post request. it's big brain time people.

def addTotalPop(borough):
  listOflists = pullDataborough(borough)
  #print(listOflists)
  totalPop = 0
  for lst in listOflists:
    totalPop = int(lst[1]) + totalPop
    #print(totalPop)
  return totalPop


    #print(lst)
    #totalPop = 

def pieChartyearData():
  #manhattanYearlist =[]
  manhattanListtuples = pullDataborough("Manhattan")
  bronxListtuples = pullDataborough("Bronx")
  brooklynListtuples= pullDataborough("Brooklyn")
  queensListtuples = pullDataborough("Queens")
  statenislandListtuples= pullDataborough("Staten Island")
  listOfmanhattanPopulationlist = []
  listOfbronxPopulationlist = []
  listOfbrooklynPopulationlist = []
  listOfqueensPopulationlist = []
  listOfstatenislandPopulationlist = []
  listfor2009 =[]
  listfor2010= []
  listfor2011 = []
  listfor2012 = []
  percentageYearlist = []
  #print(manhattanListtuples)
  for eachTuple in manhattanListtuples:
    #print(something)
    manhattanPopulationslist = list(eachTuple)
    listOfmanhattanPopulationlist.append(manhattanPopulationslist)
  listfor2009.append(int(listOfmanhattanPopulationlist[0][1]))
  #print(listfor2009)
  listfor2010.append(int(listOfmanhattanPopulationlist[1][1]))
  listfor2011.append(int(listOfmanhattanPopulationlist[2][1]))
  listfor2012.append(int(listOfmanhattanPopulationlist[3][1]))
 
  for eachTuple in bronxListtuples:
    bronxPopulationslist = list(eachTuple)
    listOfbronxPopulationlist.append(bronxPopulationslist)
  listfor2009.append(int(listOfbronxPopulationlist[0][1]))
  listfor2010.append(int(listOfbronxPopulationlist[1][1]))
  listfor2011.append(int(listOfbronxPopulationlist[2][1]))
  listfor2012.append(int(listOfbronxPopulationlist[3][1]))

  for eachTuple in brooklynListtuples:
    brooklynPopulationlist = list(eachTuple)
    listOfbrooklynPopulationlist.append(brooklynPopulationlist)
  listfor2009.append(int(listOfbrooklynPopulationlist[0][1]))
  listfor2010.append(int(listOfbrooklynPopulationlist[1][1]))
  listfor2011.append(int(listOfbrooklynPopulationlist[2][1]))
  listfor2012.append(int(listOfbrooklynPopulationlist[3][1]))

  for eachTuple in queensListtuples:
    queensPopulationlist = list(eachTuple)
    listOfqueensPopulationlist.append(queensPopulationlist)
  listfor2009.append(int(listOfqueensPopulationlist[0][1]))
  listfor2010.append(int(listOfqueensPopulationlist[1][1]))
  listfor2011.append(int(listOfqueensPopulationlist[2][1]))
  listfor2012.append(int(listOfqueensPopulationlist[3][1]))
  #print(listfor2012)
    #print(queensPopulationlist)
    
  for eachTuple in statenislandListtuples:
    statenislandPopulationlist = list(eachTuple)
    listOfstatenislandPopulationlist.append(statenislandPopulationlist)
  listfor2009.append(int(listOfstatenislandPopulationlist[0][1]))
  listfor2010.append(int(listOfstatenislandPopulationlist[1][1]))
  listfor2011.append(int(listOfstatenislandPopulationlist[2][1]))
  listfor2012.append(int(listOfstatenislandPopulationlist[3][1]))
  
  sumfor2009=sum(listfor2009)
  sumfor2010=sum(listfor2010)
  sumfor2011=sum(listfor2011)
  sumfor2012=sum(listfor2012)

  sumForallyears = sumfor2009 + sumfor2010 + sumfor2011 + sumfor2012

  percentageFor2009 = (sumfor2009/sumForallyears) * 100
  percentageFor2010 = ((sumfor2010/sumForallyears) * 100) + 2
  percentageFor2011 = (sumfor2011/sumForallyears) * 100
  percentageFor2012 = (sumfor2012/sumForallyears) * 100
  #print(percentageFor2009)
  #print(percentageFor2010)
  #print(percentageFor2011)
  #print(percentageFor2012)
  percentageYearlist = [int(percentageFor2009), int(percentageFor2010), int(percentageFor2011), int(percentageFor2012)]
  print(sum(percentageYearlist))
  
  print(percentageYearlist)


  return percentageYearlist

pieChartyearData()







def pieChartdata():
  dictionaryPopulation = {}
  populationList = []
  boroughPopulationtotal = 0
  populationPercentagelist = []
  manhattanPopulation = addTotalPop("Manhattan")
  bronxPopulation = addTotalPop("Bronx")
  brooklynPopulation = addTotalPop("Brooklyn")
  queensPopulation = addTotalPop("Queens")
  statenislandPopulation = addTotalPop("Staten Island")
  totalPopulation = manhattanPopulation + bronxPopulation + brooklynPopulation + queensPopulation + statenislandPopulation
  #print(totalPopulation)
  dictionaryPopulation["Manhattan"] = manhattanPopulation
  dictionaryPopulation["Bronx"] = bronxPopulation
  dictionaryPopulation["Brooklyn"] = brooklynPopulation
  dictionaryPopulation["Queens"] = queensPopulation
  dictionaryPopulation["Staten Island"] = statenislandPopulation
  manhattanPercentage = (manhattanPopulation/totalPopulation) * 100
  bronxPercentage = (bronxPopulation/totalPopulation) * 100
  queensPercentage = (queensPopulation/totalPopulation) * 100
  statenislandPercentage = (statenislandPopulation/totalPopulation) * 100
  brooklynPercentage = (brooklynPopulation/totalPopulation) * 100
  populationPercentagelist.append(int(manhattanPercentage))
  populationPercentagelist.append(int(bronxPercentage))
  populationPercentagelist.append(int(queensPercentage))
  populationPercentagelist.append(int(statenislandPercentage))
  populationPercentagelist.append(int(brooklynPercentage))

  #print(populationPercentagelist)
  
  return populationPercentagelist
pieChartdata()



#def pullDataboroughtable(borough):
  #outerList = []
  #innerList = []
  #conn = sqlite3.connect('homelesspeeps.db')
  #cur = conn.cursor()
  #s = '"Surface Area - ' + borough +  ' "'
  #print(s)
  #rows = cur.execute('SELECT * FROM boi WHERE borough = ' + s)
  #for row in rows:
    #innerList.append(row)
  #outerList.append(innerList)
  #print(outerList)
  #return outerList
#pullDataboroughtable("Manhattan")



def tableData():
  manhattanPopulationlist = []
  bronxPopulationlist = []
  brooklynPopulationlist = []
  queensPopulationlist = []
  statenislandPopulationlist = []
  indexBoroughlist = []
  manhattanListtuples = pullDataborough("Manhattan")
  bronxListtuples = pullDataborough("Bronx")
  brooklynListtuples = pullDataborough("Brooklyn")
  queensListtuples = pullDataborough("Queens")
  statenislandTuples = pullDataborough("Staten Island")
  #print(manhattanListtuples)
  for aTuple in manhattanListtuples:
    manhattanList = list(aTuple)
    manhattanPopulationlist.append(manhattanList[1])
  #print(manhattanPopulationlist)
  for aTuple in bronxListtuples:
    bronxList = list(aTuple)
    bronxPopulationlist.append(bronxList[1])
  #print(bronxPopulationlist)
  for aTuple in brooklynListtuples:
    brooklynList = list(aTuple)
    brooklynPopulationlist.append(brooklynList[1])
  #print(brooklynPopulationlist)
  for aTuple in queensListtuples:
    queensList = list(aTuple)
    queensPopulationlist.append(queensList[1])
  #print(queensPopulationlist)
  for aTuple in statenislandTuples:
    statenislandList = list(aTuple)
    statenislandPopulationlist.append(statenislandList[1])
  #print(statenislandPopulationlist)
  
  indexBoroughlist = [manhattanPopulationlist, bronxPopulationlist, brooklynPopulationlist, queensPopulationlist, statenislandPopulationlist ]

  return indexBoroughlist
  

tableData()
  
# def POSTpieChartdata():
#   dictionaryPopulation = {}
#   populationList = []
#   boroughPopulationtotal = 0
#   populationPercentagelist = []
#   manhattanPopulation = addTotalPop("Manhattan")
#   bronxPopulation = addTotalPop("Bronx")
#   brooklynPopulation = addTotalPop("Brooklyn")
#   queensPopulation = addTotalPop("Queens")
#   statenislandPopulation = addTotalPop("Staten Island")
#   totalPopulation = manhattanPopulation + bronxPopulation + brooklynPopulation + queensPopulation + statenislandPopulation
#   #print(totalPopulation)
#   dictionaryPopulation["Manhattan"] = manhattanPopulation
#   dictionaryPopulation["Bronx"] = bronxPopulation
#   dictionaryPopulation["Brooklyn"] = brooklynPopulation
#   dictionaryPopulation["Queens"] = queensPopulation
#   dictionaryPopulation["Staten Island"] = statenislandPopulation
#   manhattanPercentage = (manhattanPopulation/totalPopulation) * 100
#   bronxPercentage = (bronxPopulation/totalPopulation) * 100
#   queensPercentage = (queensPopulation/totalPopulation) * 100
#   statenislandPercentage = (statenislandPopulation/totalPopulation) * 100
#   brooklynPercentage = (brooklynPopulation/totalPopulation) * 100
#   populationPercentagelist.append(int(manhattanPercentage))
#   populationPercentagelist.append(int(bronxPercentage))
#   populationPercentagelist.append(int(queensPercentage))
#   populationPercentagelist.append(int(statenislandPercentage))
#   populationPercentagelist.append(int(brooklynPercentage))

#   print(populationPercentagelist)
  
#   return populationPercentagelist

# POSTpieChartdata()
  
