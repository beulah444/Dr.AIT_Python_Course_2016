__author__ = 'Dr.S.Gowrishankar'

#Using urllib, you can treat a web page much like a file. You simply indicate
#which web page you would like to retrieve and urllib handles all of the HTTP
#protocol and header details.

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

