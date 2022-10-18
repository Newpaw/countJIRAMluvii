from all import getUserTaskIDs
from tasks import getTimeForUser



def getUserTime(worklogAuthor):
    worklogAuthor = worklogAuthor
    allIDs = getUserTaskIDs(worklogAuthor)
    allWorklogsTime = getTimeForUser(worklogAuthor, allIDs)
    pocetHodin = str((sum(allWorklogsTime)/60))
    pocetDni = str((sum(allWorklogsTime)/60/8))
    return pocetHodin, pocetDni, allIDs, allWorklogsTime 
