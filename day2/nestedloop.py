# Sequence sum
# 1/1! + 2/2! + 3/3! +..
n = int(input('enter n'))
fact = 1
result = 0
for i in range(1, n+1):
    fact = fact * i
    result = result + i/fact
print(result)
# Nested Loops
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)
# Pattern
# *
# **
# ***
r = int(input('enter number of rows'))
for i in range(1, r+1):
    for j in range(1, i+1):
        print('*', end='')
    print()
# 1
# 121
# 12321
# 1234321
r = int(input('enter rows'))
for i in range(1, r+1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(i-1, 0, -1):
        print(k, end='')
    print()
# Loop control statement
# break, continue, pass
for i in range(1, 10):
    if i == 4:
        break
    print(i)
# print prime numbers between two range
lower = int(input('enter lower range'))
upper = int(input('enter upper range'))
for i in range(lower, upper+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
# continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# pass: used avoid error
for i in range(1, 10):
    pass


