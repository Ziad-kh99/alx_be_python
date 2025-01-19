import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 2), 7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 7), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 7), 49)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
        
        self.assertRaises(ZeroDivisionError, self.calc.divide, 4, 0)
    

 