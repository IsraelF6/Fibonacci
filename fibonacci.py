"""Israel Felhandler"""
"""IF12B"""
"""CIS4930 - Python"""
"""Summer 2017"""

class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.values = []
        
        self.a = 0
        self.b = 1
        self.c = 0
        self.counter = 0

        #Start the sequence and append to list
        for i in range(0, n):
            temp = self.b
            self.b += self.a
            self.values.append(self.a)
            self.a = temp
        self.a = 0
        self.b = 1 
        self.c = 0

    def __iter__(self):
        return self

    def next(self):
        if self.counter < self.n:
            val = self.a 
            self.c = self.b
            self.b += self.a
            self.a = self.c
            self.counter += 1
            return val
        else:
            raise StopIteration

    def get_nums(self):
        print str(self.values)

    def __str__(self):
        return "The first " + str(self.n) + " Fibonacci numbers are " + str(self.values) 

def fibonacci_gen(n):
    a = 0
    b = 1
    for i in range(0, n):
        yield a
        temp = a + b
        a = b
        b = temp