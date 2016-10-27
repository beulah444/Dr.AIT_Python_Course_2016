__author__ = 'Dr.S.Gowrishankar'

#As an example, we can write a program to retrieve the data for romeo.txt and
#compute the frequency of each word in the file as follows:

import urllib.request, urllib.parse, urllib.error
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)