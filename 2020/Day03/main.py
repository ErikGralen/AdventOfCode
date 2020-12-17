#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

def run_slope(toboggan):
    y, x, trees = 0, 0, 0
    width = len(slope[0])
    down, right = toboggan[0], toboggan[1]
    
    while y < len(slope):
      trees += slope[y][x] == '#'
      x = (x + right) % width
      y += down
    return trees
    

def main():
  global slope
  slope = list(line.strip() for line in open('./input.txt'))
  toboggans = [[1,1], [1,3], [1,5], [1,7], [2,1]]
  
  runs = list(map(run_slope, toboggans))
  prod = math.prod(runs)
  
  print("Part 1: {}".format(runs[1]))
  print("Part 2: {}".format(prod))
  

if __name__ == '__main__':
  main()