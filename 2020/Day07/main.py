#! /usr/bin/python3
# -*- coding: utf-8 -*-
import re
from collections import defaultdict

parents = defaultdict(set)
children = defaultdict(dict)

def count_parents():
  visited = set()
  unvisited = parents["shiny gold"]

  while(unvisited):
    curr = unvisited.pop()
    unvisited.update(parents[curr])
    visited.add(curr)
  return len(visited)

def count_children(node, t=1):
  for b in children[node].keys():
    t += children[node][b] * count_children(b)
  return t

def main():
  with open('./input.txt', 'r') as f:
    for line in f.read().split('\n'):
      bag, bags = line.split(" bags contain ")
      for amount, name in re.findall(r"(?P<a>\d+|no) (?P<b>[a-z ]+) bag", bags):
        if amount.isdigit():
          parents[name].add(bag)
          children[bag][name] = int(amount)
                
  
  part1 = count_parents()
  part2 = count_children("shiny gold", 0)
  
  print("Part 1: {}".format(part1))
  print("Part 2: {}".format(part2))


if __name__ == '__main__':
  main()