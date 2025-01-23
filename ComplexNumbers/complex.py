import math
from rational import Rational

class Complex:
  def __init__(self, real: int | Rational | float, imag: int | Rational | float = 0):
    self._real = Rational(real)
    self._imag = Rational(imag)

  @property
  def imag(self):
    if isinstance(self._imag, Rational):
      if self._imag.denominator == 1:
        self._imag = self._imag.numerator
    return self.__imag

  @imag.setter
  def imag(self, value):
    self.__imag = value

  @property
  def real(self):
    if isinstance(self._real, Rational):
      if self._real.denominator == 1:
        self._real = self._real.numerator
    return self.__real

  @real.setter
  def real(self, value):
    self.__real = value

  def __add__(self, other):
    '''метод для сложения'''
    if isinstance(other, Rational | int | float):
      return Complex(self.real + other, self.imag)
    if isinstance(other, Complex):
      return Complex(self.real + other.real, self.imag + other.imag)
    return ValueError("other must be rational or int or float")
    
  def __iadd__(self, other):
    if isinstance(other, Rational | int | float):
      self.real += Rational(other)
      self.imag += Rational(other)
    if isinstance(other, Complex):
      self.real += other.real
      self.imag += other.imag
    else:
      return ValueError("other must be rational or int or float")
    return self

  def __sub__(self, other):
    if isinstance(other, Complex):
      return Complex(self.real - other.real, self.imag - other.imag)
    if isinstance(other, Rational | int | float):
      return Complex(self.real - other, self.imag)
    return ValueError("other must be rational or int or float")
  
  def __isub__(self, other):
    if isinstance(other, Rational | int | float):
      self.real -= Rational(other)
      self.imag -= Rational(other)
    if isinstance(other, Complex):
      self.real -= other.real
      self.imag -= other.real
    else:
      return ValueError("other must be rational or int or float")
    return self

  def __mul__(self, other):
    if isinstance(other, Rational | int | float):
      return Complex(self.real * other, self.imag * other)
    if isinstance(other, Complex):
      return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    return ValueError("other must be rational or int or float")
    
  def __imul__(self, other):
    if isinstance(other, Rational | int | float):
      self.real *= Rational(other)
      self.imag *= Rational(other)
    if isinstance(other, Complex):
      self.real = self.real * other.real - self.imag * other.imag
      self.imag = self.real * other.imag + self.imag * other.real
    else:
      return ValueError("other must be rational or int or float")
    return self

  def __truediv__(self, other):
    if isinstance(other, Rational | int | float):
      return Complex(self.real / other, self.imag / other)
    if isinstance(other, Complex):
      denominator = other.real * other.real + other.imag * other.imag
      if denominator.numerator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
      return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)
    return ValueError("other must be rational or int or float")

  def __itruediv__(self, other):
    if isinstance(other, Rational | int | float):
      if other == 0:
        raise ZeroDivisionError
      self.real = Rational(self.real)
      self.imag = Rational(self.imag)
      self.real /= Rational(other)
      self.imag /= Rational(other)
    if isinstance(other, Complex):
      denominator = other.real * other.real + other.imag * other.imag
      if denominator.numerator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
      self.real = (self.real * other.real + self.imag * other.imag) / (other.real * other.real + other.imag * other.imag)
      self.imag = (self.imag * other.real - self.real * other.imag) / (other.real * other.real + other.imag * other.imag)
    else:
      return ValueError("other must be rational or int or float")
    return self

  def __eq__(self, other):
    if isinstance(other, Rational | int | float):
      return self.real == other and self.imag == 0
    if isinstance(other, Complex):
      return self.real == other.real and self.imag == other.imag
    return ValueError("other must be rational or int or float")

  def __ne__(self, other):
    return not self == other

  def __neg__(self):
    return Complex(-self.real, -self.imag)

  def __str__(self):
    if self.imag.numerator == 0:
      return f'{self.real}'
    if self.imag.numerator < 0:
      return f'{self.real} - {-self.imag}i'
    return f'{self.real} + {self.imag}i'

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
  
  def __repr__(self):
    return f'{self.__class__.__name__}(real={self.real}, imag={self.imag})'
