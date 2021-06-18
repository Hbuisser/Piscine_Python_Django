#!/usr/bin/python3

# https://www.mediawiki.org/wiki/API:Search
# https://public.paws.wmcloud.org/User:APaskulin_(WMF)/en-wikipedia-search.ipynb

import requests
import json
import sys
import dewiki
def get_wiki():
	if len(sys.argv) != 2:
		print("Error, wrong number of arguments")
	arg = sys.argv[1]
	search_query = arg
	SEARCHPAGE = ""
	number_of_results = 3
	endpoint = 'search/page'
	base_url = 'https://en.wikipedia.org/w/rest.php/v1/'
	headers = {'User-Agent': "Edessain"}
	url = base_url + endpoint
	response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
	response = json.loads(response.text)
	for page in response['pages']:
		SEARCHPAGE = page['title']
		break
	if SEARCHPAGE == "":
		print("page not found")
		return
	S = requests.Session()
	URL = "https://fr.wikipedia.org/w/api.php"
	PARAMS = {
		"action": "parse",
		"format": "json",
		"list": "search",
		"page": SEARCHPAGE,
		"prop": "wikitext",
		"formatversion": "2"
	}
	R = S.get(url=URL, params=PARAMS)
	if (R.status_code) >= 400:
		print("There was an error with the request")
		return
	DATA = R.json()
	if DATA.get('parse') == None:
		print("Oops!  no text to display")
		return
	with open(f"{arg}.wiki".replace(" ", "_"), 'w') as f:
		f.write(dewiki.from_string(DATA['parse']['wikitext']))

if __name__ == '__main__':
	get_wiki()