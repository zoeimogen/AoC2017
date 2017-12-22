#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 1 solution'''

import unittest

def day1part1(data):
    '''Solve part 1'''
    total = 0

    for i in range(0, len(data)):
        if i >= len(data) - 1:
            nxt = data[0]
        else:
            nxt = data[i+1]
        if int(data[i]) == int(nxt):
            total += int(data[i])
    return total

def day1part2(data):
    '''Solve part 2'''
    total = 0
    diff = len(data) / 2
    for i in range(0, len(data)):
        index = i + diff
        if index >= len(data):
            index = index - len(data)
        nxt = data[index]
        if int(data[i]) == int(nxt):
            total += int(data[i])
    return total

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day1_part1(self):
        '''Test part 1'''
        self.assertEqual(day1part1("1122"), 3)
        self.assertEqual(day1part1("1111"), 4)
        self.assertEqual(day1part1("1234"), 0)
        self.assertEqual(day1part1("91212129"), 9)

    def test_day1_part2(self):
        '''Test part 2'''
        self.assertEqual(day1part2("1212"), 6)
        self.assertEqual(day1part2("1221"), 0)
        self.assertEqual(day1part2("123425"), 4)
        self.assertEqual(day1part2("123123"), 12)
        self.assertEqual(day1part2("12131415"), 4)

if __name__ == '__main__':
    with open("day1.txt", "r") as f:
        problem = f.readline()
        problem = problem.rstrip("\n")
    print day1part1(problem)
    print day1part2(problem)
