import unittest
from exo3 import processLines

# Les tests unitaires
class TestExo3(unittest.TestCase):

    def test_input_2(self):
        # Lire les lignes depuis les fichiers
        with open("C:\\Users\\ALINWARE TM\\Documents\\GitHub\\tdlog_exercices\\exo3\\sample\\input1.txt", "r") as input1:
            # Lire les lignes et enlever les espaces en début/fin
            lines = [line.strip() for line in input1.readlines()]

        with open("C:\\Users\\ALINWARE TM\\Documents\\GitHub\\tdlog_exercices\\exo3\\sample\\output1.txt", "r") as output1:
            # Lire le contenu attendu et enlever les espaces en début/fin
            expected = output1.read().strip()

        # Tester si la sortie de la fonction correspond à l'attendu
        self.assertEqual(expected, processLines(lines))

if __name__ == '__main__':
    unittest.main()



