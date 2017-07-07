'''
Brianna Singer
July 5th, 2017
Version: 1.0

'''



''' Takes a first name, a middle name, a last name, and a dictionary of names and netIDs as parameters. 
Returns a new version of the dictionary with only names that match the first and last 
name parameters. Allows middle names and middle initials.'''

def netNarrow(first, last, **data): #takes a dictionary as a parameter

	# firstName = 'James'
	# lastName = 'Smith'

	firstName = first
	lastName = last
	netData = **data



	removables = []

	removables.append(' PhD')
	removables.append(' Esq')
	removables.append(' Jr')
	removables.append(' III')
	removables.append(' II')
	removables.append(' I')
	removables.append(',')

	matchDict = {}


	for key in netData: # key represents just the name, not the netID
		newKey = key
		for removable in removables:
			if removable in newKey:
				newKey = newKey.replace(removable, '') #take the removable out of key
		#print newKey

		frontLen = len(firstName)
		backLen = len(lastName)

		frontSec = newKey[:frontLen] # this is the first several letters of key
		backSec = newKey[-backLen:] # this is the last several letters of key

		if frontSec == firstName and backSec == lastName:
			print key + 'has first name: ' + firstName + 'and last name ' + lastName
			matchDict[key] = netData[key]
		else:
			print "not a match"

	return matchDict