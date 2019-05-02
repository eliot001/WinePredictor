#import libraries
import requests
from bs4 import BeautifulSoup

print("Hello Fucking World")

def Scrape():
    # url to scrape
    pageLink = 'https://en.wikipedia.org/wiki/Walla_Walla%2C_Washington'

    # fetch content from url
    pageResponse = requests.get(pageLink, timeout=5)

    # use html parses to parse url content and store
    pageContent = BeautifulSoup(pageResponse.content, "html.parser")

    textContent = []
    #for i in range(len(textContent)):
    for i in range(0, 20):
        paragraphs = pageContent.find_all("td")[i].text
        textContent.append(paragraphs)

    print(*textContent, sep = "\n")

Scrape()
