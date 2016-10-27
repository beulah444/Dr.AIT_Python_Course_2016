__author__ = 'Dr.S.Gowrishankar'

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# \S -> Matches any single non-whitespace character

y = re.findall('\S',x)
# Here any non-while space character is matched.
# It matches single character which goes on continuously while spaces are ignored
print(y)

#Here * matches all the characters in a word multiple times but even white space is included in output
y = re.findall('\S*',x)
print(y)

#Here + matches all the characters in a word multiple times while white spaces are ignored
y = re.findall('\S+',x)
print(y)

#Here what happens is re will start to check from first character and will consider it but what happens is
#after considering the characters of the word 'From' it encounters white space so that part is ignored
#but when it start to read from character s it encounters the special character @ which we have mentioned
#at this stage re deduces that this is the expression it was looking for.
#always read the regular expression in its entirety not in stand alone mode.
#if we are looking for some character (or special character then we have to explicitly specify it
y = re.findall('\S+@\S+',x)
print(y)

#There should be atleast two characters. Thats the reason 5 is not displayed
y = re.findall('\S+\S+',x)
print(y)