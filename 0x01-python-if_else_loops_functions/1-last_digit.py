#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    last_number = number % 10
    last_number *= -1
    number *= -1
if number >= 0:
    last_number = number % 10
print("Last digit of", number, "is", last_number, end=" ")

if last_number > 5:
    print("and is greater than 5")
if last_number == 0:
    print("and is 0")
if last_number < 6 and last_number != 0:
    print("and is less than 6 and not 0")
