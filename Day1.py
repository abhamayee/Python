# Python is a case-sensitive language
# 1. Python output
print('Hello World')
print('Hello', 1, 5.6, True)
print('Hello', 1, 5.6, True, sep='/')
print('hello', end='-')
print('world')

# 2. Data Types
print(8)  # Integer
print(1e308)  # 1 * 10^308
print(8.6)  # Decimal/Float
print(True)  # Boolean
print('hello')  # String
print(5+3j)  # complex
print([1, 2, 3, 4])  # list
print((1, 2, 3))  # Tuple
print({1, 2, 3})  # Set
print({'name': 'abha', 'age': 30})  # Dictionary
# type
print(type(3), type('test'))
# 3. Variables
name = 'abha'
print(name)
# Dynamic typing (It can automatically find the type based on value)
a = 5
# Dynamic binding (It can hold any type in variable)
b = 10
print(b)
b = 'test'
print(b)
x, y, z = 1, 2, 3
print(x, y, z)
x = y = z = 5
print(x, y, z)
# 4. Keywords & Identifiers
# Keywords - Reserved by the interpreter eg- print, if, True, def etc
# Identifiers
# You can't start with a digit eg- 1name= 'abha'
# You can use only special char as underscore
_name = 'abha'
_ = 'test'
# Identifier can't be keyword
# 5. User Input
input('Enter your name')
fnum = input('Enter first number')  # 5
snum = input('Enter second num')  # 9
result = fnum + snum
print(result)  # 59
print(type(fnum), type(snum))  # Both are string so it append
# 6. Explicit type conversion
print(int('4'))
print(float(7))
result = int(fnum) + int(snum)
print(result)
# fnum = int(input('Enter first number'))
# snum = int(input('Enter second num'))
# 7. Literals
# Value stored in the variables are called literals
x = 0b1010  # Binary
y = 0o310  # Octal
z = 0x12c  # Hexa decimal
print(x, y, z)
float_1 = 10.5
float_2 = 1.5e2  # 1.5 * 10^2
float_3 = 1.2e-2  # 1.2 * 10^(-2)
print(float_1, float_2, float_3)
x = 5+4j
print(x.real, x.imag)
# String can be declared by single quote / double quote / triple quote
# None
y = None





