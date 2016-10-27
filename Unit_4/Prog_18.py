__author__ = 'Dr.S.Gowrishankar'

# Write Pythonic code to compute the end time of a movie by specifying the start time and duration

class Time:
    pass

def add_time(t1, t2):
    movieEndTime = Time()
    movieEndTime.hours = t1.hours + t2.hours
    movieEndTime.minutes = t1.minutes + t2.minutes
    movieEndTime.seconds = t1.seconds + t2.seconds

    while movieEndTime.seconds >= 60:
        movieEndTime.seconds = movieEndTime.seconds - 60
        movieEndTime.minutes = movieEndTime.minutes + 1

    while movieEndTime.minutes >= 60:
        movieEndTime.minutes = movieEndTime.minutes - 60
        movieEndTime.hours = movieEndTime.hours + 1

    return movieEndTime

def print_time(t) :
    # A function to print out a time
    print("%d:%d:%d" % (t.hours, t.minutes, t.seconds ))

start = Time()
start.hours = 9
start.minutes = 14
start.seconds =  30

duration = Time()
duration.hours = 3
duration.minutes = 35
duration.seconds = 0

done = add_time(start, duration)

print_time(done)

