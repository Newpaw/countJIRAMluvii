import requests
from requests.auth import HTTPBasicAuth
import json
from all import getUserTaskIDs
from tasks import getTimeForUser

#worklogAuthor = "62f9fcb31e82e839c24f4417"
worklogAuthor = "61a73fa8c75da80072f8fb5e"

if __name__ == "__main__":
    allIDs = getUserTaskIDs(worklogAuthor)
    allWorklogsTime = getTimeForUser(worklogAuthor, allIDs)
    pocetHodin = str((sum(allWorklogsTime)/60))
    pocetDni = str((sum(allWorklogsTime)/60/8))
    print(f"{pocetHodin} hodin neboli {pocetDni} dní")
