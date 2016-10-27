__author__ = 'Dr.S.Gowrishankar'

# remember each number as the user entered it and use built-in
# functions to compute the sum and count at the end.
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)