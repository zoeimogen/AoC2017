#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 14 solution
   This is *a* solution. It's very much hacked together and not nice code'''

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

def knothash(string):
    '''Solve day 14 part 1'''
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]
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

    output = 0
    for j in range(0, 16):
        block = stream[j*16:(j+1)*16]
        h = (block[0] ^ block[1] ^ block[2] ^ block[3] ^ block[4] ^ block[5] ^
             block[6] ^ block[7] ^ block[8] ^ block[9] ^ block[10] ^ block[11] ^
             block[12] ^ block[13] ^ block[14] ^ block[15])

        output += bitcount(h)

    return output

def knothash2(string):
    '''Like the other knothash funciton, only returning binary strings'''
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]
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
        h = (block[0] ^ block[1] ^ block[2] ^ block[3] ^ block[4] ^ block[5] ^
             block[6] ^ block[7] ^ block[8] ^ block[9] ^ block[10] ^ block[11] ^
             block[12] ^ block[13] ^ block[14] ^ block[15])

        output = output + ('{0:08b}'.format(h))

    return output

def bitcount(number):
    '''Count bits set in an integer'''
    length = 0
    count = 0
    while number:
        count += (number & 1)
        length += 1
        number >>= 1
    return count

def day14part1(string):
    '''Solve part 1'''
    count = 0
    for i in range(0, 128):
        count += knothash('%s-%d' % (string, i))

    return count

def zerocluster(matrix, x, y):
    '''Zero out a cluster of 1s'''
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]):
        return
    if matrix[x][y] == '1':
        matrix[x][y] = '0'
        zerocluster(matrix, x-1, y)
        zerocluster(matrix, x+1, y)
        zerocluster(matrix, x, y-1)
        zerocluster(matrix, x, y+1)

def countclusters(matrix):
    '''Count clusters in a list of lists of 0s/1s'''
    clusters = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == '1':
                clusters += 1
                zerocluster(matrix, i, j)

    return clusters

def day14part2(string):
    '''Solve Day 14 part 2'''
    matrix = []
    for i in range(0, 128):
        matrix.append(list(knothash2('%s-%d' % (string, i))))
    return countclusters(matrix)

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day14(self):
        '''Test part 1'''
        self.assertEqual(day14part1('flqrgnkx'), 8108)
        self.assertEqual(day14part2('flqrgnkx'), 1242)

if __name__ == '__main__':
    print day14part1('uugsqrei')
    print day14part2('uugsqrei')
