#!/usr/bin/python
# pylint: disable=invalid-name,redefined-outer-name
'''Advent of Code 2017 Day 7 solution'''

import unittest

def readday7(filename, weights, parents, offspring):
    '''Read data from file'''
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip("\n").split(' ', 3)
            parent = line[0]
            weights[parent] = int(line[1].lstrip('(').rstrip(')'))
            if len(line) > 3:
                children = line[3].split(' ')
                offspring[parent] = []
                for c in children:
                    c = c.rstrip(',')
                    parents[c] = parent
                    offspring[parent].append(c)

def day7part1(weights, parents):
    '''Solve Part 1'''
    nodes = [n for n in weights]
    top = [n for n in nodes if n not in parents]
    assert len(top) == 1
    return top[0]

def day7part2(weights, children, top):
    '''Solve Part 2 (Requires output of part 1)'''
    weight = 0
    if top in children:
        w = {}
        for c in children[top]:
            w[c] = day7part2(weights, children, c)
            if w[c] < 0:
                return w[c]
            weight += w[c]
        if len(set(w.values())) != 1:
            mismatch = [a for a in w.values() if w.values().count(a) == 1][0]
            correct = [a for a in w.values() if w.values().count(a) != 1][0]
            diff = correct - mismatch
            mismatchedkey = w.keys()[w.values().index(mismatch)]
            return 0 - (weights[mismatchedkey] + diff)
    return weight + weights[top]

class TestUM(unittest.TestCase):
    '''Unit tests'''
    def setUp(self):
        self.weights = {}
        self.parents = {}
        self.children = {}
        readday7('day7test.txt', self.weights, self.parents, self.children)

    def test_day7(self):
        '''Test both parts'''
        top = day7part1(self.weights, self.parents)
        self.assertEqual(top, 'tknk')
        self.assertEqual(day7part2(self.weights, self.children, top), -60)

if __name__ == '__main__':
    weights = {}
    parents = {}
    children = {}
    readday7('day7.txt', weights, parents, children)
    top = day7part1(weights, parents)
    print top
    print 0 - day7part2(weights, children, top)
