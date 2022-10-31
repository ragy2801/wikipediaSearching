"""
This script is to show the main factor of represent and how to use it with on HTML Parser
HTML Parser to use is BeautifulSoup: one of the best xml and html parsers
"""

import argparse  # allows me to grab arguments
import sys
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


# dispatch tables for dictionary
def search_google(terms):
    terms = "+".join(terms.split())
    url = f"https://www.google.com/search?q={terms}"
    soup = BeautifulSoup(get_response(url), 'html.parser')

    for link in soup.findAll("a", href=True):
        # if "Alice's Adventures in Wonderland" in link.text:
        #     print(link['href'][7:])
        #     return link['href'][7:]
        return link.text


def search_amazon(terms):
    terms = "+".join(terms.split())
    url = f"https://www.amazon.com/s?k={terms}"
    soup = BeautifulSoup(get_response(url), 'html.parser')

    for link in soup.findAll("h3"):
        print(link.div.string)
        return link.text


def search_wikipedia(terms):
    terms = "_".join(terms.split())
    url = f"https://en.wikipendia.org/wiki/{terms}_(disambiguation)"
    soup = BeautifulSoup(get_response(url), 'html.parser')

    for blockClass in soup.findAll('div', attrs={'class': 'mw-parser-output'}):
        for link in blockClass.findAll(href=True):
            print(link.get_text())
            return link.get_text()


def search_gutenberg(terms):
    terms = "+".join(terms.split())
    #       https://www.gutenberg.org/ebooks/search/?query=alice+in+wonderland&submit_search=Go%21
    url = f"https://www.gutenberg.org/ebooks/search/?query={terms}&submit_search=Go%21"

    soup = BeautifulSoup(get_response(url), 'html.parser')

    for link in soup.findAll("a", href=True):
        # if "Alice's Adventures in Wonderland" in link.text:
        #     print(link['href'][7:])
        #     return link['href'][7:]
        return link.text


sites = {
    "google": search_google,
    "amazon": search_amazon,
    "wikipedia": search_wikipedia,
    "gutenberg": search_gutenberg,
    "wiki": search_wikipedia,
    "books": search_gutenberg
}


def init():
    sysargs = argparse.ArgumentParser(description="Loads passed shortcuts to file after initial cleaning (munging).")
    sysargs.add_argument("-q", "--query", help="The term(s) to search for.")
    sysargs.add_argument("-s", "--site", help="The site to search (google, wikipedia, gutenberg, amazon")
    args = sysargs.parse_args()

    # check that all args were passed
    site = str(args.site).lower()
    try:
        if sites[site] is not None and args.query:
            return sites.get(site)(args.query)
        else:
            print("You must pass two arguments: (-s, --site) and (-q, --query) type strings to use program")
            quit(1)
    except (KeyError, TypeError) as ex:
        print("Acceptable sites to search for are: google, wikipedia, gutenberg")
        quit(1)


def get_response(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as httperr:
        print(f"HTTP error: {httperr}")
        sys.exit(1)
    except Exception as err:
        print(f"Something went really wrong: {err}")
        sys.exit(1)

    return response.text


if __name__ == '__main__':
    uri = init()
    print(get_response(uri))
    # open our page with beautifulSoup to parse it and find information
