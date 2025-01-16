from complex import Complex
from rational import Rational

c1 = Complex(Rational(1000, 1), Rational(1001, 2))
c11 = Complex(Rational(1002, 3), Rational(1003, 4))
c2 = Complex(Rational(1004, 5), Rational(1005, 6))
c22 = Complex(Rational(1006, 7), Rational(1007, 8))
r1 = Rational(5000, 6)
n = 500

'''вывод значений'''
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"r1: {r1}")
print(f"n: {4}\n")

'''сложение'''
ADD1 = c1 + c2
ADD2 = c1 + r1
ADD3 = c1 + n
print(f"c1 + c2: {ADD1}")
print(f"c1 + r1: {ADD2}")
print(f"c1 + n: {ADD3}\n")

'''умножение'''
MUL1 = c1 * c2
MUL2 = c1 * r1
MUL3 = c1 * n
print(f"c1 * c2: {MUL1}")
print(f"c1 * r1: {MUL2}")
print(f"c1 * n: {MUL3}\n")

'''деление'''
DEV = c1 / c2
print(f"c1 / c2: {DEV}\n")

'''возведение компл числа в нат степень'''
POW = c1.power(3)
print(f"c1^3: {POW}\n")

'''The arg function calculates the phase angle using math.atan2.'''
print(f"arg(c1): {c1.arg()} radians\n")

'''модуль компл числа'''
print(f"abs(c1): {c1.abs()}\n")

'''проверка методов == и !='''
print(f"c1 == c2: {c1 == c2}")
print(f"c1 != c2: {c1 != c2}")

'''унарное сложение'''
c1 += c2
print(f"c1 += c2: {c1}")

'''унарное умножение'''
c1 *= c2
print(f"c1 *= c2: {c1}")

'''унарное деление'''
c1 /= c2
print(f"c1 /= c2: {c1}")

'''деление на 0'''
DEV0 = c1 / 0
print(f"c1 / 0: {DEV0}\n")

