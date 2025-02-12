
import unittest
from app import set_reines, generate_map
class TestNQueens(unittest.TestCase):
    def test_n_queens_4(self):
        expected_solutions = [
            [
                ["#", "R", "#", "#"],
                ["#", "#", "#", "R"],
                ["R", "#", "#", "#"],
                ["#", "#", "R", "#"]
            ],
            [
                ["#", "#", "R", "#"],
                ["R", "#", "#", "#"],
                ["#", "#", "#", "R"],
                ["#", "R", "#", "#"]
            ]
        ]

        solutions = set_reines(4)
        computed_solutions = generate_map(solutions, 4)

        self.assertEqual(computed_solutions, expected_solutions)

if __name__ == "__main__":
    unittest.main()