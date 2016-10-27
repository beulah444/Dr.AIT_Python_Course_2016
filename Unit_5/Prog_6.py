__author__ = 'Dr.S.Gowrishankar'

#Parsing HTML using BeautifulSoup
#We will use urllib to read the page and then use BeautifulSoup to extract the
#href attributes from the anchor (a) tags.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter - ')

#url = 'http://www.dr-chuck.com/page1.htm'

url = 'http://www.pythonlearn.com/book.htm'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



