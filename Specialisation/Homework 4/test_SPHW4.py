from SPHW4 import search_in_matrix
import unittest

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44



class TestSPHW4(unittest.TestCase):

    def test_targetinmatrix(self):
        self.assertEqual(search_in_matrix(matrix, target), [3, 3])

    def test_targetnotinmatrix(self):
        self.assertEqual(search_in_matrix(matrix, 6), [-1, -1])

    def test_targetminus(self):
        input = search_in_matrix(matrix, -6)
        result = [-1, -1]
        self.assertEqual(input, result)



