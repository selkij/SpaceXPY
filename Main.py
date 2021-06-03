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

    fstr = 'Voici les informations sur les fusées:\n\n'
    for x in data:
        fstr += '\n'.format(x, x['land_landings'] + x['water_landings'])
    

    print(fstr)


def loadDumpCapsulesData():
    dumpCapsulesData()
    data = loadCapsulesData()

    fstr = 'Voici les informations sur les capsules:\n\n'
    for x in data:
        fstr += '{0[serial]}: ré-utilisée {0[reuse_count]} fois, est attérie sur l\'eau {0[water_landings]} fois, est attérie sur terre {0[land_landings]} fois, est attérie  {1} fois au total, status : {0[status]}, type de capsule : {0[type]}, identifiant : {0[id]}\n'.format(x, x['land_landings'] + x['water_landings'])
    

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

    fstr = 'Voici les informations sur la compagnie SpaceX:\n\n'
    fstr += 'Nom de la compagnie: {0[name]}\n Fondateur de SpaceX: {0[founder]}\n Créé en: {0[founded]}\n CEO: {0[ceo]}\n CTO: {0[cto]}\n COO: {0[coo]}\n Propulsion du CTO: {0[cto_propulsion]}\n Nombre d\'employés dans SpaceX: {0[employees]}\n Valeur de SpaceX: {0[valuation]} Nombre de voitures: {0[vehicles]}\n Nombre de sites de lancement: {0[launch_sites]}\n Nombre de sites de test: {0[test_sites]}\n Description de SpaceX: SpaceX conçoit, fabrique et lance des fusées et des engins spatiaux avancés. La société a été fondée en 2002 pour révolutionner la technologie spatiale, dans le but ultime de permettre aux gens de vivre sur d\'autres planètes.'.format(data)
    

    print(fstr)
    

    print(fstr)


print("Powered by SpaceX api https://github.com/r-spacex/SpaceX-API\n")

while True:
    print("Quelles informations voulez vous?")
    print("1) Capsules")
    print("2) Fusées")
    print("3) Informations sur SpaceX")
    inp = input("> ")

    if inp == "1":
        
        while True:
            loadDumpCapsulesData()
            inpexit = input("> Quitter? (y/n)")
            if inpexit == "y":
                break
        
    if inp == "2":
        pass

    if inp == "3":
        while True:
            loadDumpCompanyData()
            inpexit = input("> Quitter? (y/n)")
            if inpexit == "y":
                break
