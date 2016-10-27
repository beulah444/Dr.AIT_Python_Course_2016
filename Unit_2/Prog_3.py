__author__ = 'Dr.S.Gowrishankar'

#ask user to input a number continuously and find its square number. Use break to come out of the loop if the user wants to stop executing the loop.

while True:
    num = int(input("Enter a number: "))
    #num = 11
    print("square of %d is %d"%(num, num * num ))
    print("Want to enter another number y/n: ")
    another = input()
    #print another
    if another == 'y':
        continue
    else:
        break