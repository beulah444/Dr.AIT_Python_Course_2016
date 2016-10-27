__author__ = 'Dr.S.Gowrishankar'


# Write a program to prompt the user for hours and rate per hour to compute gross pay.

inp = input('Enter Hours: ')
hours = float(inp)
inp = input('Enter Rate: ')
rate = float(inp)
pay = hours * rate
print('Pay:', pay)
