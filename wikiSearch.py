"""
This script is to show the main factor of represent and how to use it with on HTML Parser
HTML Parser to use is BeautifulSoup: one of the best xml and html parsers
"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys  # allows me to grab arguments

if __name__ == '__main__':

    for term in sys.argv[1:]:

        # add the term to the wikipedia url
        url = f'https://www.wikipedia.org/wiki/{term}_(disambiguation)'

        # Gets website url and provides response
        # if error - exits with exception
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as httperr:
            print(f"HTTP error: {httperr}")
            sys.exit(1)
        except Exception as err:
            print(f"Something went really wrong: {err}")

        # open our page with beautifulSoup to parse it and find information
        soup = BeautifulSoup(response.text, 'html.parser')

        # for link in soup.findAll(href=True):
        for blockClass in soup.findAll('div', attrs={'class': 'mw-parser-output'}):
            for link in blockClass.findAll(href=True):
                print(link.get_text())
