__author__ = 'Dr.S.Gowrishankar'

import re
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)

x = 'From: Using the: character:'
z = re.findall('^F.+:', x)
print(z)

p = 'From: Using the: character'
q = re.findall('^F.+', p)
print(q)