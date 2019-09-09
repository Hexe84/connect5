import unittest
import numpy as np
import Connect5 as c5


class TestConnect5(unittest.TestCase):

    
    
    def test_find_empty_row(self):
        testGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 2, 2, 2, 0, 2, 1, 0, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 2, 2, 1, 1, 2]]
        self.assertEqual(c5.find_empty_row(testgrid, 5), 3, "Should be 3")

        
    def test_is_winning_horizontal(self):
        testGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 2, 2, 2, 2, 2, 1, 0, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 2, 2, 1, 1, 2]]
        self.assertEqual(c5.is_winning(testGrid, 2), True, "Should be True")
        
    def test_is_winning_vertical(self):
        testGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 2, 2, 2, 0, 2, 1, 0, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 2, 2, 1, 1, 2]]
        self.assertEqual(c5.is_winning(testGrid, 1), True, "Should be True")
    
    def test_is_winning_diagonal_negative(self):
        testGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0],[2, 1, 2, 2, 0, 2, 1, 0, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 1, 2, 1, 1, 2]]
        self.assertEqual(c5.is_winning(testGrid, 1), True, "Should be True")
        
    def test_is_winning_diagonal_positive(self):
        testGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 1, 0, 0, 0, 0],[2, 1, 2, 1, 0, 2, 1, 0, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 1, 2, 2, 2, 2, 1, 2, 1],[1, 2, 1, 1, 1, 2, 1, 1, 2]]
        self.assertEqual(c5.is_winning(testGrid, 1), True, "Should be True")
        
    def test_is_full(self):
        testGrid = [[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 2, 2, 1, 1, 2],[1, 2, 2, 2, 1, 2, 1, 1, 2],
        [1, 2, 1, 2, 2, 2, 1, 1, 1],[1, 2, 1, 1, 2, 2, 1, 2, 1],[1, 2, 1, 1, 2, 2, 1, 1, 2]]
        self.assertEqual(c5.is_full(testGrid), True, "Should be True")
    
    
if __name__ == '__main__':

    import doctest
        
    unittest.main()
    doctest.testmod()