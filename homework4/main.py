#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 4 - Pirple
Homework Assignment #4: Lists
"""

myUniqueList = []
myLeftovers = []

def add_extra_value(value):
  """
    Args:
      value: (str, int, float, list, dictionary)
    Returns:
      array
  """

  return myLeftovers.append(value)

def add_value(value):
  """
    Args:
      value: (str, int, float, list, dictionary)
    Returns:
      bool
  """

  if value in myUniqueList:
    add_extra_value(value)
    return False
  else:
    myUniqueList.append(value)
    return True

add_value(3)
add_value(4)
add_value(3)
add_value("hello")
add_value("Hello")
add_value(3.1)
add_value("hello")
add_value(["Andres", "Bedoya"])
add_value(["andres", "bedoya"])
add_value(["Andres", "bedoya"])
print(myUniqueList)
print(myLeftovers)
