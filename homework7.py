RossList = [ 'Lisa' , 'Fred' , 'Chris' , 'Carol' , 'Frank' ]
ChandlerList = [ 'Melissa' , 'Jack' , 'Lisa' , 'Carol' , 'Pete' , 'Ben']
MonicaList = [  'Helen' , 'Frank' , 'Gunther' , 'Ben' , 'Pete' ]
PhoebeList = [ 'Gunther' , 'Judy' , 'Chris' , 'Fred' ]
RachelList = [ 'Emily' , 'Carol' , 'Richard' , 'Lisa' , 'Mona' ]
JoeyList = [ 'Susan' , 'Richard' , 'Frank' , 'Jack' , 'Fred' ]
FriendsList = ['Phoebe' , 'Rachel' , 'Chandler' , 'Ross' , 'Monica' , 'Joey']
InvitedList = RossList + ChandlerList + MonicaList + PhoebeList + RachelList + JoeyList + FriendsList

def remove_duplicates(duplist):
    noduplist = []
    
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
            
    return noduplist

print(remove_duplicates(InvitedList))

    

