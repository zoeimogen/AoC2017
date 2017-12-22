#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 5 solution'''

import unittest

def day5part1(problem):
    '''Solve part 1'''
    p = list(problem)
    ptr = 0
    count = 0

    while ptr >= 0 and ptr < len(p):
        newptr = ptr + p[ptr]
        p[ptr] += 1
        ptr = newptr
        count += 1
    return count

def day5part2(problem):
    '''Solve part 2'''
    p = list(problem)
    ptr = 0
    count = 0

    while ptr >= 0 and ptr < len(p):
        newptr = ptr + p[ptr]
        if p[ptr] >= 3:
            p[ptr] -= 1
        else:
            p[ptr] += 1
        ptr = newptr
        count += 1
    return count

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day5_part1(self):
        '''Test Part 1'''
        self.assertEqual(day5part1([0, 3, 0, 1, -3]), 5)

    def test_day5_part2(self):
        '''Test Part 2'''
        self.assertEqual(day5part2([0, 3, 0, 1, -3]), 10)

if __name__ == '__main__':
    data = []
    with open("day5.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            data.append(int(line))

    print day5part1(data)
    print day5part2(data)
