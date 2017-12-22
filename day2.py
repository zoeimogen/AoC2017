#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 2 solution'''

import unittest
import re

def day2part1(data):
    '''Solve part 1'''
    return sum([max(i) - min(i) for i in data])

def getdivision(data):
    '''Find evenly divisible entries'''
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if i != j:
                if data[i] % data[j] == 0:
                    return data[i] / data[j]
    raise Exception("Failed to find entires to divide")

def day2part2(data):
    '''Solve part 2'''
    return sum([getdivision(i) for i in data])

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day2_part1(self):
        '''Test part 1'''
        testdata = [[5, 1, 9, 5],
                    [7, 5, 3],
                    [2, 4, 6, 8]]
        self.assertEqual(day2part1(testdata), 18)

    def test_day2_part2(self):
        '''Test part 2'''
        testdata = [[5, 9, 2, 8],
                    [9, 4, 7, 3],
                    [3, 8, 6, 5]]
        self.assertEqual(day2part2(testdata), 9)

if __name__ == '__main__':
    problem = []
    with open("day2.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            problem.append(map(int, re.split(' +', line)))

    print day2part1(problem)
    print day2part2(problem)
