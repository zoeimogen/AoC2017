#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 16 solution
   The output of this program is used to initalise day16vars.h, needed to compile day16.c
   Zoes-MacBook-Pro:advent-of-code zoe$ python day16.py && cc day16.c -o day16
   Zoes-MacBook-Pro:advent-of-code zoe$ time ./day16
   ceijbfoamgkdnlph
   pnhajoekigcbflmd

   real    2m31.859s
   user    2m27.654s
   sys 0m0.825s
   Zoes-MacBook-Pro:advent-of-code zoe$ 
'''

import string

def day16part1(program, l):
    '''Solve part 1'''
    spun = 0
    exchangemap = range(0, l)
    for p in program:
        if p[0] == 's':
            spun += int(p[1:])
            if spun > l:
                spun -= l
        elif p[0] == 'x':
            xy = p[1:].split('/')
            x = int(xy[0]) - spun
            y = int(xy[1]) - spun
            if x < 0:
                x += l
            if y < 0:
                y += l
            exchangemap[x], exchangemap[y] = exchangemap[y], exchangemap[x]

    return (exchangemap, spun)

def partnermap(program, l):
    '''Create a parnermap from p operations'''
    inp = "abcdefghijklmnop"[:l]
    line = list(inp)
    for p in program:
        if p[0] == 'p':
            xy = p[1:].split('/')
            a = line.index(xy[0])
            b = line.index(xy[1])
            line[a], line[b] = line[b], line[a]
    return string.maketrans(inp, ''.join(line))

if __name__ == '__main__':
    with open("day16.txt", "r") as f:
        prog = f.readline().split(',')
    transmap = partnermap(prog, 16)
    (emap, s) = day16part1(prog, 16)

    with open("day16vars.h", "w") as f:
        f.write("    const char translate[] = \"%s\";\n" % ('abcdefghijklmnop'.translate(transmap)))
        f.write("    const short maparray[] = {%s};\n" % (','.join(map(str, emap))))
        f.write("    const short spin = %d;\n" % s)
