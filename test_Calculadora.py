import unittest
from calculadora import multiplicar

class TestCalculator(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()
