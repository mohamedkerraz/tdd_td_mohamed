
import unittest
from app import set_reines, generate_map, init_plateau
class TestNQueens(unittest.TestCase):
    def test_n_queens_4(self):
        """Test avec n=4 """
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

    def test_n_queens_no_solution(self):
        """Test pas de solution trouvé """
        self.assertEqual(set_reines(2), [], "Échec : n=2 devrait renvoyer une liste vide")
        self.assertEqual(set_reines(3), [], "Échec : n=3 devrait renvoyer une liste vide")
        self.assertEqual(init_plateau(2), "no solution, for n = 2", "Échec : n=2 devrait afficher un message d'erreur")
        self.assertEqual(init_plateau(3), "no solution, for n = 3", "Échec : n=3 devrait afficher un message d'erreur")


    def test_invalid_n(self):
        self.assertEqual(init_plateau(-1), "Erreur : n doit être un entier positif", "Échec : n=-1 devrait retourner une erreur")
        self.assertEqual(init_plateau(0), "Erreur : n doit être un entier positif", "Échec : n=0 devrait retourner une erreur")
        self.assertEqual(init_plateau("abc"), "Erreur : n doit être un entier positif", "Échec : n='abc' devrait retourner une erreur")
        self.assertEqual(init_plateau(None), "Erreur : n doit être un entier positif", "Échec : n=None devrait retourner une erreur")



if __name__ == "__main__":
    unittest.main()