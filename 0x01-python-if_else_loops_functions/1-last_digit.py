#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l = number % -10
else:
    l = number % 10
if l > 5:
    print(f"Last digit of {number} is {l} and is greater than 5")
elif l == 0:
    print(f"Last digit of {number} is {l} and is 0")
else:
    print(f"Last digit of {number} is {l} and is less than 6 and not 0")
