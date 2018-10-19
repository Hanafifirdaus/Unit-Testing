import unittest

def penjumlahanGenap(arr):
    add = 0
    for num in arr:
        if num % 2 == 0:
            add += num
    return add

class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5,9)
    def test2(self):
        self.assertNotEqual(5 * 2,11)
    def test3(self):
        self.assertTrue(4 + 5 == 9,True)
    def test4(self):
        self.assertFalse(4 + 5 == 8,False)
    def test5(self):
        self.assertIn(3,[1,2,3])
    def test6(self):
        self.assertNotIn(10, range(5))
    def test7(self):
        self.assertEqual(penjumlahanGenap([1,2,3,4,5]), 9)


if __name__ == '__main__':
   unittest.main()