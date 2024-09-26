# Menu driven calculator
fnum = int(input('enter first num'))
snum = int(input('enter second num'))
op = input('enter the operation')
if op == '+':
    print(fnum+snum)
elif op == '-':
    print(fnum-snum)
elif op == '*':
    print(fnum*snum)
else:
    print(fnum/snum)

# Multi line input
menu = input("""
Hi! How can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawal
4. Enter 4 for exit
""")
if menu == '1':
    print('pin change')
elif menu == '2':
    print('balance')
elif menu == '3':
    print('withdraw')
else:
    print('exit')
