# Find the smallest number in 3 given numbers
a = int(input('first num'))
b = int(input('second num'))
c = int(input('third num'))
if a < b and a < c:
    print('Smallest is', a)
elif b < c:
    print('Smallest is', b)
else:
    print('Smallest is', c)