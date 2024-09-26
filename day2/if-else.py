# if-else in python
email = input('enter email')
password = input('enter password')
if email == 'xyz@gmail.com' and password == '1234':
    print('welcome')
elif email == 'xyz@gmail.com' and password != '1234':
    print('Incorrect Password')
    password = input('enter password again')
    if password == '1234':
        print('Welcome, Finally!')
    else:
        print('Not successful')
else:
    print('Not correct')
