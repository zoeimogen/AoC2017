#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 13 solution'''

import unittest

def day13part1(data, start):
    '''Solve Day 13 part 1'''
    severity = None

    for i in range(0, len(data)):
        if data[i] is not None:
            if (i+start) % ((data[i]-1)*2) == 0:
                if severity is None:
                    severity = 0
                severity += data[i] * i
    return severity

def day13part2(data):
    '''Solve Day 13 part 2'''
    start = 0

    while day13part1(data, start) is not None:
        start += 1

    return start

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day13part1(self):
        '''Test part 1'''
        testdata = [3, 2, None, None, 4, None, 4]
        self.assertEqual(day13part1(testdata, 0), 24)

    def test_day13part2(self):
        '''Test part 2'''
        testdata = [3, 2, None, None, 4, None, 4]
        self.assertEqual(day13part2(testdata), 10)

if __name__ == '__main__':
    stream = {}
    with open('day13.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split(': ')
            stream[int(line[0])] = int(line[1])

    streamlist = []
    for val in range(0, max(stream.keys())+1):
        if val not in stream:
            streamlist.append(None)
        else:
            streamlist.append(stream[val])

    print day13part1(streamlist, 0)
    print day13part2(streamlist)
