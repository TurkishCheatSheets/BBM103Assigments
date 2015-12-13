def commandParser():
    f = open('commandsP1.txt', 'r')
    allCommands = []
    for line in f:
        params = line.replace('\r\n','').split(' ')
        allCommands.append(params)
    f.close()
    for command in allCommands:
        if command[0] == "AU":
            if len(command) != 3:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                addUser(command[1], command[2])
        elif command[0] == "RU":
            if len(command) != 2:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                removeUser(command[1])
        elif command[0] == "AR":
            if len(command) != 3:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                addRelation(command[1],command[2],True)
        elif command[0] == "RR":
            if len(command) != 3:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                removeRelation(command[1],command[2],True)
        elif command[0] == "PA":
            if len(command) != 2:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                rankUser(int(command[1]))
        elif command[0] == "SA":
            if len(command) != 3:
                print "Error: Wrong input type for '%s'" % (command[0])
            else:
                suggestFriendship(command[1],int(command[2]))
        else:
            print "Error: Undefined command type!"

def networkFileParse():
    f = open('sn.txt', 'r')
    for line in f:
        network.update({line[0]:line[2:].replace('\n','').replace(' ','')})
    f.close()

def updateSNFile():
    file_ = open('sn.txt', 'w')
    for key in network:
         file_.writelines(key + ":" +str([x for x in network[key]]).replace('[','').replace(']','').replace("'","").replace(',','') + "\n")
    file_.close()

def sort_(d):
    #Returns the keys of dictionary d sorted by their values
    items = d.items()
    reversedItems = [[item[1],item[0]] for item in items]
    reversedItems.sort()
    return [reversedItems[i][1] for i in range(0,len(reversedItems))]

def dictSort(d):
	free_ = []
	for key in sort_(d):
		free_.append([key,d[key]])

	return free_[::-1]

def hasRelation(sourceUser,targetUser):
    friends = list(network[sourceUser])
    if targetUser in friends:
        return True
    else:
        return False

def addUser(newUser,existingUser):
    if newUser in network.keys():
        print "This user already exists!!"
    else:
        if existingUser not in network.keys():
            print "There is no user named '%s'" % (existingUser)
        else:
            network.update({newUser:''})
            addRelation(newUser,existingUser,False)
            updateSNFile()
            print "User '%s' has been added and tied to '%s' successfully" % (newUser, existingUser)

def removeUser(username):
    if username not in network.keys():
        print "There is no user named '%s'" % (username)
    else:
        for friend in list(network[username]):
            removeRelation(username,friend,False)
        del network[username]
        updateSNFile()
        print "User '%s' and its all relations have been removed successfully." % (username)

def addRelation(sourceUser,targetUser,output):
    if sourceUser not in network.keys():
        print "There is no user named '%s'" % (sourceUser)
    else:
        if targetUser not in network.keys():
            print "There is no user named '%s'" % (targetUser)
        else:
            if hasRelation(sourceUser,targetUser):
                print "A relation between '%s' and '%s' already exists!!" % (sourceUser,targetUser)
            else:
                network[sourceUser] += targetUser  #Add source to target's friend list
                network[targetUser] += sourceUser  #Add target to source's friend list
                updateSNFile()
                if output:
                    print "Relation between '%s' and '%s' has been added succesfully." % (sourceUser,targetUser)

def removeRelation(sourceUser,targetUser,output):
    if sourceUser not in network.keys():
        print "There is no user named '%s'" % (sourceUser)
    else:
        if targetUser not in network.keys():
            print "There is no user named '%s'" % (targetUser)
        else:
            if not hasRelation(sourceUser,targetUser):
                print "No relation between '%s' and '%s' found!!" % (sourceUser,targetUser)
            else:
                friends = list(network[sourceUser])
                friends.remove(targetUser)
                network[sourceUser] = ""
                for friend in friends:
                    network[sourceUser] += friend
                friends = list(network[targetUser])
                friends.remove(sourceUser)
                network[targetUser] = ""
                for friend in friends:
                    network[targetUser] += friend
                updateSNFile()
                if output:
                    print "A relation between '%s' and '%s' has been removed successfully." % (sourceUser,targetUser)

def rankUser(n):
    if n > len(network.keys()):
        limit = len(network.keys())
        print "Invalid input since n is greater than %s" % (limit)
        rankUser(20)
        print "------------"
    else:
        rankDict = {}
	for key in network:
		friends = len(network[key])
		rankDict.update({key:friends})
	for i in range(n):
		item = dictSort(rankDict)[i]
		print "User '%s' has '%s' friends" % (item[0],item[1])

def suggestFriendship(username,md):
    if username in network.keys():
        if len(network[username]) >= md:
            mutualList = set()
            b = []
            friendsOfUser = list(network[username])
            searchFor = network.keys()
            searchFor.remove(username)
            print "Suggestion List for '%s' (when MD is %s):" % (username,md)
            for user in friendsOfUser:
                searchFor.remove(user)
            for fou in friendsOfUser:
                for user in searchFor:
                    if fou in network[user]:
                        mutualList.add((user,fou))
            for e in mutualList:
                b.append(e[0])
            for e in set(b):
                if b.count(e) >= md:
                    print "'%s' has %s mutual friends with %s" % (username,md,e)
        else:
            print "User '%s' has less friend than %s" % (username,md)
    else:
        print "No user named '%s' found!!" % (username)


if __name__ == "__main__":
    network  = {}
    networkFileParse()
    commandParser()
