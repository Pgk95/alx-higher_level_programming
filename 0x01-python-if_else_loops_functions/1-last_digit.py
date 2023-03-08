#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1
message = "Last digit of %d is %d and is" % (number, last_digit)
if last_digit > 5:
    print(f"{message} is greater than 5")
if last_digit == 0:
    print(f"{message} zero")
if last_digit < 6:
    print(f"{message} less than 6 and not 0")
