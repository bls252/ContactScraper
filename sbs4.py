# based off the tutorial here: https://www.youtube.com/watch?v=3xQTJi2tqgk

import requests
from bs4 import BeautifulSoup


url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=los+angelous"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


		# Alternative:

		#print "<a href='%s'>%s</a>" %(link.get("href"), link.text) if "http" in link.get("href")


# how you find a div of a certain class, in this case the class is called "info":

g_data = soup.find_all("div", {"class": "info"})

# a forloop for getting the text of the divs of class "info"

for item in g_data:
	print item.text # item.contents would give us a comma separated list of all the child elements of each item


	_____


	Test junk:

	https://www.monster.com/jobs/search/?q=graphic-design&intcid=skr_navigation_nhpso_searchMain&sort=rv.dt.di

#<h4>We couldn't find this page for you</h4>