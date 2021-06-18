import sys
import requests
from bs4 import BeautifulSoup

# BS produit un arbre syntaxique qui peut être utilisé pour chercher des éléments ou les modifier. 
# Lorsque le document HTML ou XML est mal formé (par exemple s'il manque des balises fermantes), Beautiful Soup propose une approche à base d'heuristiques afin de reconstituer l'arbre syntaxique sans générer d'erreurs

def main():
    if len(sys.argv) != 2:
        return
    URL = 'https://en.wikipedia.org/wiki/' + sys.argv[1]
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find(id='mw-content-text').find(class_="mw-parser-output").find_all('p', recursive=False)
    list_a = []
    for p in paragraphs:
        p_links = p.find_all("a", recursive=False)
        for link in p_links:
            print(link.get('href'))
            list_a.append(link.get('href'))
            break

if __name__ == '__main__':
    main()

#     import sys, requests
# from bs4 import BeautifulSoup
# ​
# def main(search):
# 	S = requests.session()
	
# 	init_search = search
# 	count = 0
# 	road_to_philosophy = []
# 	title = str()
# 	while (title != 'Philosophy'):
# 		url = 'https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=en&search={}&language=en&go=Go'.format(search)
# 		page = S.get(url)
# 		soup = BeautifulSoup(page.content, 'html.parser')
		
# 		results = soup.find_all('p')
# 		first_link = ''
# 		i = 0
# 		while (i < len(results)):
# 			if (first_link != ''):
# 				break
# 			if ('line-height' not in str(results[i]) and 'thumb' not in str(results[i])):
# 				a = results[i].find_all('a')
# 				if (a):
# 					for link in a:
# 						s_link = str(link)
# 						index = str(results[i]).find(s_link)
# 						if ('href' in s_link and ':' not in s_link and 'cite_note' not in s_link and '/wiki/' in s_link and str(results[i])[index - 1] != '('):
# 							first_link = s_link
# 							break
# 			i += 1
# ​
# 		if (first_link == ''):
# 			print('It leads to a dead end !')
# 			exit()
# 		#print(first_link)
# ​
# 		i = first_link.find('/wiki/')
# 		j = first_link.find('title')
# 		k = first_link.find('>')
# 		search = first_link[i+6:j-2]
# 		title = first_link[j+7:k-1]	
# 		if (title in road_to_philosophy):
# 			print('It leads to an infinite loop !')
# 			exit()
# 		road_to_philosophy.append(title)
# 		count += 1
# ​
	
# 	for elem in road_to_philosophy:
# 		print(elem)
# 	if (count == 1):
# 		road = 'road'
# 	else:
# 		road = 'roads'
# 	print('{count} {road} from {init_search} to philosophy'.format(count=count, road=road, init_search=init_search))
# ​
# ​
# ​
# if __name__ == '__main__':
# 	if (len(sys.argv) != 2):
# 		print('Invalid number of arguments')
# 		exit()
# 	main(sys.argv[1])