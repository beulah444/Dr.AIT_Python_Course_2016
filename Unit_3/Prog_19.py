__author__ = 'Dr.S.Gowrishankar'

import re

hand = open('test.txt')
for line in hand:
    line = line.rstrip()
    #When u use *
    extractedString = re.findall('^X.*:', line)
    print(extractedString)

    # When u use +
    extractedString = re.findall('^X.+:', line)
    print(extractedString)
