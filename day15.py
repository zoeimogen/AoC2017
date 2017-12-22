#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 15 solution'''

import unittest

def generate(value, factor):
    '''Generator function used in part 1'''
    return (value * factor) % 2147483647

def generatepart2(value, factor, mod):
    '''Generator function used in part 2'''
    answer = value
    while True:
        answer = generate(answer, factor)
        if answer % mod == 0:
            return answer

def day15part1(starta, startb):
    '''Solve part 1'''
    matches = 0
    gena = starta
    genb = startb

    for i in range(0, 40000000):
        gena = generate(gena, 16807)
        genb = generate(genb, 48271)
        if (gena & 65535) == (genb & 65535):
            matches += 1

    return matches

def day15part2(starta, startb):
    '''Solve part 2'''
    matches = 0
    gena = starta
    genb = startb

    for i in range(0, 5000000):
        gena = generatepart2(gena, 16807, 4)
        genb = generatepart2(genb, 48271, 8)
        if (gena & 65535) == (genb & 65535):
            matches += 1

    return matches

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day15part1(self):
        '''Test part 1'''
        self.assertEqual(day15part1(65, 8921), 588)

    def test_day15part2(self):
        '''Test part 2'''
        self.assertEqual(day15part2(65, 8921), 309)

if __name__ == '__main__':
    print day15part1(883, 879)
    print day15part2(883, 879)
