#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 23 solution
   There are no tests for this problem'''

def is_prime(n):
    '''Stolen from StackOverflow:
       https://stackoverflow.com/questions/15285534/isprime-function-for-python-language'''
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

def getreg(r, registers):
    '''Return value of a register (Or zero if uninitalized) or integer'''
    try:
        return int(r)
    except ValueError:
        if r not in registers:
            return 0
        return registers[r]

def day23(prog, registers):
    '''Solve Day 23'''
    ptr = 0
    counter = 0

    while ptr < len(prog):
        p = prog[ptr]
        if p[0] == 'snd':
            registers['sound'] = getreg(p[1], registers)
        elif p[0] == 'set':
            registers[p[1]] = getreg(p[2], registers)
        elif p[0] == 'sub':
            registers[p[1]] = getreg(p[1], registers) - getreg(p[2], registers)
        elif p[0] == 'mul':
            registers[p[1]] = getreg(p[1], registers) * getreg(p[2], registers)
            counter = counter + 1
        elif p[0] == 'jnz':
            if getreg(p[1], registers) != 0:
                ptr = ptr + getreg(p[2], registers) - 1
        elif p[0] == 'prime':
            if not is_prime(registers['b']):
                registers['f'] = 0
        else:
            raise Exception("Invalid instruction")
        ptr = ptr + 1

    return counter

def run():
    '''Run the solution'''
    program = []
    with open("day23.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            program.append(line.split(' '))
    registers = {}
    print day23(program, registers)

    program = []
    # Modified version of the input, with the set e 2...jnz g -13 loop replaced with the more
    # efficient "prime" instruction
    with open("day23modified.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            program.append(line.split(' '))
    registers = {'a': 1}
    day23(program, registers)
    print registers['h']

if __name__ == '__main__':
    run()
