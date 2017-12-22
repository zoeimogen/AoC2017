#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 17 solution
   Zoes-MacBook-Pro:advent-of-code zoe$ time python day17.py
   1914
   41797835

   real    1m12.034s
   user    1m9.359s
   sys 0m2.251s
Zoes-MacBook-Pro:advent-of-code zoe$ '''

import unittest
import blist

def day17(step, target):
    '''Solve Day 17'''
    buf = blist.blist([0])
    i = 1
    ptr = 0

    while i <= target:
        ptr += step
        ptr = ptr % len(buf)
        buf.insert(ptr+1, i)
        ptr += 1
        i += 1

    return (buf[1], buf[ptr+1])

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day17(self):
        '''Test part 1'''
        self.assertEqual(day17(3, 2017)[1], 638)

if __name__ == '__main__':
    print day17(343, 2017)[1]
    print day17(343, 50000000)[0]
