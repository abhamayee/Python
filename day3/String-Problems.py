# Find the length of a given string without using len()
s = input('enter the string')
counter = 0
for i in s:
    counter += 1
print('length of the string is:', counter)
# Extract username from a given email
# Eg if the email is test123@gmail.com
# then the username should be test123
email = input('enter the email')
pos = email.index('@')
print(email[0:pos])
# write a program that convert number to string
num = int(input('enter a number'))
digits = '0123456789'
result = ''
while num != 0:
    result = digits[num%10] + result
    num = num // 10
print(result)
