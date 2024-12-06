def decrypt(message: [int]) -> str:
    """
    Convertit une liste de valeurs ASCII en chaîne de caractères.
    """
    return ''.join(chr(code) for code in message)

# Section de tests
def run_tests():
    # Message à décrypter
    coded_message = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 115, 
                 101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 
                 101, 32, 33]

    
    # Test de décryptage
    decrypted_text = decrypt(coded_message)
    expected_text = "This exercise is awesome !"
    
    # Debug print
    print("Decrypted text:", repr(decrypted_text))
    print("Expected text:", repr(expected_text))
    
    # Comparaison détaillée
    if decrypted_text != expected_text:
        print("Les chaînes ne correspondent pas ! Diagnostic détaillé :\n")
        print(f"Longueur chaîne décryptée : {len(decrypted_text)}")
        print(f"Longueur chaîne attendue  : {len(expected_text)}\n")
        
        # Comparaison caractère par caractère
        for i in range(max(len(decrypted_text), len(expected_text))):
            actual = decrypted_text[i] if i < len(decrypted_text) else None
            expected = expected_text[i] if i < len(expected_text) else None
            
            actual_code = ord(actual) if actual else "None"
            expected_code = ord(expected) if expected else "None"
            
            print(f"Index {i}:")
            print(f"  Chaîne décryptée : '{actual}' (code ASCII : {actual_code})")
            print(f"  Chaîne attendue  : '{expected}' (code ASCII : {expected_code})\n")
    else:
        print("✓ Les chaînes correspondent exactement !")

        
        # Vérification
        assert decrypted_text == expected_text, "Le déchiffrement est incorrect"
        print("✓ Déchiffrement réussi !")

if __name__ == '__main__':
    run_tests()
