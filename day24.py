#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 24 solution'''

import unittest
import copy

def day24(components, last):
    '''Solve Day 24'''
    strongest = 0

    for c in components:
        if c[0] == last:
            components2 = copy.copy(components)
            components2.remove(c)
            strength = day24(components2, c[1])
            if strength + c[0] + c[1] > strongest:
                strongest = strength + c[0] + c[1]
        elif c[1] == last:
            components2 = copy.copy(components)
            components2.remove(c)
            strength = day24(components2, c[0])
            if strength + c[0] + c[1] > strongest:
                strongest = strength + c[0] + c[1]

    return strongest

def day24part2(components, last):
    '''Solve Day 24 Part 2'''
    strongest = 0
    longest = 0

    for c in components:
        if c[0] == last:
            components2 = copy.copy(components)
            components2.remove(c)
            (strength, length) = day24part2(components2, c[1])
            if length + 1 > longest:
                longest = length + 1
                strongest = strength + c[0] + c[1]
            elif length + 1 == longest and strength + c[0] + c[1] > strongest:
                strongest = strength + c[0] + c[1]
        elif c[1] == last:
            components2 = copy.copy(components)
            components2.remove(c)
            (strength, length) = day24part2(components2, c[0])
            if length + 1 > longest:
                longest = length + 1
                strongest = strength + c[0] + c[1]
            elif length + 1 == longest and strength + c[0] + c[1] > strongest:
                strongest = strength + c[0] + c[1]

    return (strongest, longest)

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    components = [(0, 2), (2, 2), (2, 3), (3, 4), (3, 5), (0, 1), (10, 1), (9, 10)]

    def test_day24part1(self):
        '''Run test'''
        self.assertEqual(day24(self.components, 0), 31)

    def test_day24part2(self):
        '''Run test'''
        self.assertEqual(day24part2(self.components, 0)[0], 19)

def run():
    '''Run the solution'''
    components = []
    with open("day24.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            components.append(tuple(map(int, line.split('/'))))

    print day24(components, 0)
    print day24part2(components, 0)[0]

if __name__ == '__main__':
    run()
