#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 18 solution'''
import unittest

def getreg(r, registers):
    '''Return value of a register (Or zero if uninitalized) or integer'''
    try:
        return int(r)
    except ValueError:
        if r not in registers:
            return 0
        return registers[r]

def day18(prog):
    '''Solve Day 18 part 1'''
    registers = {}
    ptr = 0

    while True:
        p = prog[ptr]
        if ptr >= len(prog):
            raise Exception("End of program")
        if p[0] == 'snd':
            registers['sound'] = getreg(p[1], registers)
        elif p[0] == 'set':
            registers[p[1]] = getreg(p[2], registers)
        elif p[0] == 'add':
            registers[p[1]] = getreg(p[1], registers) + getreg(p[2], registers)
        elif p[0] == 'mul':
            registers[p[1]] = getreg(p[1], registers) * getreg(p[2], registers)
        elif p[0] == 'mod':
            registers[p[1]] = getreg(p[1], registers) % getreg(p[2], registers)
        elif p[0] == 'rcv':
            if getreg(p[1], registers) != 0:
                return registers['sound']
        elif p[0] == 'jgz':
            if getreg(p[1], registers) > 0:
                ptr = ptr + getreg(p[2], registers) - 1
        else:
            raise Exception("Invalid instruction")
        ptr = ptr + 1

def getreg2(r, pid, registers):
    '''Return value of a register (Or zero if uninitalized) or integer'''
    try:
        return int(r)
    except ValueError:
        if r not in registers[pid]:
            return 0
        return registers[pid][r]

def day18part2(prog):
    '''Solve Day 18 part 2'''
    registers = [{'p': 0}, {'p': 1}]
    queue = [[], []]
    ptr = [0, 0]
    pid = 0
    count = [0, 0]

    while True:
        p = prog[ptr[pid]]
        if ptr[pid] >= len(prog):
            raise Exception("End of program")
        if p[0] == 'snd':
            queue[(pid + 1) % 2].insert(0, getreg2(p[1], pid, registers))
            count[pid] += 1
        elif p[0] == 'set':
            registers[pid][p[1]] = getreg2(p[2], pid, registers)
        elif p[0] == 'add':
            registers[pid][p[1]] = getreg2(p[1], pid, registers) + getreg2(p[2], pid, registers)
        elif p[0] == 'mul':
            registers[pid][p[1]] = getreg2(p[1], pid, registers) * getreg2(p[2], pid, registers)
        elif p[0] == 'mod':
            registers[pid][p[1]] = getreg2(p[1], pid, registers) % getreg2(p[2], pid, registers)
        elif p[0] == 'rcv':
            if not queue[pid]:
                pid = (pid + 1) % 2
                if not queue[pid]:
                    return count[1]
                ptr[pid] = ptr[pid] - 1
            else:
                registers[pid][p[1]] = queue[pid].pop()
        elif p[0] == 'jgz':
            if getreg2(p[1], pid, registers) > 0:
                ptr[pid] = ptr[pid] + getreg2(p[2], pid, registers) - 1
        else:
            raise Exception("Invalid instruction")
        ptr[pid] += 1

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day18(self):
        '''Test part 1'''
        prog = [['set', 'a', '1'],
                ['add', 'a', '2'],
                ['mul', 'a', 'a'],
                ['mod', 'a', '5'],
                ['snd', 'a'],
                ['set', 'a', '0'],
                ['rcv', 'a'],
                ['jgz', 'a', '-1'],
                ['set', 'a', '1'],
                ['jgz', 'a', '-2']]
        self.assertEqual(day18(prog), 4)

    def test_day18part2(self):
        '''Test part 2'''
        prog = [['snd', '1'],
                ['snd', '2'],
                ['snd', 'p'],
                ['rcv', 'a'],
                ['rcv', 'b'],
                ['rcv', 'c'],
                ['rcv', 'd']]
        self.assertEqual(day18part2(prog), 3)

if __name__ == '__main__':
    program = []
    with open("day18.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            program.append(line.split(' '))
    print day18(program)
    print day18part2(program)
