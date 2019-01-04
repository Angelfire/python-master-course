#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 3 - Pirple
Homework Assignment #3: "If" Statements
"""

def compare(param1, param2, param3):
  """
    Args:
      param1 (string or int)
      param2 (string or int)
      param3 (string or int)

    Returns:
      bool: True if 2 params are equal, False if none of them are equal
  """
  param1, param2, param3 = int(param1), int(param2), int(param3)

  if (param1 == param2) or (param1 == param3) or (param2 == param3):
    return True
  else:
    return False

print(compare(9, 3, 3))
print(compare("9", "32", "3"))
print(compare(9, 32, "3"))
print(compare("9", 3, "3"))
