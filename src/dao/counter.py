import os

COUNTER_FILENAME = 'counter.dat'
COUNTER_FULLPATH = os.path.dirname(__file__) + '/../data/' + COUNTER_FILENAME

class CounterDAO(object):
    def __init__(self):
        f = open(COUNTER_FULLPATH, 'r')
        self.current = int(f.read())
        f.close()

    def save(self, value):
        f = open(COUNTER_FULLPATH, 'w')
        f.write(str(value))
        f.close()
        self.current = int(value)

    def reset(self):
        self.save(0)

    def get(self):
        return self.current

    def add(self, value):
        self.current = self.current + value
        self.save(self.current)
        return self.current

    def substract(self, value):
        self.current = self.current - value
        if self.current < 0:
            self.reset()
        else:
            self.save(self.current)
        return self.current

    def divide(self, value):
        if value > 0:
            self.current = self.current / value
            self.save(self.current)
        return self.current

    def multiply(self, value):
        self.current = self.current * value
        self.save(self.current)
        return self.current
