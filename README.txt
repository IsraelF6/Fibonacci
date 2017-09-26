===================
     Fibonacci
===================

Made By: Israel Felhandler

This is a module named fibonacci.py which defines the Fibonacci class. An instance of the Fibonacci class is instantiated with a single integer argument which determines the number of elements of the Fibonacci sequence to calculate. The Fibonacci sequence includes the numbers 0 and 1. Every subsequent term in the sequence is defined as the sum of the two previous terms. For example, the first ten terms of the Fibonacci sequence are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

The Fibonacci class has a get_nums() method which returns a list of the Fibonacci numbers. 

SAMPLE RUN:

>>> from fibonacci import Fibonacci
>>> f = Fibonacci(10)
>>> print f
The first 10 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> f.get_nums()
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 
>>> for item in Fibonacci(8):
... print item,
...
0 1 1 2 3 5 8 13


A generator is defined, fibonacci_gen(), outside of the scope of the Fibonacci class. The generator accepts a single optional integer argument which determines the number of Fibonacci sequence numbers that should be generated. The generarator exhibits the following behavior,

>>> from fibonacci import fibonacci_gen 
>>> for i in fibonacci_gen(12):
...   print i, 
...
0 1 1 2 3 5 8 13 21 34 55 89
