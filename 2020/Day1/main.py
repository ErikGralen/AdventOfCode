#! /usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import combinations      

def main():
  numbers = set(int(line.strip()) for line in open('./input.txt'))
  
  for n in numbers:
    x = 2020 - n
    if x in numbers:
      ans = x * n
      print("Part 1: {} * {} = {}".format(x,n,ans))
      break
      
  for n, m in combinations(numbers, 2):
    x = 2020 - n - m
    if x in numbers:
      ans = x * n * m
      print("Part 2: {} * {} * {} = {}".format(x,n,m,ans))
      break

if __name__ == '__main__':
  main()