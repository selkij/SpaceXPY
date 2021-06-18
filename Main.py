from os import system

#install 'requests' library to get SpaceX unofficial API
system('pip install requests')

#import required libraries
from requests import get
import json
import time

#Put capsules data on a .json file
def dumpCapsulesData():   
    r = get("https://api.spacexdata.com/v4/capsules")
    with open('capsules.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)

#Get capsules.json file content
def loadCapsulesData():
    #Return capsules.json content
    return dict(json.load(open('capsules.json', 'r')))['value']

#Put rockets data on a .json file
def dumpRocketsData():   
    r = get("https://api.spacexdata.com/v4/rockets")
    with open('rockets.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)

#Get rockets.json file content
def loadRocketsData():
    #Return rockets.json content
    return dict(json.load(open('rockets.json', 'r')))['value']

#Load rockets' data and print results
def loadDumpRocketsData():
    dumpRocketsData()
    data = loadRocketsData()

    fstr = 'Rockets informations:\n\n'
    #for each information in 'data' add to fstr
    for d in data:
        launcher = d
        h = launcher['height']['meters']
        fstr += 'meters: \n\n' + str(h) + '\n'
    
    #Print result
    print(fstr)

#Load capsules' data and print results
def loadDumpCapsulesData():
    dumpCapsulesData()
    data = loadCapsulesData()

    fstr = 'Capsules informations:\n\n'
    #for each information in 'data' add to fstr
    for x in data:
        fstr += '{0[serial]}: reused {0[reuse_count]} times, landed on water {0[water_landings]} times, landed on land {0[land_landings]} times, landed  {1} times in total, status : {0[status]}, type of capsule : {0[type]}, id : {0[id]}\n'.format(x, x['land_landings'] + x['water_landings'])
    
    #Print results
    print(fstr)

#Put company's data on a .json file
def dumpCompanyData():   
    r = get("https://api.spacexdata.com/v4/company")
    with open('company.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)

#Get company.json data
def loadCompanyData():
    #Return company.json content
    return dict(json.load(open('company.json', 'r')))['value']

#Load company's data and print results
def loadDumpCompanyData():
    dumpCompanyData()
    data = loadCompanyData()

    fstr = 'SpaceX informations:\n\n'
    fstr += 'Company name: {0[name]}\n SpaceX founder: {0[founder]}\n Founded in: {0[founded]}\n CEO: {0[ceo]}\n CTO: {0[cto]}\n COO: {0[coo]}\n Propulsion of CTO: {0[cto_propulsion]}\n Number of employees in SpaceX: {0[employees]}\n Value of SpaceX: {0[valuation]}\n Number of vehicles: {0[vehicles]}\n Number of launch sites: {0[launch_sites]}\n Number of test sites: {0[test_sites]}\n Description of SpaceX: {0[summary]}'.format(data)
    
    #Print results
    print(fstr)


print("Powered by SpaceX api https://github.com/r-spacex/SpaceX-API\n")
print("   _____                     __   _________     __\n")
print("  / ____|                    \ \ / /  __ \ \   / /\n")
print(" | (___  _ __   __ _  ___ ___ \ V /| |__) \ \_/ / \n")
print("  \___ \| '_ \ / _` |/ __/ _ \ > < |  ___/ \   /  \n")
print("  ____) | |_) | (_| | (_|  __// . \| |      | |   \n")
print(" |_____/| .__/ \__,_|\___\___/_/ \_\_|      |_|   \n")
print("        | |                                       \n")
print("        |_|                                       \n")

while True:
    
    print("What informations do you want?")
    print("1) Capsules")
    print("2) Rockets")
    print("3) Informations of SpaceX")
    inp = input("> ")

    #If input equals '1'
    if inp == "1":
        
        while True:
            #Print capsules' data
            loadDumpCapsulesData()
            inpexit = input("> Quit? (y/n)")
            if inpexit == "y":
                break

    #If input equals '2' 
    if inp == "2":
        while True:
            #Print rockets' data
            loadDumpRocketsData()
            inpexit = input("> Quit? (y/n)")
            if inpexit == "y":
                break

    #If input equals '3'
    if inp == "3":
        while True:
            #Print company's data
            loadDumpCompanyData()
            inpexit = input("> Quit? (y/n)")
            if inpexit == "y":
                break


