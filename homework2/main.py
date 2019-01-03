#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 2 - Pirple
Homework Assignment #2: Functions
"""


def song():
  """
    Returns:
      string: The name of the song
  """
  song = "Walking in my shoes"

  return song

def artist():
  """
    Returns:
      string: The name of the artist
  """
  artist = "Depeche Mode"

  return artist

def youtube_video():
  """
    Returns:
      string: The URL for the Youtube video
  """
  youtube_url = "https://www.youtube.com/watch?v=GrC_yuzO-Ss"

  return youtube_url

def song_writer(composer):
  """
    Args:
      composer (string): The name of the composer

    Returns:
      bool: True if composer is equal to Martin Gore, False if else
  """
  if composer == "Martin Gore":
    return True
  else:
    return False

print("Song\t\t\t", song())
print("Artist\t\t\t", artist())
print("Youtube URL\t\t", youtube_video())
print("Song Writer\t\t", song_writer("Martin Gore"))
print("Song Writer\t\t", song_writer("Dave Gahan"))
