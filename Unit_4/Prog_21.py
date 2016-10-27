__author__ = 'Dr.S.Gowrishankar'

class Time:
    pass

def print_time(t):
    # A function to print out a time
    print("%d:%d:%d" % (t.hours, t.minutes, t.seconds))

def time_to_int(time):
    minutes = time.hours * 60 + time.minutes
    seconds = minutes * 60 + time.seconds
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)
    time.hours, time.minutes = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

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

