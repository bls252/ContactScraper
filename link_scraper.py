#McKinsey alum link: https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221371%22%5D&facetSchool=%5B%2218946%22%5D


import requests
from bs4 import BeautifulSoup

current_page_url = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221371%22%5D&facetSchool=%5B%2218946%22%5D'

next_page = current_page_url + '&page=' + str(1)


r = requests.get(current_page_url)
soup = BeautifulSoup(r.content)
result_spans = soup.find_all('span', {'class': 'actor-name'})

result_count = 0

	for result in result_spans:
		result_count += 1
		name = result.find_all("span", {"class": "name actor-name"})
		print name