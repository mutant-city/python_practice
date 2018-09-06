import unittest
import random
from solution import *

class TestCase(unittest.TestCase):

    def test_int2base(self):
        b10 = int2base(53, 10, 'i')
        b9  = int2base(53, 9, 'i')
        b8  = int2base(53, 8, 'i')
        b7  = int2base(53, 7, 'i')
        b6  = int2base(53, 6, 'i')
        b5  = int2base(53, 5, 'i')
        b4  = int2base(53, 4, 'i')
        b3  = int2base(53, 3, 'i')
        b2  = int2base(53, 2, 'i')
        self.assertTrue(b10 == 53)
        self.assertTrue(b9 == 58)
        self.assertTrue(b8 == 65)
        self.assertTrue(b7 == 104)
        self.assertTrue(b6 == 125)
        self.assertTrue(b5 == 203)
        self.assertTrue(b4 == 311)
        self.assertTrue(b3 == 1222)
        self.assertTrue(b2 == 110101)


    def test_getNext(self):
        r = getNext('1211', 10)
        self.assertTrue(r == '0999')
        r = getNext('0999', 10)
        self.assertTrue(r == '8991')
        r = getNext('8082', 10)
        self.assertTrue(r == '8532')
        r = getNext('8532', 10)
        self.assertTrue(r == '6174')
        r = getNext('6174', 10)
        self.assertTrue(r == '6174')
        r = getNext('210111', 3)
        self.assertTrue(r == '122221')
        r = getNext('122221',3)
        self.assertTrue(r == '102212')
        r = getNext('102212', 3)
        self.assertTrue(r == '210111')
    
    def test_hasEndCycle(self):
        list = self.getRandomList() + [3,2,1,3,2,1]
        r = hasEndCycle(list, 3)
        self.assertTrue(r == 2)
        list = self.getRandomList() + ['333',22,1,0,'333',22,1,0]
        r = hasEndCycle(list, 3)
        self.assertTrue(r == 0)
        list = self.getRandomList() + ['333',2,1,0,'333',2,1,0]
        r = hasEndCycle(list, 4)
        self.assertTrue(r == 2)
        list = self.getRandomList() + [1,1,1,1,1]
        r = hasEndCycle(list, 1)
        self.assertTrue(r == 5)

    def test_findSmallestWindowSize(self):
        list = self.getRandomList() + [3,2,1,3,2,1,3,2,1,3,2,1]
        r = findSmallestWindowSize(list)
        self.assertTrue(r == 3)
        list = self.getRandomList() + ['333',22,1,0,'333',22,1,0]
        r = findSmallestWindowSize(list)
        self.assertTrue(r == 4)
        list = self.getRandomList() + ['x', '333',22343423,11100,0,'x', '333',22343423,11100,0]
        r = findSmallestWindowSize(list)
        self.assertTrue(r == 5)
        list = self.getRandomList() + [1,1,1,1,1]
        r = findSmallestWindowSize(list)
        self.assertTrue(r == 1)
        list = self.getRandomList() + [1,2,1,2,1,2,1,2,1,2]
        r = findSmallestWindowSize(list)
        self.assertTrue(r == 2)

    def getRandomList(self):
        x = random.randint(0,100)
        out = []
        for i in range(x):
            out.append(random.randint(0,100))
        return out

if __name__ == '__main__':
    unittest.main()