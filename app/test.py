import requests
from requests.auth import HTTPBasicAuth
import json
import yaml

with open("app/config.yml", "r") as ymlfile:
    api_token = yaml.safe_load(ymlfile)["access"]["api_token"]

auth = HTTPBasicAuth("jan.novopacky@icord.cz", f"{api_token}")

url = "https://mluvii.atlassian.net/rest/api/3/user/search"


headers = {
   "Accept": "application/json"
}

query = {
   'query': 'project = Mluvii'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

displayName = []
accountId = []
for i in range(len(json.loads(response.text))):
    displayName.append(json.loads(response.text)[i]["displayName"])
    accountId.append(json.loads(response.text)[i]["accountId"])

res = {displayName[i]: accountId[i] for i in range(len(displayName))}
print(res)

