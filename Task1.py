# Q1 :- Print the given strings as per stated format.
# Given strings:

"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
# Output:
# Data-Science-Mentorship-Program-started-By-CampusX
# Concept- [Seperator and End]
# Write your code here
print('Data', 'Science', 'Mentorship', 'Program', sep='-', end='-')
print('started', 'By', 'Campus', sep='-')

# Q2:- Write a program that will convert celsius value to fahrenheit.
# Write your code here
cel = float(input('Enter celcius degree'))
far = (cel*9/5) + 32
print(far)
# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers
# without using any special python syntax.
num1 = int(input('enter first number'))
num2 = int(input('enter second number'))
print('num1: ', num1, 'num2: ', num2)
temp = num1
num1 = num2
num2 = temp
print('After swap', 'num1: ', num1, 'num2: ', num2)
# Write your code here
# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
x1 = float(input('enter x coordinate of first point'))
y1 = float(input('enter y coordinate of first point'))
x2 = float(input('enter x coordinate of second point'))
y2 = float(input('enter y coordinate of second point'))
eucl_dist = ((x2-x1)**2 - (y2-y1)**2)**1/2
print('Euclidean distance between two points', (x1,y1),'and', (x2,y2), 'is', eucl_dist)
# Write your code here
# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
principal = float(input('Enter principal amount'))
time = int(input('Enter time period'))
rate = float(input('Enter rate of interest'))
si = (principal*time*rate)/100
print('simple interest', si)
# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2
total_heads = int(input('enter total head count'))
total_legs = int(input('enter total leg count'))
dog_count = (total_legs - (2*total_heads))/2
chik_count = total_heads - dog_count
print('Dog count:', dog_count, 'Chicken count:', chik_count)
# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input('enter n'))
sum = (n*(n+1)*(2*n+1))/6
print('Sum of squares of first', n, 'natural numbers is: ', sum)
# Write your code here
# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
a1 = int(input('enter first number in AP'))
a2 = int(input('enter second number in AP'))
d = a2 - a1
n = int(input('enter n'))
a_n = a1 + (n-1) * d
print('Nth number in AP is: ', a_n)
# Q9:- Given 2 fractions, find the sum of those 2 fractions.
# Take the numerator and denominator values of the fractions from the user.

# Q10:- Given the height, width and breadth of a milk tank, you have to find out
# how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input:
# Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm
H = int(input('enter height of the tank'))
L = int(input('Enter length of the tank'))
B = int(input('enter Breadth of the tank'))
h = int(input('enter height of the glass'))
r = int(input('enter radius of the glass'))
vol_tank = H * L * B
vol_glass = 3.14 * (r**2) * h
num_glass_req = vol_tank/vol_glass
print('number of glass required: ', num_glass_req)
