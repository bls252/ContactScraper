'''
Brianna Singer
July 5th, 2017
Version: 1.0

'''

#to call from terminal:
# first go into the directory that holds this file, probably "Scraper"
# type: $ python -c 'import netNarrow; print netGetter.getNets("John", "Stewart")'

''' Takes a first name, a middle name, a last name, and a dictionary of names and netIDs as parameters. 
Returns a new version of the dictionary with only names that match the first and last 
name parameters. Allows middle names and middle initials.'''

def netNarrow(fist, last, **data): #takes a dictionary as a parameter

	# netData = {u'James Howard Smith': u'jhs26',
	#  u'James C. Smith': u'jcs478',
	#  u'James P. Naismith': u'jpn44',
	#   u'James E. Smith': u'jes494',
	#   u'James O. Goldsmith': u'jog5',
	#    u'James A. Goldsmith': u'jag299',
	#    u'Alfred James Smith III': u'ajs485',
	#     u'James B. Smithson': u'jbs233',
	#     u'James Cooper Smith': u'jcs384',
	#      u'James D. Smith': u'jds37',
	#      u'James A. Smith': u'jas728',
	#       u'James R. Smith, II': u'jrs2',
	#       u'James G. Smith': u'jgs228',
	#        u'James Anthony Smith': u'jas372',
	#        u'James William Smithmeyer': u'jws45',
	#         u'James B. Smith': u'jbs354',
	#         u'James H. Smith Jr': u'jhs63',
	#         u'Gregory James Smith, Esq': u'gjs16',
	#          u'Theodore James Goldsmith': u'tjg26',
	#           u'Aaron James Smith': u'ajs585',
	#           u'James Paul Smith': u'jps336',
	#            u'James E. Smith Jr': u'jes334',
	#            u'James S. Smith Jr PhD': u'jss344',
	#             u'James Nesmith III': u'jn277',
	#             u'James T. Smith': u'jts98',
	#              u'James F. Smith': u'jfs242',
	#              u'James W. Smith': u'jws346',
	#               u'William James Smith': u'wjs14',
	#               u'James M. Smith': u'jms488',
	#                u'James Hewitt Smith': u'jhs222',
	#                u'James R. Smith': u'jrs522',
	#                 u'James Francis Smith III': u'jfs248',
	#                 u'Michael James Smith': u'mjs648',
	#                  u'James A. Smith Jr Esq': u'jas592',
	#                  u'James L. Smith': u'jls454',
	#                   u'James D. Smith, PhD': u'jds58'}

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



# ///////////////////////////////Testing Only ///////////////////////////////////////////////


# key = next(iter(netData))

# newKey = key
# 	for removable in removables:
# 		if removable in newKey:
# 			newKey = newKey.replace(removable, '') #take the removable out of key
# 	#print newKey




# frontLen = len(firstName)
# backLen = len(lastName)

# frontSec = newKey[:frontLen] # this is the first several letters of key
# backSec = newKey[-backLen:] # this is the last several letters of key

# if frontSec == firstName and backSec == lastName:
	# print key + 'has first name: ' + firstName + 'and last name ' + lastName


