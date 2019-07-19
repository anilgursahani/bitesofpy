NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    nameList = []
    for name in names:
        name = name.title()
        nameList.append(name)
    nameList = set(nameList)
    nameList = list(nameList)
    return nameList
    
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    namesDict = {}
    lastnames = []
    sortedNames = []
    for fullname in names:
        (firstname, lastname) = fullname.split(" ") # extract out last name.  We will use lastname as key into dictionary to store the full name
        lastnames.append(lastname) # append last name to list which will be sorted
        namesDict[lastname]= fullname # store fullname into dictionary using lastname as the key
    
    lastnames.sort(reverse=True)
    
    for lastname in lastnames:
        sortedNames.append(namesDict[lastname])
    
    return sortedNames

       
def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortestFirstNameLen = 100 # set a large sentinel for shortest first namelength so that the len of first name that we get will for starters be set to
                               # the shortest first name length
    for fullname in names:
        (firstname, lastname) = fullname.split(" ") # Extract out the firstname
        firstnameLen = len(firstname)
        if firstnameLen < shortestFirstNameLen:
            shortestFirstName= firstname
            shortestFirstNameLen = firstnameLen
            
        
    return shortestFirstName
            
        
        
        
    
    # ...