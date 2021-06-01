"""
Program to take number as an input and print prime factors for the number
"""
import math

number = int(input("Enter the number: "))

# Print the number of two's that divide number and reduce it to an odd number
while number % 2 == 0:
    print(2)
    number = number / 2

# optimized for loop
for i in range(3, int(math.sqrt(number)) + 1, 2):
    while number % i == 0:
        print(i)
        number = number / i

# if number is prime
if number > 2:
    print(number)
