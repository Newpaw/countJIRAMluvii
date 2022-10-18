from all import getUserTaskIDs
from tasks import getTimeForUser

worklogAuthors = ["62f9fcb31e82e839c24f4417", "61a73fa8c75da80072f8fb5e"]

if __name__ == "__main__":
    for worklogAuthor in worklogAuthors:
        allIDs = getUserTaskIDs(worklogAuthor)
        allWorklogsTime = getTimeForUser(worklogAuthor, allIDs)
        pocetHodin = str((sum(allWorklogsTime)/60))
        pocetDni = str((sum(allWorklogsTime)/60/8))
        print(f"{pocetHodin} hodin neboli {pocetDni} dní")
