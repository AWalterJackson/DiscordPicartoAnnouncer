import requests
import json

#webhookURL = ""
#webhookURL = ""
webhookURL = ""
dataString = "An outbreak of H5N1 Avian influenza has been detected in Hunan province, Mainland China. (Deaths: 4,500 chickens from disease, 17,828 chickens from culling). (NHC, DXY)"
avatarOverride = "https://i.imgur.com/p4hoKss.png"
requests.post(webhookURL, {"content": dataString, "avatar_url" : avatarOverride, "username" : "CoronaWatch"}, timeout = 10)