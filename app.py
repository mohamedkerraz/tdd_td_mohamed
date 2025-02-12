def set_reines(n):
    def checkIf_attack(plateau, ligne, col):
        
        for i in range(ligne):
            if plateau[i] == col or \
               plateau[i] - i == col - ligne or \
               plateau[i] + i == col + ligne:
                return False
        return True

    def process_resolve(plateau, ligne, solutions):
        
        if ligne == n:
            solutions.append(plateau[:])
            return
        for col in range(n):
            if checkIf_attack(plateau, ligne, col):
                plateau[ligne] = col
                process_resolve(plateau, ligne + 1, solutions)

    solutions = []
    process_resolve([-1] * n, 0, solutions)
    return solutions

def generate_map(solutions, n):
    grilles = []
    for sol in solutions:
        grille = [["#" for _ in range(n)] for _ in range(n)]
        for i in range(n):
            grille[i][sol[i]] = "R"

        # print
        for ligne in grille:
            print(" ".join(ligne))
        print()

        # stockage
        grilles.append(grille)
    return grilles

def init_plateau(n):
    solutions = set_reines(n)
    if not solutions:
        message = f"no solution, for n = {n}"
        print(message)
        return message
    generate_map(solutions, n)

def main():
    n = int(input("Entrez le n: "))
    init_plateau(n)

if __name__ == "__main__":
    main()
