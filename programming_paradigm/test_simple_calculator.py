import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(5, 2)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = self.calc.subtract(4, 7)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = self.calc.multiply(7, 7)
        self.assertEqual(result, 49)
    
    def test_divide(self):
        result = self.calc.divide(12, 3)
        self.assertEqual(result, 4)
        
        self.assertRaises(ZeroDivisionError, self.calc.divide, 4, 0)
    

 