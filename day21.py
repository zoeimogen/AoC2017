#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 21 solution'''
import unittest

def comparegrids(grida, gridb):
    '''Compare 2 grids'''
    for i in range(0, len(grida)):
        if grida[i] != gridb[i]:
            return False
    return True

def enhance(grid, rules):
    '''Apply rules to a 2x2 or 3x3 grid'''
    for r in rules:
        if comparegrids(grid, r[0]):
            return r[1]
    raise Exception("No match for %s", str(grid))

def iterateevens(grid, rules):
    '''Iterate over 2x2 grids'''
    x = 0
    a = 0
    outputgrid = []
    while x < len(grid):
        outputgrid.append('')
        outputgrid.append('')
        outputgrid.append('')
        y = 0
        while y < len(grid[x]):
            g = [grid[x][y:y+2], grid[x+1][y:y+2]]
            g = enhance(g, rules)
            outputgrid[a] = outputgrid[a] + g[0]
            outputgrid[a+1] = outputgrid[a+1] + g[1]
            outputgrid[a+2] = outputgrid[a+2] + g[2]
            y += 2
        x += 2
        a += 3
    return outputgrid

def iterateodds(grid, rules):
    '''Iterate over 3x3 grids'''
    x = 0
    a = 0
    outputgrid = []
    while x < len(grid):
        outputgrid.append('')
        outputgrid.append('')
        outputgrid.append('')
        outputgrid.append('')
        y = 0
        while y < len(grid[x]):
            g = [grid[x][y:y+3], grid[x+1][y:y+3], grid[x+2][y:y+3]]
            g = enhance(g, rules)
            outputgrid[a] = outputgrid[a] + g[0]
            outputgrid[a+1] = outputgrid[a+1] + g[1]
            outputgrid[a+2] = outputgrid[a+2] + g[2]
            outputgrid[a+3] = outputgrid[a+3] + g[3]
            y += 3
        x += 3
        a += 4
    return outputgrid

def iterate(grid, rules):
    '''Select and run appropriate iteration function'''
    if len(grid) % 2:
        return iterateodds(grid, rules['3'])

    return iterateevens(grid, rules['2'])

def readevenrule(rules, left, right):
    '''Read rules for 2x2 squares'''
    rules.append((left, right))
    seen = [left]
    #HFlip
    l = (''.join([left[0][1], left[0][0]]),
         ''.join([left[1][1], left[1][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #VFlip
    l = (''.join([left[1][0], left[1][1]]),
         ''.join([left[0][0], left[0][1]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #180
    l = (''.join([left[1][1], left[1][0]]),
         ''.join([left[0][1], left[0][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #90
    l = (''.join([left[1][0], left[0][0]]),
         ''.join([left[1][1], left[0][1]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #270
    l = (''.join([left[0][1], left[1][1]]),
         ''.join([left[0][0], left[1][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)

def readoddrule(rules, left, right):
    '''Read rules for 3x3 squares'''
    rules.append((left, right))
    seen = [left]
    #HFlip
    l = (''.join([left[0][2], left[0][1], left[0][0]]),
         ''.join([left[1][2], left[1][1], left[1][0]]),
         ''.join([left[2][2], left[2][1], left[2][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #VFlip
    l = (''.join([left[2][0], left[2][1], left[2][2]]),
         ''.join([left[1][0], left[1][1], left[1][2]]),
         ''.join([left[0][0], left[0][1], left[0][2]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #180
    l = (''.join([left[2][2], left[2][1], left[2][0]]),
         ''.join([left[1][2], left[1][1], left[1][0]]),
         ''.join([left[0][2], left[0][1], left[0][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #90
    l = (''.join([left[0][0], left[1][0], left[2][0]]),
         ''.join([left[0][1], left[1][1], left[2][1]]),
         ''.join([left[0][2], left[1][2], left[2][2]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #90 + Flip
    l = (''.join([left[2][0], left[1][0], left[0][0]]),
         ''.join([left[2][1], left[1][1], left[0][1]]),
         ''.join([left[2][2], left[1][2], left[0][2]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #270
    l = (''.join([left[0][2], left[1][2], left[2][2]]),
         ''.join([left[0][1], left[1][1], left[2][1]]),
         ''.join([left[0][0], left[1][0], left[2][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)
    #270 + Flip
    l = (''.join([left[2][2], left[1][2], left[0][2]]),
         ''.join([left[2][1], left[1][1], left[0][1]]),
         ''.join([left[2][0], left[1][0], left[0][0]]))
    if l not in seen:
        rules.append((l, right))
        seen.append(l)

def readrules(line, rules):
    '''Read the rules from the file.'''
    lr = line.split(' => ')
    left = lr[0].split('/')
    right = lr[1].split('/')

    if len(left) == 2:
        readevenrule(rules['2'], left, right)
    else:
        readoddrule(rules['3'], left, right)

def countpixels(grid):
    '''Count the number of #s in the grid'''
    count = 0
    for line in grid:
        for c in line:
            if c == '#':
                count += 1

    return count

class TestUM(unittest.TestCase):
    '''Unit Tests'''

    def test_day21(self):
        '''Run test'''
        rules = {'2': [],
                 '3': []}
        testdata = ['../.# => ##./#../...',
                    '.#./..#/### => #..#/..../..../#..#']
        for l in testdata:
            readrules(l, rules)

        grid = ['.#.', '..#', '###']
        grid = iterate(grid, rules)
        grid = iterate(grid, rules)

        self.assertEqual(countpixels(grid), 12)

def run():
    '''Solve the problem'''
    rules = {'2': [],
             '3': []}
    with open("day21.txt", "r") as f:
        for l in f:
            l = l.rstrip("\n")
            readrules(l, rules)

    grid = ['.#.', '..#', '###']
    for i in range(0, 5):
        grid = iterate(grid, rules)
    print countpixels(grid)

    for i in range(0, 13):
        grid = iterate(grid, rules)
    print countpixels(grid)

if __name__ == '__main__':
    run()
