__author__ = 'Dr.S.Gowrishankar'

import re
lin = 'From the stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

y = re.findall('^From .+@([^ ]+)',lin)
print(y)

y = re.findall('^From .+@([a-z.]*)',lin)
print(y)
