import unittest
from operaciones import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertIsInstance(dividir(5, 0), str) #Cuando tratamos de dividir entre cero, el programa devuelve el mensaje str que hemos escrito
if __name__ == '__main__':
 unittest.main()