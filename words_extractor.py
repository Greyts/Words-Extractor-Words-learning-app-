import requests
import lxml.html
from bs4 import BeautifulSoup

def get_page(url): # preparing the soup

    result = requests.get(url)

    if not result.ok: # checking if the page responded
        print('Server responded: ', result.status_code)
    else:
        print('Server responded correctly: ', result.status_code)
        soup = BeautifulSoup(result.text, "lxml")
    return soup

def get_list_of_pages(soup): # puts all the links to each section in a list

    pages = soup.find_all(class_='col-md-1')
    links = [link.a.get('href') for link in pages]
    return links

def page_under(links): # creates soup out of every link to each section

    return [get_page(f'https://fiszkoteka.pl{link}') for link in links]

def main_extractor(): # main

    url = 'https://fiszkoteka.pl/tag/1002-slowka-rosyjski'
    multi_soup = page_under(get_list_of_pages(get_page(url)))
    pages_words_class = [soup.find_all(class_="col-md-4 col-xs-8") for soup in multi_soup]
    words = []
    for page in pages_words_class:
        words.append([word.text.replace('rozpocznij naukę', '').replace('\n', '').strip() for word in page])
        """single for single in"""

    words_dict = {}
    for list in words:
        words_dict.update({
            list[n]: list[n + 1] for n in range(int(len(list))) if n % 2 == 0
        })

    return words_dict
