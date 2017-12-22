#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 3 solution'''

import unittest
import numpy

def day3part1(number):
    '''Solve part 1'''
    if number == 1:
        return 0
    total = 2
    i = 1
    while True:
        if number < total + i*8:
            side = int((number-total)/(i*2))
            perside = i*2
            midpoint = total+(perside*(side+0.5))-1
            return int(i + abs(number-midpoint))
        total += i * 8
        i += 1

def day3part2(number):
    '''Solve part 2'''
    grid = numpy.empty((99, 99))
    grid.fill(0)
    x = 49
    y = 49
    direction = 3
    value = 1
    while value <= number:
        grid[x][y] = value
        if direction == 0:
            if grid[x-1][y] == 0:
                direction = 1
                x = x - 1
            else:
                y = y + 1
        elif direction == 1:
            if grid[x][y-1] == 0:
                direction = 2
                y = y - 1
            else:
                x = x - 1
        elif direction == 2:
            if grid[x+1][y] == 0:
                direction = 3
                x = x + 1
            else:
                y = y - 1
        else:
            if grid[x][y+1] == 0:
                direction = 0
                y = y + 1
            else:
                x = x + 1
        value = sum([grid[x-1][y-1],
                     grid[x][y-1],
                     grid[x+1][y-1],
                     grid[x+1][y],
                     grid[x+1][y+1],
                     grid[x][y+1],
                     grid[x-1][y+1],
                     grid[x-1][y]])
    return int(value)


class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day3_part1(self):
        '''Test part 1'''
        self.assertEqual(day3part1(1), 0)
        self.assertEqual(day3part1(12), 3)
        self.assertEqual(day3part1(23), 2)
        self.assertEqual(day3part1(1024), 31)

    def test_day3_part2(self):
        '''Test part 2'''
        self.assertEqual(day3part2(361), 362)
        self.assertEqual(day3part2(362), 747)
        self.assertEqual(day3part2(363), 747)
        self.assertEqual(day3part2(748), 806)

if __name__ == '__main__':
    problem = []
    with open("day3.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            problem = int(line)

    print day3part1(problem)
    print day3part2(problem)
