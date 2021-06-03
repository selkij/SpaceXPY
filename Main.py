from os import system

system('pip install requests')

from requests import get
import json
import time


def dumpCapsulesData():   
    r = get("https://api.spacexdata.com/v4/capsules")
    with open('capsules.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)


def loadCapsulesData():
    return dict(json.load(open('capsules.json', 'r')))['value']


def dumpRocketsData():   
    r = get("https://api.spacexdata.com/v4/rockets")
    with open('rockets.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)


def loadRocketsData():
    return dict(json.load(open('rockets.json', 'r')))['value']


def loadDumpRocketsData():
    dumpRocketsData()
    data = loadRocketsData()

    fstr = 'Rockets informations:\n\n'
    for x in data:
        fstr += '\n'.format(x, x['land_landings'] + x['water_landings'])
    

    print(fstr)


def loadDumpCapsulesData():
    dumpCapsulesData()
    data = loadCapsulesData()

    fstr = 'Capsules informations:\n\n'
    for x in data:
        fstr += '{0[serial]}: reused {0[reuse_count]} times, landed on water {0[water_landings]} times, landed on land {0[land_landings]} times, landed  {1} times in total, status : {0[status]}, type of capsule : {0[type]}, id : {0[id]}\n'.format(x, x['land_landings'] + x['water_landings'])
    

    print(fstr)


def dumpCompanyData():   
    r = get("https://api.spacexdata.com/v4/company")
    with open('company.json', 'w') as f:
        json.dump({'value':r.json()}, f, indent=4)


def loadCompanyData():
    return dict(json.load(open('company.json', 'r')))['value']


def loadDumpCompanyData():
    dumpCompanyData()
    data = loadCompanyData()

    fstr = 'SpaceX informations:\n\n'
    fstr += 'Company name: {0[name]}\n SpaceX founder: {0[founder]}\n Founded in: {0[founded]}\n CEO: {0[ceo]}\n CTO: {0[cto]}\n COO: {0[coo]}\n Propulsion of CTO: {0[cto_propulsion]}\n Number of employees in SpaceX: {0[employees]}\n Value of SpaceX: {0[valuation]}\n Number of vehicles: {0[vehicles]}\n Number of launch sites: {0[launch_sites]}\n Number of test sites: {0[test_sites]}\n Description of SpaceX: {0[summary]}'.format(data)
    

    print(fstr)
    

    print(fstr)


print("Powered by SpaceX api https://github.com/r-spacex/SpaceX-API\n")

while True:
    print("What information do you want?")
    print("1) Capsules")
    print("2) Rockets")
    print("3) Informations of SpaceX")
    inp = input("> ")

    if inp == "1":
        
        while True:
            loadDumpCapsulesData()
            inpexit = input("> Quit? (y/n)")
            if inpexit == "y":
                break
        
    if inp == "2":
        pass

    if inp == "3":
        while True:
            loadDumpCompanyData()
            inpexit = input("> Quit? (y/n)")
            if inpexit == "y":
                break
