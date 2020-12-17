#! /usr/bin/python3
# -*- coding: utf-8 -*-
import re

pattern = r"(?P<a>\d+)-(?P<b>\d+) (?P<letter>.): (?P<password>.+)"  

def main():
  lines = list(re.match(pattern, line) for line in open('./input.txt'))
  part1, part2 = 0, 0
  
  for line in lines:
      (a, b, letter, password) = line.groups()
      a, b = int(a), int(b)
      
      if a <= password.count(letter) <= b:
          part1 += 1
      
      if (password[a - 1] == letter) ^ (password[b - 1] == letter):
          part2 += 1
     
  print("Part 1: {}".format(part1))
  print("Part 2: {}".format(part2))
  

if __name__ == '__main__':
  main()