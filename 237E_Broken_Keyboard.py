import sys
import unittest
from itertools import tee
import re


def broken_keyboard(key_board, wordlist):
    return max((word for word in wordlist if re.fullmatch("[" + key_board + "]+", word)),
                key=lambda x: len(x))


class BrokenKeyboardTest(unittest.TestCase):

    def setUp(self):
        self.f = open('enable1.txt')
        self.wordList = [word.rstrip('\n') for word in self.f.readlines()]

    def testSimple1(self):
        result = broken_keyboard("abcd", self.wordList)
        self.assertEqual(result, "abaca")

    def testSimple2(self):
        result = broken_keyboard("qwer", self.wordList)
        self.assertEqual(result, "weewee")

    def testSimple3(self):
        result = broken_keyboard("hjklo", self.wordList)
        self.assertEqual(result, "holloo")

    def tearDown(self):
        self.f.close()



if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        with open('enable1.txt') as wordlist:
            no_line = int(file.readline())
            words = (line.rstrip('\n') for line in open('enable1.txt'))
            wordsIters = tee(words, no_line)
            keyboards = (keyboard.rstrip('\n') for keyboard in file.readlines())
            results = ((keyboard, broken_keyboard(keyboard, wordsIters[index]))
                    for index, keyboard in enumerate(keyboards))
            for keyboard, result in results:
                print(keyboard, '==', result if result else "NO MATCH.")
