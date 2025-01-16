import math
from rational import Rational
class Complex:
  """вид комплексного числа ai+b => (a, b)"""
  def __init__(self, real: Rational, imag: Rational):
    if not isinstance(imag, Rational):
      raise ValueError("imag must be an rational")
    if not isinstance(real, Rational):
      raise ValueError("real must be an rational")
    self.__imag = imag
    self.__real = real

  @property
  def imag(self):
      return self.__imag

  @imag.setter
  def imag(self, value: Rational | None):
    if not isinstance(value, Rational):
      raise ValueError("imag must be an rational")
    self.__imag = value

  @property
  def real(self):
    return self.__real

  @real.setter
  def real(self, value: Rational | None):
    if not isinstance(value, Rational):
      raise ValueError("real must be an rational")
    self.__real = value

  def __add__(self, other):
    '''метод для сложения'''
    if isinstance(other, Rational | int):
      return Complex(self.real + other, self.imag)
    if isinstance(other, Complex):
      return Complex(self.real + other.real, self.imag + other.imag)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    
  def __iadd__(self, other):
    if isinstance(other, Rational | int):
      self.real = self.real + other
    if isinstance(other, Complex):
      self.real = self.real + other.real
      self.imag = self.imag + other.imag
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    return self

  def __sub__(self, other):
    if isinstance(other, Complex):
      return Complex(self.real - other.real, self.imag - other.imag)
    if isinstance(other, Rational | int):
      return Complex(self.real - other, self.imag)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")

  def __isub__(self, other):
    if isinstance(other, Rational | int):
      self.real = self.real + other*(-1)
    if isinstance(other, Complex):
      self.real = self.real + other.real*(-1)
      self.imag = self.imag + other.imag*(-1)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    return self

  def __mul__(self, other):
    if isinstance(other, Rational | int):
      return Complex(self.real * other, self.imag * other)
    if isinstance(other, Complex):
      return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    
  def __imul__(self, other):
    if isinstance(other, Rational | int):
      self.real *= other
      self.imag *= other
    if isinstance(other, Complex):
      self.real = self.real * other.real - self.imag * other.imag
      self.imag = self.real * other.imag + self.imag * other.real
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    return self

  def __truediv__(self, other):
    if isinstance(other, Rational | int):
      return Complex(self.real / other, self.imag / other)
    if isinstance(other, Complex):
      denominator = other.real * other.real + other.imag * other.imag
      if denominator.numerator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
      return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")

  def __itruediv__(self, other):
    if isinstance(other, Rational | int):
      self.real /= other
      self.imag / other
    if isinstance(other, Complex):
      denominator = other.real * other.real + other.imag * other.imag
      if denominator.numerator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
      self.real = (self.real * other.real + self.imag * other.imag) / (other.real * other.real + other.imag * other.imag)
      self.imag = (self.imag * other.real - self.real * other.imag) / (other.real * other.real + other.imag * other.imag)
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")
    return self

  def __eq__(self, other):
    if isinstance(other, Rational | int):
      return self.real == other and self.imag == 0
    if isinstance(other, Complex):
      return self.real == other.real and self.imag == other.imag
    else:
      raise TypeError("Operand must be an Complex or Rational or Int")

  def __ne__(self, other):
    return not self == other

  def __neg__(self):
    return Complex(-self.real, -self.imag)

  def __str__(self):
    sign = '+' if self.imag.numerator >= 0 else '-'
    return f"{self.real} {sign} {abs(self.imag)}i"

  def power(self, n):
    if n < 0:
      raise ValueError("Exponent must be a natural number")
    if n == 0:
      return Complex(Rational(1, 1), Rational(0, 1))
    result = Complex(Rational(1, 1), Rational(0, 1))
    for _ in range(n):
      result *= self
    return result

  def arg(self):
    return math.atan2(self.imag.to_float(), self.real.to_float())

  def abs(self):
    return math.sqrt(self.real.to_float()**2 + self.imag.to_float()**2)
    

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
