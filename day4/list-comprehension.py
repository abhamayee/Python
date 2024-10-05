# Add 1 to 10 number to a list
l = []
for i in range(1, 11):
    l.append(i)
print(l)
l1 = [i for i in range(1, 11)]
print(l1)
# scalar multiplication on a vector
v = [2, 3, 4]
s = -3
x = [s * i for i in v]
print(x)
# add square
L = [1, 2, 3, 4]
L1 = [i ** 2 for i in L]
print(L1)
# print all numbers divisible by 5 in the range 1 to 50
l = [ i for i in range(1, 51) if i % 5 == 0]
print(l)
# Find languages which starts with letter p
lan = ['java', 'python', 'php', 'c', 'javascript']
li = [i for i in lan if i.startswith('p')]
print(li)
# Nested if with list comprehension
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
# create a new list from my-fruits if the fruits exits in basket and also starts with 'a'
fruit = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(fruit)
# print (3 * 3) matrix
mat = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print(mat)
# cartesian products
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
cart = [i * j for i in L1 for j in L2]
print(cart)
# zip
L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]
print(list(zip(L1, L2)))
z = [i + j for i, j in zip(L1, L2)]
print(z)

