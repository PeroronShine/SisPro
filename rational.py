class Rational:
  """принимаем два необязательных аргумента (n)числитель и (m)знаментель
  используем аннотацию типов, указываем, что оба числа могут быть целыми
  или None

  проверяем на целочисленность, а после устанавливаем значения
  как закрытое поле (атрибут)
  """
  def __init__(self, n: int | None, m: int | None):
    if not isinstance(n, int):
      raise ValueError("numerator must be an int")
    if not isinstance(m, int):
      raise ValueError("denomitor must be an int")

    self.__numerator = n

    """знаменатель не может быть равен 0"""
    if m==0:
      raise ValueError("Division by zero")

    self.__denominator = m

  """геттер для числителя
  получаем значение числителя через свойство numerator"""
  @property
  def numerator(self):
    return self.__numerator

  """сеттер для числителя
  устанавливаем значение числителя
  принимаем значение и проверяем целое оно или нет"""
  @numerator.setter
  def numerator(self, value: int | None):
    if not isinstance(value, int):
      raise ValueError("numerator must be an int")
    self.__numerator = value

  """аналогично геттер и сеттер для знаменателя"""
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

  """Метод для сложения"""
  def __add__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other. denominator)
    elif isinstance(other, int):
      return Rational(self.numerator + other * self.denominator, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __iadd__(self, other):
    """Метод для унарного сложения"""
    if isinstance(other, Rational):
      self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
      self.denominator = self.denominator * other.denominator
    elif isinstance(other, int):
      self.numerator = self.numerator + other * self.denominator
    else:
      raise TypeError("Operand must be an integer or Rational")
    return self

  def __sub__(self, other):
    """Метод для вычитания"""
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator + self.denominator * other.numerator * -1, self.denominator * other. denominator)
    elif isinstance(other, int):
      return Rational(self.numerator - other * self.denominator, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __isub__(self, other):
    """Метод для унарного вычитания"""
    if isinstance(other, Rational):
      self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
      self.denominator = self.denominator * other.denominator
    elif isinstance(other, int):
      self.numerator = self.numerator - other * self.denominator
    else:
      raise TypeError("Operand must be an integer or Rational")
    return self

  def __mul__(self, other):
    """Метод для умножения"""
    if isinstance(other, Rational):
      return Rational(self.numerator * other.numerator, self.denominator*other.denominator)
    elif isinstance(other, int):
      return Rational(self.numerator * other, self.denominator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __imul__(self, other):
    """Метод для унарного умножения"""
    if isinstance(other, Rational):
      self.numerator *= other.numerator
      self.denominator *= other.denominator
    elif isinstance(other, int):
      self.numerator *= other
    else:
      raise TypeError("Operand must be an integer or Rational")
    return self

  def __truediv__(self, other):
    """Метод для деления"""
    if isinstance(other, int):
      if other == 0:
        raise ValueError("Division by zero")
      else:
        return Rational(self.numerator, self.denominator * other)
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    else:
      raise TypeError("Operand must be an integer or Rational")

  def __itruediv__(self, other):
    """Метод для унарного деления"""
    if isinstance(other, int):
      if other == 0:
        raise ValueError("Division by zero")
      else:
        self.denominator *= other
    if isinstance(other, Rational):
      self.numerator *= other.denominator
      self.denominator *= other.numerator
    else:
      raise TypeError("Operand must be an integer or Rational")
    return self

  def __eq__(self, other):
    """метод определения равенства (==)"""
    if isinstance(other, Rational):
      return self.numerator * other.denominator == self.denominator * other.numerator
    elif isinstance(other, int):
      return self.numerator == other * self.denominator
    else:
      raise ValueError("Operand must be an int or Rational")

  def __ne__(self, other):
    """метод определения неравенства (!=)"""
    return not self == other

  """возведение в степень"""
  def __pow__(self, exponent: int):
    if not isinstance(exponent, int):
      raise ValueError("Exponent must be an int")
    if exponent < 0:
      return Rational(self.denominator ** abs(exponent), self.numerator ** abs(exponent))
    else:
      return Rational(self.numerator ** exponent, self.denominator ** exponent)

  """модуль"""
  def __abs__(self):
    return Rational(abs(self.numerator), abs(self.denominator))

  """представляет рациональное число в формате "числитель/знаменатель"
  в формате строки"""
  def __str__(self):
    return f"{self.numerator}/{self.denominator}"

  def __repr__(self):
    return f"Rational({self.numerator}, {self.denominator})"

  def print_fraction(self):
    return f"Rational number: ({self.numerator} / {self.denominator})"

  def to_float(self):
    return self.numerator / self.denominator
