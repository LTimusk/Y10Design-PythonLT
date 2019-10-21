import json
import requests

#*************************** RETRIEVING DATA ******************************************

request = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Toronto")
request_text = request.text

#print(type(data))

data = json.loads(request_text)


#*************************** USER REQUESTS ******************************************





datajson = request.json()
datapoint1 = datajson ['player'][12]['strPlayer']
print (datapoint1)









