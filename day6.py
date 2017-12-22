#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017, Day 6'''

import unittest
import re

def redistribute(problem):
    '''Carry out memory bank redistribution once'''
    idx = problem.index(max(problem))
    i = problem[idx]
    problem[idx] = 0
    while i > 0:
        idx += 1
        if idx >= len(problem):
            idx = 0
        problem[idx] += 1
        i -= 1
    return problem

def day6(problem):
    '''Solve Day 6'''
    sstr = ' '.join(map(str, problem))
    states = []

    while sstr not in states:
        states.append(sstr)
        redistribute(problem)
        sstr = ' '.join(map(str, problem))
    return len(states)

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day6(self):
        '''Test day 6 (Both parts)'''
        problem = [0, 2, 7, 0]
        self.assertEqual(day6(problem), 5)
        self.assertEqual(day6(problem), 4)

if __name__ == '__main__':
    p = []
    with open("day6.txt", "r") as f:
        line = f.readline()
        p = map(int, re.split('\t+', line))

    print day6(p)
    print day6(p)
