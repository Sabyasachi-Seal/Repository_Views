import json
import requests
import os

username = "Sabyasachi-Seal"
request = requests.get('https://api.github.com/users/'+username+'/repos')
jsonfile = request.json()

file = open('./config.json', 'r')
readfile = file.read()
file.close()


data = json.loads(readfile)
newdata = []

for i in range(0,len(jsonfile)):
    newdata.append(jsonfile[i]['name'])

data['repository'] = newdata

jsondump = json.dumps(data)
file = open('./config.json', 'w')
file.write(jsondump)
file.close()

print("Updated Repository List")

os.system('git add .')
os.system('git commit -m "repository list update"')
os.system('git push')