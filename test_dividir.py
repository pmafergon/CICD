import unittest
from dividir import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertEqual(dividir(5, 0), ZeroDivisionError)
    
if __name__ == '__main__':
 unittest.main()