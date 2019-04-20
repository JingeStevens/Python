#!/usr/bin/python

"""
Object Oriented Programming and Python Classes
"""

"""
QUESTION 1: 
========================================================================================================
Write a class with name WindowAverage which is initialized by a window size and returns an average of
a stream of integers over a window by calling a method next.

The method next should take in a real number and return the average of that number and the previous window-size numbers. 

Example:
===========================
    w = WindowAverage(2)
    w.next(2) = 2
    w.next(4) = (2+4)/2
    w.next(3) = (4+3)/2
    w.next(2) = (2+3)/2
    
Hints: You should have __init__ and next methods and can use a data structure - double-ended queue
from collections module.    
"""
from collections import deque

class WindowAverage:
    def __init__(self, window_size: float):
        try:
            window_size = float(window_size)
        except ValueError as e:
            print(e)
            return

        self._size_deque = deque()
        self._size_deque.append(window_size)

    def next(self, new_size):
        try:
            new_size = float(new_size)
        except ValueError as e:
            print(e)
            return

        self._size_deque.append(new_size)
        pre_size = self._size_deque.popleft()
        return (pre_size + new_size) / 2
"""
QUESTION 2: 
========================================================================================================
Write a class with name AlternateIterator which is initialized by two lists v1 and v2
and returns the elements alternatively every time a method next is called and stops
iteration when both lists are exhausted.

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 4, 2, 5, 3, 6, 7]
 
    Usage:
    iter = AlternateIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

Hints: You should have three methods: __init__, next, and has_next. 
"""


class AlternateIterator:
    def __init__(self, v1: list, v2: list):
        if not (isinstance(v1, list) and isinstance(v2, list)):
            return


        self._deque = deque()  # 一个双端队列用来存储值
        self._source_deque = deque()  # 另一个用来存储来自v1 还是v2
        for i in range(max(len(v1), len(v2))):
            try:
                temp1 = v1[i]
                self._deque.append(temp1)
                self._source_deque.append(1)
            except IndexError:   # 当v1短于v2时，会发生数组访问越界
                pass

            try:
                temp2 = v2[i]
                self._deque.append(temp2)
                self._source_deque.append(2)
            except IndexError:
                pass

    def has_next(self):
        return len(self._deque) > 0  # 只要双端队列中还有值

    def next(self):
        return self._deque.popleft()


"""
QUESTION 3:
========================================================================================================
Write a class ModifiedIterator that inherits the class AlternateIterator you wrote in Q2 that overwrites
the method next so that it return twice of the value from l2.

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 8, 2, 10, 3, 12, 14]
    
    Usage:
    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())
"""


class ModifiedIterator(AlternateIterator):
    def next(self):
        try:
            source = self._source_deque.popleft()
            value = self._deque.popleft()
        except IndexError:
            return

        if source == 1:
            return value
        elif source == 2:
            return 2 * value


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]

    # Question 1 test
    print("Question 1 Test")
    w = WindowAverage(2)
    print(w.next(2))
    print(w.next(4))
    print(w.next(3))
    print(w.next(2))

    print()
    print("Question 2 Test")
    res = []
    iter = AlternateIterator(l1, l2)
    while iter.has_next():
        res.append(iter.next())
    print(res)

    print()
    print("Question 3 Test")
    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())
    print(res)

