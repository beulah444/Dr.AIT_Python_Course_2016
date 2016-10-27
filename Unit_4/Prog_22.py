__author__ = 'Dr.S.Gowrishankar'

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

p = Point(3, 4)

print("When we use __str__ method")
str(p)

print("When we use print method")
print(p)