#file only for testing
import json

def loadRocketsData():
    return dict(json.load(open('rockets.json', 'r')))['value']

a = loadRocketsData()

for x in a:
    launcher = x
    c = launcher["height"]["meters"]
    print(c)