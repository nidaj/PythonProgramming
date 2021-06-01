"""
program to accept n (number) as input from command line and calculate power of 2 till n
"""
import sys

n = int(sys.argv[1])
i = 1
if n <= 31:
    while 0 < i <= n:
        print(2 ** i)
        i += 1
else:
    print("Enter number less than 31 to avoid overflow problem")
