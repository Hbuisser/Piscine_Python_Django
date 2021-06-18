#!/usr/bin/python3

import requests
import json
import sys
import dewiki

def get_wiki():
    if len(sys.argv) != 2:
        return
    search_query = sys.argv[1]
    number_of_results = 3
    endpoint = 'search/page'
    base_url = 'https://en.wikipedia.org/w/rest.php/v1/'
    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://meta.wikimedia.org/wiki/User:APaskulin_(WMF))'}
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
    search_query = search_query.replace(" ", "_")
    with open(f"{search_query}.wiki", 'w') as f:
        f.write(dewiki.from_string(DATA['parse']['wikitext']))


if __name__ == '__main__':
    get_wiki()