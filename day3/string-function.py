# Common function
# len, max, min, sorted
print(len('hello world'))
print(max('hello world'))
print(min('hello world'))
print(sorted('hello world'))  # return a list
print(sorted('hello world', reverse = True))
# Other function
# capitalized
s = 'hello World'
print(s.capitalize())  # first char will be capital
# Title
print(s.title())  # first letter of each word will be capital
# lower
print(s.lower())
# upper
print(s.upper())
# swapcase
print(s.swapcase())
# count/find/index
print('my name is abha'.count('a'))  # count frequency
print('my name is abha'.index('a'))  # find first matching position, if not present then throw error
print('my name is abha'.find('m'))  #find first matching position, if not present then return -1
# startswith/endswith
print('my name is abha'.startswith('my'))
print('my name is abha'.endswith('is'))
# format
name = 'abha'
gender = 'female'
print('Hi my name is {} and I am a {}'.format(name,gender))
print('Hi my name is {0} and I am a {1}'.format(name,gender))
# isalnum/isalpha/isdigit/isidentifier
print('abha1234'.isalnum())
print('abha1234%'.isalnum())
print('abha'.isalpha())
print('12a'.isalpha())
print('12'.isdigit())
print('1name'.isidentifier())
print('name1'.isidentifier())
# split/join
print('hi my name is abha'.split())
print('hi my name is abha'.split('i'))
print(' '.join(['hi', 'my', 'name', 'is', 'abha']))
print('-'.join(['hi', 'my', 'name', 'is', 'abha']))  # reverse of split
# replace
print('hi my name is abha'.replace('abha', 'xyz'))
print('hi my name is abha'.replace('ad', 'xyz'))  # if not present then does not do anything
# strip
print('  abha   '.strip())
