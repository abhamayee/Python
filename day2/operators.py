# Operators
# Arithmetic Operators
print(5+6)
print(5-6)
print(5*6)
print(5/2)
print(5//2)  # Integer division
print(5 % 2)
print(5**2)
# Relational operators
print(4 > 5)
print(4 < 5)
print(4 >= 4)
print(4 <= 4)
print(4 == 4)
# Logical operators
print(1 and 0)
print(1 or 0)
print(not 1)
# Bitwise operators ( applied on binary data)
print(2 & 3)  # Bitwise and
print(2 | 3)  # Bitwise or
print(2 ^ 3)  # Bitwise xor
print(~3)  # Not
print(4 >> 2)  # Right shift
print(4 << 2)  # Left shift
# Assignment operator
a = 2
a += 2  # a = a+2
print(a)
# Membership operators
# in / not in
print('D' in 'Delhi')
print('D' not in 'Delhi')
print(1 in [2, 3, 4, 5])
# Find the sum of a 3-digit number entered by the user
number = int(input('Enter a 3 digit number'))
print(number)
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
print(a + b + c)
