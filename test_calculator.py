import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(1.2, 3.4), 4.6)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertAlmostEqual(sub(5.5, 2.2), 3.3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(math.e, math.e), 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(100, 1)

        with self.assertRaises(ValueError):
            log(100, -5)

        with self.assertRaises(ValueError):
            log(-100, 10)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(9, 3), 3.0)
        self.assertAlmostEqual(div(5, 2), 2.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(10, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == "__main__":
    unittest.main()