#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 12 solution'''

import unittest

def countnodes(graph, i, seen):
    '''Code nodes in graph'''
    total = 1 # Count this node too
    seen.append(i)

    for j in graph[i]:
        if j not in seen:
            total += countnodes(graph, j, seen)

    del graph[i]
    return total

def day12(data):
    '''Solve Day 12'''
    graph = {}
    for d in data:
        values = d.split(' ')
        i = int(values[0])
        g = []
        for j in values[2:]:
            j = j.rstrip(',')
            g.append(int(j))
        graph[i] = g

    part1 = countnodes(graph, 0, [])
    count = 1
    while graph:
        count += 1
        n = graph.keys()[0]
        countnodes(graph, n, [])

    return (part1, count)

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day12(self):
        '''Test both parts'''
        testdata = ['0 <-> 2', '1 <-> 1', '2 <-> 0, 3, 4', '3 <-> 2, 4',
                    '4 <-> 2, 3, 6', '5 <-> 6', '6 <-> 4, 5']
        self.assertEqual(day12(testdata), (6, 2))

if __name__ == '__main__':
    stream = []
    with open('day12.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            stream.append(line)

    print day12(stream)
