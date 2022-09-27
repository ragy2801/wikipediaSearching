"""
This script is to show the main factor of represent and how to use it with on HTML Parser
HTML Parser to use is BeautifulSoup: one of the best xml and html parsers
"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys      # allows me to grab arguments


if __name__ == '__main__':
    for url in sys.argv[1:]:

        # add https to url without protocol with layer
        if not url.lower().startswith('http'):
            url = f'https://{url}'

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

        for link in soup.findAll("h3"):
            print(link.div.string)
        # print(f"Yeah! worked!\n\n{soup.prettify()}")

