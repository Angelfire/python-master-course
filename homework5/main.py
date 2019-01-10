#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 5 - Pirple
Homework Assignment #5: Basic Loops

  Returns:
    FizBuzz list of number from 1 to 100
"""

for num in range(1, 101):
  if num > 1:
    # Verify if num is not Prime
    for i in range(2, num):
      if (num % i) == 0:
        if (num % 3 == 0 and num % 5 == 0):
          print("FizzBuzz")
        elif (num % 5 == 0):
          print("Buzz")
        elif (num % 3 == 0):
          print("Fizz")
        else:
          print(num)
        break
    # if num is Prime
    else:
      print("Prime")
  # Just to print 1
  else:
    print(num)
