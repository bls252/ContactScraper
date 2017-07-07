# $ python -c 'import scrape_monster; print scrape_monster.getNumberMonsterResultPages("sewing","california")'



import requests
from bs4 import BeautifulSoup
import re

'''takes input of first name and last name and returns a dictionary of result names and NetIDs'''
def getNets(first, last):

	url = 'https://www.cornell.edu/search/people.cfm?q=' + str(first) + '+' + str(last) + '&tab=people'
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	alumLink = soup.find_all('a', {'name': 'Alumni'})[0]
	alumCap = alumLink.parent
	resultTable = alumCap.parent
	if resultTable['class'] == 'results cu-table':
		rows = resultTable.find_all("tr")
	else:
		print "error finding result table"

	resultDict = dict()	

	for row in rows:
		nameCell = row.find_all('td', {'class': 'name'})[0]
		contactName = nameCell.text
		print contactName
		netSpan = row.find_all('span', {'class': 'label'})[0]#everything above this line works
		if netSpan.text == "NetID:":
			netCell = netSpan.parent
			contactNetUnparsed = netCell.text # example: "NetID: jbs263"
			contactNet = contactNetUnparsed.replace('NetID: ', '')
			resultDict[contactName] = contactNet
		else:
			print "couldn't find NetID span, yo"


