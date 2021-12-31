from unittest import mock
from unittest import TestCase
from models.board import Board
from models.constants import Outputs, Exceptions


class TestBoard(TestCase):
    def test_check_result(self):
        grids = [
            ["X","O","X","X","X","O","X","O","O"],
            ["X","O","X","O","X","O","X","O","O"],
            ["X","O","X","X","X","O","O","O","O"],
            ["X","O","X","X","O","O","X","O","O"],
            ["X","O","X","O","O","X","X","X","O"],
            ["X","O","X","X","O","O","O","X","X"]
        ]
        expected_results = [
            "X","X","O","X", None, None
        ]
        for index in range(len(grids)):
            board = Board()
            board.grid = grids[index]
            result = board.check_result()
            self.assertEqual(result, expected_results[index])

