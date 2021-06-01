"""
Program to accept a number n and print harmonic value of n
"""
n = int(input("Enter the number: "))
harmonic_value = 1.00
for i in range(2, n + 1):
    harmonic_value += 1 / i
print(f"The harmonic value of {n} = {round(harmonic_value, 2)}")
