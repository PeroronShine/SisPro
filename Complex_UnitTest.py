from complex import Complex
from rational import Rational

a = Complex(Rational(1, 2), Rational(3, 4))
b = Complex(Rational(5, 6), Rational(7, 8))

import unittest
class TestComplex(unittest.TestCase):
  def test_initialization(self):
    r = Complex(3, 4)
    self.assertEqual(r.numerator, 3)
    self.assertEqual(r.denominator, 4)

  def test_add(self):
    self.assertEqual(a + b, Complex(10, 8))

  def test_iadd(self):
    a += b
    result = a + b
    self.assertEqual(a, result)

  def test_sub(self):
    self.assertEqual(a - b, Complex(-2, 8))

  def test_isub(self):
    a -= b
    result = a - b
    self.assertEqual(a, result)

  def test_mul(self):
    self.assertEqual(a * b, Complex(3, 8))

  def test_imul(self):
    a *= b
    result = a * b
    self.assertEqual(a, result)

  def test_truediv(self):
    self.assertEqual(a / b, Complex(4, 6))

  def test_itruediv(self):
    a /= b
    result = a / b
    self.assertEqual(a, result)

  def test_equality(self):
    self.assertEqual(a, Complex(1, 2))

  def test_inequality(self):
    self.assertEqual(a, Complex(3, 4))

  def test_str(self):
    self.assertEqual(str(b), "3/4")
