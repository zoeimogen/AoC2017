#!/usr/bin/python
# pylint: disable=invalid-name
'''Advent of Code 2017 Day 9 solution'''

import unittest
import re

def validphrase(phrase):
    '''Check for valid phrases using the part 1 definition'''
    words = re.split(' +', phrase)
    return len(set(words)) == len(words)

def validphrasepart2(phrase):
    '''Check for valid phrases usigng the part 2 (anagram) definition'''
    words = re.split(' +', phrase)
    sortedwords = [''.join(sorted(word)) for word in words]
    return len(set(sortedwords)) == len(sortedwords)

def day4part1(problem):
    '''Solve part 1'''
    return [validphrase(phrase) for phrase in problem].count(True)

def day4part2(problem):
    '''Solve part 2'''
    return [validphrasepart2(phrase) for phrase in problem].count(True)

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day4_part1(self):
        '''Test part 1'''
        self.assertEqual(validphrase("aa bb cc dd ee"), True)
        self.assertEqual(validphrase("aa bb cc dd aa"), False)
        self.assertEqual(validphrase("aa bb cc dd aaa"), True)

    def test_day4_part2(self):
        '''Test part 2'''
        self.assertEqual(validphrasepart2("abcde fghij"), True)
        self.assertEqual(validphrasepart2("abcde xyz ecdab"), False)
        self.assertEqual(validphrasepart2("a ab abc abd abf abj"), True)
        self.assertEqual(validphrasepart2("iiii oiii ooii oooi oooo"), True)
        self.assertEqual(validphrasepart2("oiii ioii iioi iiio"), False)

if __name__ == '__main__':
    p = []
    with open("day4.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            p.append(line)

    print day4part1(p)
    print day4part2(p)
