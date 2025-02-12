
import unittest
from app import place_reines, convertir_en_grille
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

        solutions = place_reines(4)
        computed_solutions = convertir_en_grille(solutions, 4)

        self.assertEqual(computed_solutions, expected_solutions)

if __name__ == "__main__":
    unittest.main()