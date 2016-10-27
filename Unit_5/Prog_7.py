__author__ = 'Dr.S.Gowrishankar'

#Parsing HTML using BeautifulSoup
#You can use BeautifulSoup to pull out various parts of each tag as follows:

from urllib.request import urlopen
from bs4 import BeautifulSoup

#url = input('Enter - ')

url = 'http://www.dr-chuck.com/page1.htm'

html = urlopen(url).read()
# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


