"""
Program to flip a coin and find percentage count of head and tail occurences
"""
import random

count_t = 0
count_h = 0
times = int(input("Enter number of times u want 2 flip the coin: "))
for i in range(times):
    if round(random.random(), 2) < 0.5:
        count_t += 1
    else:
        count_h += 1
print(f"The number of times we got tails = {count_t}")
print(f"The number of times we got heads = {count_h}")
per_h = count_h / (count_h + count_t) * 100
per_t = count_t / (count_h + count_t) * 100
print(f"Percentage of Tail occurrence = {per_t}%")
print(f"Percentage of Head occurrence = {per_h}%")
