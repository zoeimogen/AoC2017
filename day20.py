#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 20 solution'''
import re
import operator
import copy
import unittest

def day20(data):
    '''Solve part 1'''
    for j in range(0, 500): # 500, by observation, is sufficient
        sh = None
        for i in range(0, len(data)):
            p = data[i]['p']
            h = abs(p[0]) + abs(p[1]) + abs(p[2])
            if sh is None or h < sh[1]:
                sh = (i, h)
            data[i]['p'] = tuple(map(operator.add, data[i]['p'], data[i]['v']))
            data[i]['v'] = tuple(map(operator.add, data[i]['v'], data[i]['a']))

    return sh[0]

def day20part2(data):
    '''Solve part 2'''
    cycles = 0
    for j in range(0, 100): # 100, by observation, is sufficient
        sh = None
        seen = set()
        deletes = set()
        cycles += 1
        for i in range(0, len(data)):
            p = data[i]['p']
            h = abs(p[0]) + abs(p[1]) + abs(p[2])
            if sh is None or h < sh[1]:
                sh = (i, h)
            data[i]['v'] = tuple(map(operator.add, data[i]['v'], data[i]['a']))
            data[i]['p'] = tuple(map(operator.add, data[i]['p'], data[i]['v']))
            if data[i]['p'] in seen:
                deletes.add(i)
                deletes.add([d['p'] for d in data].index(data[i]['p']))
            seen.add(data[i]['p'])
        for i in sorted(deletes, reverse=True):
            del data[i]
    return len(data)

def readparticle(data):
    '''Read particle data'''
    pattern = ('p=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
               'v=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
               'a=<([-0-9]+),([-0-9]+),([-0-9]+)>')
    d = []
    for line in data:
        v = map(int, re.search(pattern, line).groups())
        d.append({'p': (v[0], v[1], v[2]), 'v': (v[3], v[4], v[5]), 'a': (v[6], v[7], v[8])})

    return d

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day21(self):
        '''Run test'''
        testdata = ['p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>'
                    'p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>'
                    'p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>'
                    'p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>']
        d = readparticle(testdata)
        self.assertEqual(day20(d), 0)

def run():
    '''Solve the problem'''
    with open("day20.txt", "r") as f:
        d = readparticle(f)
    d2 = copy.deepcopy(d)
    print day20(d)
    print day20part2(d2)

if __name__ == '__main__':
    run()
