#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Homework 7 - Pirple
Homework Assignment #7: Dictionaries and Sets
"""

dict_artist = {
  "song" : "Walking in My Shoes",
  "artist" : "Depeche Mode",
  "album" : "Songs of Faith and Devotion",
  "song_writer" : "Martin Gore",
  "genre" : "Alternative rock",
  "length_in_seconds_single" : 259,
  "length_in_seconds_album" : 335,
  "release_date" : "1993, 04, 26",
  "single_information_url" : "http://archives.depechemode.com/discography/singles/29_walkinginmyshoes.html",
  "youtube_video" : "https://www.youtube.com/watch?v=GrC_yuzO-Ss"
}

# Print the key and its corresponding value
for key, value in dict_artist.items():
  print(f'{key:25} = {value}')

def guess_value(key, value):
  """
    Allows someone to guess the value of any key in the dictionary

    Args:
      key(string): Song Characteristic
      value(string or number): Value of the characteristic
    
    Returns:
      bool: True if key and value are corrects, False if not
  """
  if (key in dict_artist) and (dict_artist[key] == value):
    return True
  else:
    return False

print("\n")
print(guess_value("artist", "Depeche Mode"))
print(guess_value("song", "Home"))
print(guess_value("song_writer", "Dave Gahan"))
