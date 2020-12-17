#! /usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  part1, part2 = 0, 0 
    
  with open('./input.txt', 'r') as f:
    for line in f.read().split('\n\n'):
      s = [set(x) for x in line.splitlines()]
      part1 += len(set.union(*s))
      part2 += len(set.intersection(*s))
                
  print("Part 1: {}".format(part1))
  print("Part 2: {}".format(part2))


if __name__ == '__main__':
  main()