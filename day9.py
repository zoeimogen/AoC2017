#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 9 solution'''

import unittest

def recurse(stream, state, i):
    '''Recurse through the stream'''
    while state['ptr'] < len(stream):
        if stream[state['ptr']] == '!':
            state['ptr'] += 2
        elif stream[state['ptr']] == '}':
            state['ptr'] += 1
            state['score'] += i
            return
        elif stream[state['ptr']] == '{':
            state['ptr'] += 1
            recurse(stream, state, i+1)
        elif stream[state['ptr']] == '<':
            state['ptr'] += 1
            while stream[state['ptr']] != '>':
                if stream[state['ptr']] == '!':
                    state['ptr'] += 2
                else:
                    state['ptr'] += 1
                    state['garbage'] += 1
        else:
            state['ptr'] += 1

def day9(i):
    '''Solve Day 9, both parts'''
    state = {}
    state['ptr'] = 0
    state['score'] = 0
    state['garbage'] = 0
    recurse(i, state, 0)
    return (state['score'], state['garbage'])

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day9(self):
        '''Test both parts'''
        self.assertEqual(day9('{}'), (1, 0))
        self.assertEqual(day9('{{{}}}'), (6, 0))
        self.assertEqual(day9('{{},{}}'), (5, 0))
        self.assertEqual(day9('{{{},{},{{}}}}'), (16, 0))
        self.assertEqual(day9('{<a>,<a>,<a>,<a>}'), (1, 4))
        self.assertEqual(day9('{{<ab>},{<ab>},{<ab>},{<ab>}}'), (9, 8))
        self.assertEqual(day9('{{<!!>},{<!!>},{<!!>},{<!!>}}'), (9, 0))
        self.assertEqual(day9('{{<a!>},{<a!>},{<a!>},{<ab>}}'), (3, 17))

if __name__ == '__main__':
    with open('day9.txt', 'r') as f:
        print day9(f.readline().rstrip('\n'))
