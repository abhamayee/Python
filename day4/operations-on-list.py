L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
# concatenation/Merge
print(L1+L2)
print(L1 * 3)  # 3times L1 will merge
# Membership
print(5 in L1)
print(4 in L1)
print(5 not in L1)
# loops
for i in L1:
    print(i)
# len/min/max/sorted
L = [1, 3, 2, 6, 4, 6]
print(len(L))
print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L, reverse=True))
L = [1, 2, 5, 4, 5]
print(L.count(5))
# index
print(L.index(2))
# reverse
L.reverse()  # Permanently reverse the list
print(L)
# sort
L.sort()
print(L)
# copy
L1 = L.copy()
print(L1)
