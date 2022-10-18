import requests
from requests.auth import HTTPBasicAuth
import json
import yaml




def getUserTaskIDs(worklogAuthor):
   with open("config.yml", "r") as ymlfile:
      api_token = yaml.safe_load(ymlfile)["access"]["api_token"]
      
   auth = HTTPBasicAuth("jan.novopacky@icord.cz", f"{api_token}")
   worklogAuthor = worklogAuthor

   url = "https://mluvii.atlassian.net/rest/api/3/search"

   headers = {
      "Accept": "application/json"
   }

   query = {
      'jql': f'project = Mluvii AND worklogAuthor = {worklogAuthor} AND worklogDate >= startOfMonth() AND worklogDate < startOfMonth(1) order by created DESC'
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query,
      auth=auth
   )
   
   #print(response.text)
   #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

   outputJSON = json.loads(response.text)

   taskIDs = []

   for i in range(len(outputJSON["issues"])):
      taskIDs.append(outputJSON["issues"][i]["key"])
   return taskIDs
      

