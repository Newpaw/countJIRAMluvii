import requests
from requests.auth import HTTPBasicAuth
import json


def getTimeForUser(worklogAuthor, issues):
    worklogAuthor = worklogAuthor
    issues = issues
    allWorklogs = []
    for issue in issues:
        api_token = "k9Tq94tmbg5emSHOOft1320C"
        url = f"https://mluvii.atlassian.net/rest/api/3/issue/{issue}"

        auth = HTTPBasicAuth("jan.novopacky@icord.cz", f"{api_token}")

        headers = {
        "Accept": "application/json"
        }

        response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
        )
        outputJSON = json.loads(response.text)

        
        for i in range(len(outputJSON["fields"]["worklog"]["worklogs"])):
            if worklogAuthor == str(outputJSON["fields"]["worklog"]["worklogs"][i]["author"]["accountId"]):
                allWorklogs.append(outputJSON["fields"]["worklog"]["worklogs"][i]["timeSpentSeconds"]/60)
        
    return(allWorklogs)
