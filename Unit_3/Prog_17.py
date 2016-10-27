__author__ = 'Dr.S.Gowrishankar'

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 gs@gmail.com'

#x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 From gs@gmail.com'

#This extracts multiple mail ids from anywhere in the text
y = re.findall('\S+@\S+',x)
print(y)

#Code is much more optimized in such a way that the
#mail id is extracted from beginning of the line that start from 'From' word
#other mail ids are ignored since they do not start at the beginning of the line with 'From' word
y = re.findall('^From (\S+@\S+)',x)
print(y)



