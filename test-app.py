
import unittest
from app import set_reines, generate_map, init_plateau, checkIf_attack
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
        """Test input invalides"""
        self.assertEqual(init_plateau(-1), "Erreur : n doit être un entier positif", "Échec : n=-1 devrait retourner une erreur")
        self.assertEqual(init_plateau(0), "Erreur : n doit être un entier positif", "Échec : n=0 devrait retourner une erreur")
        self.assertEqual(init_plateau("abc"), "Erreur : n doit être un entier positif", "Échec : n='abc' devrait retourner une erreur")
        self.assertEqual(init_plateau(None), "Erreur : n doit être un entier positif", "Échec : n=None devrait retourner une erreur")

    def test_n_float(self):
        """Test avec n = 4.5 (non convertible en entier valide)"""
        self.assertEqual(init_plateau(4.5), "Erreur : n doit être un entier positif", "Échec : n=4.5 devrait lever une erreur")

    def test_n_queens_8(self):
        """Test avec n=8 (test de performance)"""
        solutions = set_reines(8)
        self.assertGreater(len(solutions), 0, "Échec : n=8 devrait avoir des solutions")

    def test_checkIf_attack(self):
        """Test la fonction checkIf_attack pour différents cas"""
        plateau = [0, 2, -1, -1]  # Plateau partiel pour un échiquier de 4x4

        self.assertFalse(checkIf_attack(plateau, 2, 0))
        self.assertFalse(checkIf_attack(plateau, 2, 3))
        self.assertFalse(checkIf_attack(plateau, 2, 1))
        self.assertTrue(checkIf_attack(plateau, 3, 1))

    def test_(self):
        """Test la fonction checkIf_attack pour différents cas"""
        plateau = [0, 2, -1, -1]  # Plateau partiel pour un échiquier de 4x4

        self.assertFalse(checkIf_attack(plateau, 2, 0))
        self.assertFalse(checkIf_attack(plateau, 2, 3))
        self.assertFalse(checkIf_attack(plateau, 2, 1))
        self.assertTrue(checkIf_attack(plateau, 3, 1))



if __name__ == "__main__":
    unittest.main()