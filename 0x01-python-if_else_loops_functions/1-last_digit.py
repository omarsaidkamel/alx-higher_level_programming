#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = " and is greater than 5"
str2 = " and is 0"
str3 = " and is less than 6 and not 0"
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
