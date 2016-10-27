__author__ = 'Dr.S.Gowrishankar'

import re

import re
x = 'My 2 favorite numbers are 19 and 42'

print('When + is used it matches One or more instances')
#Here the + checks the preceding expression for numbers which can be single digit or multiple digits
y = re.findall('[0-9]+',x)
print(y)

print('when * is used it matches zero or more instances')
#Here the * checks the preceding expression for numbers but since * matches zero instance
#even if we do not have an matching instance it returns you none
z = re.findall('[0-9]*',x)
print(z)


