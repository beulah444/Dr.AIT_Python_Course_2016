#Write Pythonic code to increment a given time with few seconds

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        # A function to print out a time
        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))

    def increment(self, seconds):
        self.seconds = seconds + self.seconds

        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1

        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1

        return self

start = Time(9, 45, 00)
start.print_time()

end = start.increment(1337)
end.print_time()

