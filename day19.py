#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 18 solution'''
import unittest

def move(location, direction):
    '''Move!'''
    if direction == 0:
        return (location[0], location[1] - 1)
    elif direction == 1:
        return (location[0]+1, location[1])
    elif direction == 2:
        return (location[0], location[1] + 1)
    elif direction == 3:
        return (location[0]-1, location[1])
    raise Exception("Bad direction")

def change(location, diagram, direction):
    '''Figure out which weay we should turn'''
    if direction == 0 or direction == 2:
        if diagram[location[0]+1][location[1]] in '|ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 1
        elif diagram[location[0]-1][location[1]] in '|ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 3
        raise Exception("Can't turn N/S")
    elif direction == 1 or direction == 3:
        if diagram[location[0]][location[1]-1] in '-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 0
        elif diagram[location[0]][location[1]+1] in '-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 2
        raise Exception("Can't turn E/W")
    raise Exception("Bad direction in turn")

def day19(diagram):
    '''Walk the diagram'''
    location = (0, diagram[0].index('|'))
    direction = 1
    letters = ''
    steps = 0

    while True:
        letter = diagram[location[0]][location[1]]
        if letter == '|' or letter == '-':
            location = move(location, direction)
        elif letter == '+':
            direction = change(location, diagram, direction)
            location = move(location, direction)
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letters = letters + letter
            location = move(location, direction)
        else:
            return (letters, steps)
        steps += 1

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day18(self):
        '''Test part 1'''
        diagram = ['     |          ',
                   '     |  +--+    ',
                   '     A  |  C    ',
                   ' F---|----E|--+ ',
                   '     |  |  |  D ',
                   '     +B-+  +--+ ',
                   '                ']

        self.assertEqual(day19(diagram), ('ABCDEF', 38))

if __name__ == '__main__':
    d = []
    with open("day19.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            d.append(line)
    print day19(d)
