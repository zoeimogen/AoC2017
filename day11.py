#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 11 solution'''

import unittest

def day11part1(moves):
    '''Solve day 11 part 1'''
    high = 0
    x = 0
    y = 0
    for m in moves:
        if m == 'ne':
            x += 1
            y += 1
        elif m == 'se':
            x += 1
            y -= 1
        elif m == 's':
            y -= 2
        elif m == 'sw':
            y -= 1
            x -= 1
        elif m == 'nw':
            x -= 1
            y += 1
        elif m == 'n':
            y += 2
        if ((abs(x) + abs(y)) / 2) > high:
            high = ((abs(x) + abs(y)) / 2)
    return ((abs(x) + abs(y)) / 2, high)

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day11(self):
        '''Test both parts'''
        self.assertEqual(day11part1(['ne', 'ne', 'ne']), 3)
        self.assertEqual(day11part1(['ne', 'ne', 'sw', 'sw']), 0)
        self.assertEqual(day11part1(['ne', 'ne', 's', 's']), 2)
        self.assertEqual(day11part1(['se', 'sw', 'se', 'sw', 'sw']), 3)

if __name__ == '__main__':
    with open('day11.txt', 'r') as f:
        line = f.readline().rstrip('\n')
        print day11part1(line.split(','))
