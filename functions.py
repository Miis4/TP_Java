# Fonction qui retourne une liste de 10 zéros
def several_zeros():
    return [0] * 10

# Fonction qui retourne une liste personnalisée de zéros
def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

# Fonction qui crée une matrice de zéros avec des dimensions spécifiées
def matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Classe pour créer et manipuler des matrices
class Matrix:
    def __init__(self, rows, cols):
        # Initialisation d'une matrice de zéros avec les dimensions spécifiées
        self._data = [[0 for _ in range(cols)] for _ in range(rows)]
        self._rows = rows
        self._cols = cols

    def get_value(self, row, col):
        # Récupèration de la valeur à la position spécifiée
        return self._data[row][col]

    def __eq__(self, other):
        # Comparer deux matrices
        if not isinstance(other, Matrix):
            return False
        return (self._rows == other._rows and 
                self._cols == other._cols and 
                self._data == other._data)

# Section de tests 
def run_tests():
    # Tests several_zeros()
    zeros_list = several_zeros()
    assert len(zeros_list) == 10, "several_zeros() doit retourner exactement 10 zéros"
    assert all(x == 0 for x in zeros_list), "Tous les éléments doivent être des zéros"
    print("✓ Test several_zeros() réussi")

    # Tests several_zeros_custom()
    # Test avec valeur par défaut
    default_zeros = several_zeros_custom()
    assert len(default_zeros) == 10, "several_zeros_custom() sans argument doit retourner 10 zéros"
    
    # Test avec valeur personnalisée
    custom_zeros = several_zeros_custom(5)
    assert len(custom_zeros) == 5, "several_zeros_custom(5) doit retourner 5 zéros"
    assert all(x == 0 for x in custom_zeros), "Tous les éléments doivent être des zéros"
    print("✓ Test several_zeros_custom() réussi")

    # Tests matrix()
    # Test création de matrice
    test_matrix = matrix(3, 4)
    assert len(test_matrix) == 3, "La matrice doit avoir 3 lignes"
    assert all(len(row) == 4 for row in test_matrix), "Chaque ligne doit avoir 4 colonnes"
    assert all(all(x == 0 for x in row) for row in test_matrix), "Tous les éléments doivent être des zéros"
    print("✓ Test matrix() réussi")

    # Tests classe Matrix
    # Test création et récupération valeur
    m = Matrix(2, 3)
    assert m.get_value(0, 0) == 0, "La valeur par défaut doit être 0"
    
    # Test égalité de matrices
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    m3 = Matrix(3, 2)
    
    assert m1 == m2, "Deux matrices de même taille doivent être égales"
    assert m1 != m3, "Matrices de tailles différentes ne doivent pas être égales"
    print("✓ Test Matrix() réussi")

    print("Tous les tests sont passés avec succès !")

if __name__ == '__main__':
    pass

run_tests()