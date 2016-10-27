__author__ = 'Dr.S.Gowrishankar'

#Parsing HTML using regular expressions

# Search for lines that start with "href=”http://"

import urllib.request, urllib.parse, urllib.error
import re

#url = input('Enter - ')

url = 'http://www.dr-chuck.com/page1.htm'

#url = 'http://www.pythonlearn.com/book.htm'

html = urllib.request.urlopen(url).read()

links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())
