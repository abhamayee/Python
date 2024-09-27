# For loop
for i in range(1, 11):
    print(i)
for i in range(1, 11, 3):
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in 'delhi':
    print(i)
for i in [1, 2, 3, 4, 5]:
    print(i)
# WAP print population reduced by 10%
curr_pop = 10000
for i in range(10, 0, -1):
    print(i, curr_pop)
    curr_pop = curr_pop - 0.1 * curr_pop
