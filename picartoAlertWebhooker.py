#Picarto Alerts webhooker
import requests
import json
from time import sleep

def parseUsers(jsonData):
    online = []
    for creator in jsonData:
        online.append(creator['name'].lower())
    print(online)
    exit()
    return online

#Main execution starts here
creatorsSeen = {}
while(True):
    #Read configuration file to retrieve list of servers and creators to monitor for that server
    hooksFile = open('webhooks.json', 'r')
    webhooks = json.load(hooksFile)['webhooks']
    hooksFile.close()
    
    errorState = false
    onlineCreators = []
    try:
        onlineCreators = parseUsers(json.loads(requests.get("http://api.picarto.tv/v1/online?adult=true&gaming=true").text))
    except:
        print("Error communicating with picarto, retrying in 60 seconds.")
        sleep(60)
        continue
    
    #Iterate over all servers
    for server in webhooks:
        print("Checking: " + server['serverName'])
        if server['serverName'] not in creatorsSeen.keys():
            creatorsSeen[server['serverName']] = []

        #Iterate over all creators for that server
        for creator.lower() in server['creators']:
            #If a creator is online *and* has not already been announced to the server, announce to the server
            #Otherwise do nothing, if a previously seen creator returns offline, flag them as offline so they'll be announced next time they come online
            if creator in onlineCreators:
                if creator in creatorsSeen[server['serverName']]:
                    continue
                else:
                    creatorsSeen[server['serverName']].append(creator)
                    try:
                        if server['useAtHere']:
                            requests.post(server['url'], {"content" :"@here " + creator + " has gone live on Picarto\nhttps://picarto.tv/" + creator})
                        else:
                            requests.post(server['url'], {"content" : creator + " has gone live on Picarto\nhttps://picarto.tv/" + creator})
                        print(creator + " now online.")
                    except:
                        creatorsSeen[server['serverName']].remove(creator)
                        errorState = true
                        print("Couldn't reach discord server " + server["serverName"] + ". Retrying in 60 seconds.")
            else:
                if creator in creatorsSeen[server['serverName']]:
                    creatorsSeen[server['serverName']].remove(creator)
                    print(creator + " now offline.")
    #Take a nap for three minutes
    sleep(180)