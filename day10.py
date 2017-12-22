#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 10 solution'''

import unittest

def reverse(stream, ptr, length):
    '''Reverse length items in the list stream'''
    if length == 1:
        return

    replace = []
    p = ptr + length - 1
    if p >= len(stream):
        p -= len(stream)
    i = 0

    while i < length:
        replace.append(stream[p])
        p -= 1
        if p < 0:
            p = len(stream) - 1
        i += 1

    p = ptr
    i = 0

    while i < length:
        stream[p] = replace[i]
        p += 1
        if p >= len(stream):
            p = 0
        i += 1

def day10part1(lengths, streamlength):
    '''Solve day 10 part 1'''
    stream = range(0, streamlength)
    ptr = 0
    skip = 0

    for l in lengths:
        reverse(stream, ptr, l)
        ptr += l + skip
        while ptr >= len(stream):
            ptr -= len(stream)
        skip += 1

    return stream[0] * stream[1]

def day10part2(lengths):
    '''Solve day 10 part 2'''
    stream = range(0, 256)
    ptr = 0
    skip = 0

    for j in range(0, 64):
        for l in lengths:
            reverse(stream, ptr, l)
            ptr += l + skip
            while ptr >= len(stream):
                ptr -= len(stream)
            skip += 1

    output = ''
    for j in range(0, 16):
        block = stream[j*16:(j+1)*16]
        print block
        h = (block[0] ^ block[1] ^ block[2] ^ block[3] ^ block[4] ^ block[5] ^
             block[6] ^ block[7] ^ block[8] ^ block[9] ^ block[10] ^ block[11] ^
             block[12] ^ block[13] ^ block[14] ^ block[15])
        output = output + '%02x' % (h)

    return output

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day10(self):
        '''Test part 1'''
        self.assertEqual(day10part1([3, 4, 1, 5], 5), 12)

if __name__ == '__main__':
    with open('day10.txt', 'r') as f:
        line = f.readline().rstrip('\n')
        print day10part1(map(int, line.split(',')), 256)
        part2input = [ord(c) for c in line]
        part2input = part2input + [17, 31, 73, 47, 23]
        print day10part2(part2input)
