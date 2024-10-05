# del
L = [1, 2, 3, 4, 5]
# del L
print(L)
# indexing
del L[-1]
print(L)
# slicing
del L[1:3]
print(L)
L = [1, 2, 3, 4, 5]
# remove
L.remove(5)  # delete by value
print(L)
# pop
li = [1, 2, 3, 4, 5]
li.pop(1)
print(li)
li.pop()  # remove last item
print(li)
# clear
li.clear()
print(li)

