__author__ = 'Dr.S.Gowrishankar'

class Time:
    pass

def add_time(t1, t2):
    movieEndTime = Time()
    movieEndTime.hours = t1.hours + t2.hours
    movieEndTime.minutes = t1.minutes + t2.minutes
    movieEndTime.seconds = t1.seconds + t2.seconds

    return movieEndTime

def print_time(t) :
    # A function to print out a time
    print("%d:%d:%d" % (t.hours, t.minutes, t.seconds))

start = Time()
start.hours = 9
start.minutes = 14
start.seconds = 30

duration = Time()
duration.hours = 3
duration.minutes = 35
duration.seconds = 0

done = add_time(start, duration)

print_time(done)



