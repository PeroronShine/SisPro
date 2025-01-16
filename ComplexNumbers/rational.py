import math

class Rational:
  def __init__(self, n, m = 1):
    if m == 0:
      raise ValueError("Denominator cannot be zero")
    if isinstance(n, Rational) or isinstance(m, Rational):
      self._rational_input(n, m)
    else:
      self._float_input(n, m)

    self._simplify()

  def _rational_input(self, n, m):
    if isinstance(n, Rational) and isinstance(m, Rational):
      self.numerator = n.numerator * m.denominator
      self.denominator = n.denominator * m.numerator
    elif isinstance(n, Rational):
      self.numerator = n.numerator
      self.denominator = n.denominator * m
    elif isinstance(m, Rational):
      self.numerator = n * m.denominator
      self.denominator = m.numerator

  def _float_input(self, num, denom):
    #num denom - вещ числа
    num_num, num_denom = None, None
    den_num, den_denom = None, None

    if isinstance(num, float):
        num_num, num_denom = self._float2rational(num)
    if isinstance(denom, float):
        den_num, den_denom = self._float2rational(denom)

    #обработка
    if num_num is not None and den_num is not None:
      self.numerator = num_num * den_denom
      self.denominator = den_num * num_denom
    elif num_num is not None:
      self.numerator = num_num
      self.denominator = num_denom * denom
    elif den_num is not None:
      self.numerator = den_denom * num
      self.denominator = den_num

    elif isinstance(num, int) and isinstance(denom, int):
      self.numerator = num
      self.denominator = denom
  
  def _simplify(self):
    gcd_val = math.gcd(self.numerator, self.denominator)
    self.numerator //= gcd_val
    self.denominator //= gcd_val

    if self.denominator < 0:
      self.numerator = -self.numerator
      self.denominator = -self.denominator

  def _float2rational(self, num):
    if num.is_integer():
      return int(num), 1

    sign = -1 if num < 0 else 1
    num = abs(num)
    decimal_places = len(str(num).split('.')[-1])
    denom = 10 ** decimal_places
    numerator = round(num * denom)

    gcd_val = math.gcd(numerator, denom)
    numerator //= gcd_val
    denom //= gcd_val

    return sign * numerator, denom

  @property
  def numerator(self):
    return self.__numerator

  @numerator.setter
  def numerator(self, value: int | None):
    if not isinstance(value, int):
      raise ValueError("numerator must be an int")
    self.__numerator = value

  @property
  def denominator(self):
    return self.__denominator

  @denominator.setter
  def denominator(self, value: int | None):

    if not isinstance(value, int):
      raise ValueError("denominator must be an int")

    if value == 0:
      raise ValueError("Denominator cannot be zero")

    self.__denominator = value

  def __add__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other. denominator)
    elif isinstance(other, int):
      return Rational(self.numerator + other * self.denominator, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __sub__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator + self.denominator * other.numerator * -1, self.denominator * other. denominator)
    elif isinstance(other, int):
      return Rational(self.numerator - other * self.denominator, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __mul__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.numerator, self.denominator*other.denominator)
    elif isinstance(other, int):
      return Rational(self.numerator * other, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __truediv__(self, other):
    if isinstance(other, int):
      if other == 0:
        raise ValueError("Division by zero")
      else:
        return Rational(self.numerator, self.denominator * other)
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __eq__(self, other):
    if isinstance(other, Rational):
      return self.numerator * other.denominator == self.denominator * other.numerator
    elif isinstance(other, int):
      return self.numerator == other * self.denominator
    else:
      raise ValueError("Operand must be an int or Rational")

  def __ne__(self, other):
    if isinstance(other, Rational):
      return self.numerator != other.numerator or self.denominator != other.denominator
    return NotImplemented

  def __pow__(self, exponent: int):
    if not isinstance(exponent, int):
      raise ValueError("Exponent must be an int")
    if exponent < 0:
      return Rational(self.denominator ** abs(exponent), self.numerator ** abs(exponent))
    else:
      return Rational(self.numerator ** exponent, self.denominator ** exponent)

  def __lt__(self, other):
    if isinstance(other, Rational):
      return self.numerator * other.denominator < other.numerator * self.denominator
    elif isinstance(other, int | float):
      return self.numerator < other * self.denominator
    return NotImplemented

  def __le__(self, other):
    if isinstance(other, Rational):
      return self.numerator * other.denominator <= other.numerator * self.denominator
    elif isinstance(other, int | float):
      return self.numerator <= other * self.denominator
    return NotImplemented
  
  def __gt__(self, other):
    if isinstance(other, Rational):
        return self.numerator * other.denominator > other.numerator * self.denominator
    elif isinstance(other, int | float):
        return self.numerator > other * self.denominator
    return NotImplemented

  def __ge__(self, other):
    if isinstance(other, Rational):
        return self.numerator * other.denominator >= other.numerator * self.denominator
    elif isinstance(other, int | float):
        return self.numerator >= other * self.denominator
    return NotImplemented

  def __round__(self, n=None):
      if n is None:
          return Rational(round(self.numerator / self.denominator))
      else:
          factor = 10 ** n
          rounded_numerator = round(self.numerator * factor / self.denominator)
          return Rational(rounded_numerator, factor)
      
  def __abs__(self):
    return Rational(abs(self.numerator), abs(self.denominator))
  
  def __str__(self):
    if self.denominator == 1:
        return str(self.numerator)
    return f"{self.numerator}/{self.denominator}"

  def __repr__(self):
    return f"Rational({self.numerator}, {self.denominator})"

  def print_Rational(self):
    return f"Rational number: ({self.numerator} / {self.denominator})"

  def __int__(self):
      return self.numerator // self.denominator

  def to_float(self):
    return self.numerator / self.denominator
  
  def __neg__(self):
    return Rational(-self.numerator, self.denominator)
