#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 24 solution'''

import unittest

def getvalue(values, v):
    '''Get a value, or return 0 if it doens't exist'''
    if v in values:
        return values[v]

    return 0

def day25(program, steps):
    '''Solve Day 25'''
    values = {}
    ptr = 0
    state = 'A'

    for _ in range(0, steps):
        p = program[state][getvalue(values, ptr)]
        values[ptr], ptr, state = p[0], ptr + p[1], p[2]

    return len([v for v in values if values[v] == 1])

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    program = {'A': {0: [1, 1, 'B'],
                     1: [0, -1, 'B']},
               'B': {0: [1, -1, 'A'],
                     1: [1, 1, 'A']}}

    def test_day24(self):
        '''Run test'''
        self.assertEqual(day25(self.program, 6), 3)

def run():
    '''Run the solution. Hard coded input rather than reading the file, sorry!'''
    program = {'A': {0: (1, 1, 'B'),
                     1: (0, 1, 'F')},
               'B': {0: (0, -1, 'B'),
                     1: (1, -1, 'C')},
               'C': {0: (1, -1, 'D'),
                     1: (0, 1, 'C')},
               'D': {0: (1, -1, 'E'),
                     1: (1, 1, 'A')},
               'E': {0: (1, -1, 'F'),
                     1: (0, -1, 'D')},
               'F': {0: (1, 1, 'A'),
                     1: (0, -1, 'E')}}

    print day25(program, 12964419)

if __name__ == '__main__':
    run()
