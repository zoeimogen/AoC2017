#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 22 solution'''
import unittest

def readmap(data):
    '''Convert input map m into dict of infected nodes i'''
    infected = {}
    x = 0
    for a in data:
        y = 0
        for b in a:
            if b == '#':
                infected[(x, y)] = True
            y += 1
        x += 1

    return infected

def move(carrier):
    '''Moved carrier'''
    if carrier[2] == 0:
        carrier[0] -= 1
    elif carrier[2] == 1:
        carrier[1] += 1
    elif carrier[2] == 2:
        carrier[0] += 1
    elif carrier[2] == 3:
        carrier[1] -= 1
    else:
        raise Exception("Bad direction")

def iterate(carrier, infected):
    '''Part 1 iteration function'''
    if (carrier[0], carrier[1]) in infected and infected[(carrier[0], carrier[1])]:
        carrier[2] += 1
        if carrier[2] > 3:
            carrier[2] = 0
        infected[(carrier[0], carrier[1])] = False
        move(carrier)
        return False

    carrier[2] -= 1
    if carrier[2] < 0:
        carrier[2] = 3
    infected[(carrier[0], carrier[1])] = True
    move(carrier)
    return True

def iteratepart2(carrier, infected, weakened, flagged):
    '''Part 2 iteration function'''
    if (carrier[0], carrier[1]) in infected and infected[(carrier[0], carrier[1])]:
        # Infected. Turn right
        carrier[2] += 1
        if carrier[2] > 3:
            carrier[2] = 0
        # Change from infected to flagged
        infected[(carrier[0], carrier[1])] = False
        flagged[(carrier[0], carrier[1])] = True
        move(carrier)
        return False

    if (carrier[0], carrier[1]) in weakened and weakened[(carrier[0], carrier[1])]:
        # Weakened, do not turn, change to infected.
        weakened[(carrier[0], carrier[1])] = False
        infected[(carrier[0], carrier[1])] = True
        move(carrier)
        return True

    if (carrier[0], carrier[1]) in flagged and flagged[(carrier[0], carrier[1])]:
        # Flagged. U-Turn
        carrier[2] = (carrier[2] + 2) % 4
        # Change from flagged to clean
        flagged[(carrier[0], carrier[1])] = False
        move(carrier)
        return False

    # Clean. Turn left, make weakened
    carrier[2] -= 1
    if carrier[2] < 0:
        carrier[2] = 3
    weakened[(carrier[0], carrier[1])] = True
    move(carrier)
    return False

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day22part1(self):
        '''Test part 1'''
        testdata = ['.........',
                    '.........',
                    '.........',
                    '.....#...',
                    '...#.....',
                    '.........',
                    '.........',
                    '.........']
        infected = readmap(testdata)
        carrier = [int(len(testdata)/2), int(len(testdata[0])/2), 0]
        count = 0
        for i in range(0, 70):
            if iterate(carrier, infected):
                count += 1
        self.assertEqual(count, 41)
        for i in range(70, 10000):
            if iterate(carrier, infected):
                count += 1
        self.assertEqual(count, 5587)

    def test_day22part2(self):
        '''Test part 2'''
        testdata = ['.........',
                    '.........',
                    '.........',
                    '.....#...',
                    '...#.....',
                    '.........',
                    '.........',
                    '.........']
        infected = readmap(testdata)
        weakened = {}
        f = {}
        carrier = [int(len(testdata)/2), int(len(testdata[0])/2), 0]
        count = 0
        for i in range(0, 100):
            if iteratepart2(carrier, infected, weakened, f):
                count += 1
        self.assertEqual(count, 26)
        for i in range(100, 10000000):
            if iteratepart2(carrier, infected, weakened, f):
                count += 1
        self.assertEqual(count, 2511944)

def run():
    '''Solve the problem'''
    with open("day22.txt", "r") as data:
        infected = readmap(data)
    carrier = [12, 12, 0]
    count = 0
    for i in range(0, 10000):
        if iterate(carrier, infected):
            count += 1
    print count

    with open("day22.txt", "r") as data:
        infected = readmap(data)
    weakened = {}
    flagged = {}
    carrier = [12, 12, 0]
    count = 0
    for i in range(0, 10000000):
        if iteratepart2(carrier, infected, weakened, flagged):
            count += 1
    print count

if __name__ == '__main__':
    run()
