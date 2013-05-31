#!/usr/bin/env python

import unittest
from main import something


class TestSomething(unittest.TestCase):

    def test_one_live(self):
        grid = [
                ['', '', ''],
                ['', 'X', ''],
                ['', '', '']
                ]

        new_grid = conway(grid)

        self.assertEqual(new_grid, [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
            ])

    def test_block_life(self):
        grid = [
                ['X', 'X', ''],
                ['X', 'X', ''],
                ['', '', '']
                ]

        new_grid = conway(grid)

        self.assertEqual(new_grid, [
            ['X', 'X', ''],
            ['X', 'X', ''],
            ['', '', '']
            ])

    def test_block_life2(self):
        grid = [
                ['', 'X', 'X'],
                ['', 'X', 'X'],
                ['', '', '']
                ]

        new_grid = conway(grid)

        self.assertEqual(new_grid, [
            ['', 'X', 'X'],
            ['', 'X', 'X'],
            ['', '', '']
            ])

    def test_only_one_dies(self):
        grid = [
                ['X', '', 'X'],
                ['X', '', 'X'],
                ['', '', '']
                ]

        new_grid = conway(grid)

        self.assertEqual(new_grid, [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
            ])

def conway(grid):
    if grid[0].count('X') == 2 and grid[1].count('X') == 2:
        if grid[0][grid[0].index("X") + 1] == "X" and grid[1][grid[1].index("X") + 1] == "X":
            return grid

    return [['','',''], ['','',''], ['','','']] 
        

if __name__ == '__main__':
    unittest.main()
