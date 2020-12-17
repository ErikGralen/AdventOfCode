#! /usr/bin/python3
# -*- coding: utf-8 -*-

commands = {
  "acc": lambda x, acc, i: (acc + x, i + 1),
  "jmp": lambda x, acc, i: (acc    , i + x),
  "nop": lambda x, acc, i: (acc    , i + 1)
}

def execute(instructions):
  i, acc, visited = 0, 0, set()

  while i < len(instructions):
    if i in visited:
      return acc, False
    visited.add(i)
    cmd, nbr = instructions[i].split()
    acc, i = commands[cmd](int(nbr), acc, i)
     
  return acc, True
  
def find_corruption(instructions):
  for j in range(len(instructions)):
    cmd, nbr = instructions[j].split()
    if cmd != "acc":
      instructions[j] = "jmp " + nbr if cmd == "nop" else "nop " + nbr
      acc, finished = execute(instructions)
      instructions[j] = cmd + " " + nbr
      if finished: return acc

def main():
  with open('./input.txt', 'r') as f:
    instructions = list(f.read().split('\n'))
     
  print("Part 1: {}".format(execute(instructions)[0]))
  print("Part 2: {}".format(find_corruption(instructions)))


if __name__ == '__main__':
  main()