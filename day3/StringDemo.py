# Positive Indexing
s = 'Hello world'
print(s[0])
# Negative Indexing ( started from last index as -1)
s = 'hello world'
print(s[-1])
# slicing (Its like substring)
s = 'hello world'
print(s[0:4])
print(s[6:])
print(s[:3])
print(s[:])
print(s[0:6:2])  # step is 2
print(s[6:0:-1])  # if step size is negative then first value should be greater than second one
print(s[::-1])  # reverse a string
# Editing a string
s = 'hello world'
# s[0] = 'H' we can't edit
# delete
del s
