#!/usr/bin/python
# pylint: disable=invalid-name,too-many-branches
'''Advent of Code 2017 Day 7 solution'''

import unittest

def readday8(filename):
    '''Read data from file'''
    i = []
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip("\n").split(' ')
            if line[1] == 'inc':
                val = int(line[2])
            else:
                val = 0 - int(line[2])

            instruction = [line[0], val, line[4], line[5], int(line[6])]
            i.append(instruction)
    return i

def readreg(registers, register):
    '''See if a register exists. If not, return 0'''
    if register in registers:
        return registers[register]

    return 0

def day8(instr):
    '''Solve Parts 1 and 2'''
    registers = {}
    highest = 0

    for i in instr:
        val = readreg(registers, i[2])
        if i[3] == '>':
            if val > i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        elif i[3] == '<':
            if val < i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        elif i[3] == '>=':
            if val >= i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        elif i[3] == '<=':
            if val <= i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        elif i[3] == '==':
            if val == i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        elif i[3] == '!=':
            if val != i[4]:
                registers[i[0]] = readreg(registers, i[0]) + i[1]
        else:
            raise Exception("Unrecognised comparison %s", i[3])
        if registers and max(registers.values()) > highest:
            highest = max(registers.values())
    return (max(registers.values()), highest)

class TestUM(unittest.TestCase):
    '''Unit tests'''
    def setUp(self):
        self.instructions = readday8('day8test.txt')

    def test_day8(self):
        '''Test both parts'''
        self.assertEqual(day8(self.instructions), (1, 10))

if __name__ == '__main__':
    instructions = readday8('day8.txt')
    print day8(instructions)
