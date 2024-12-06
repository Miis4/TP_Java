class Disk:
    def __init__(self, total, used):
        """
        Initialisation d'un disque avec un espace total et un espace utilisé.
        total: Espace total du disque en Go
        used: Espace utilisé du disque en Go
        """
        self._total = total
        self._used = used

    @property
    def free(self):
        """Calcule et retourne l'espace libre du disque."""
        return self._total - self._used

    @property
    def used_perc(self):
        """Calcule et retourne le pourcentage d'espace utilisé."""
        return self._used / self._total

    def __str__(self):
        """Représentation disque."""
        return f"Disk[total: {self._total} Gb, used: {self._used} Gb]"

    def __repr__(self):
        """Représentation débogage."""
        return self.__str__()

    def __lt__(self, other):
        """
        Permet le tri basé sur le pourcentage d'espace utilisé.
        
        """
        return self.used_perc < other.used_perc

# Section de tests 

def run_tests():
    # Test de création et propriétés de base
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)
    
    # Test des propriétés
    assert disk1.free == 8, "Calcul de l'espace libre incorrect"
    assert disk2.free == 15, "Calcul de l'espace libre incorrect"
    assert abs(disk1.used_perc - 0.2) < 1e-10, "Calcul du pourcentage utilisé incorrect"
    assert abs(disk2.used_perc - 0.25) < 1e-10, "Calcul du pourcentage utilisé incorrect"
    print("✓ Tests de propriétés réussis")

    # Test de la représentation textuelle
    assert str(disk1) == "Disk[total: 10 Gb, used: 2 Gb]", "Représentation textuelle incorrecte"
    print("✓ Test de représentation textuelle réussi")

    # Test du tri
    disks = [disk1, disk2]
    disks_sorted = sorted(disks)
    assert disks_sorted[0] == disk1, "Tri incorrect des disques"
    assert disks_sorted[1] == disk2, "Tri incorrect des disques"
    print("✓ Test de tri réussi")

    print("Tous les tests sont passés avec succès !")

if __name__ == '__main__':
    pass
