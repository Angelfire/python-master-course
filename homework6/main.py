#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 6 - Pirple
Homework Assignment #6: Advanced Loops
"""
import os

t_columns, t_rows = os.get_terminal_size()

def playing_board(rows, columns):
  """
    Args:
      rows(number): Represent the rows
      columns(number): Represent the columns

    Returns:
      bool: True is playing board was drawn, False if rows or columns exceed the current terminal size
  """
  if rows > t_rows or columns > t_columns:
    return False
  else:
    for row in range(rows):
      if row % 2 == 0:
        for column in range(columns):
          if column % 2 == 0:
            print(" ", end="")
          else:
            print("|", end="")
        print("")
      else:
        print("-" * columns)
    return True

playing_board(9, 9)
