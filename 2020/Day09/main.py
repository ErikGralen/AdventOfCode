#! /usr/bin/python3
# -*- coding: utf-8 -*-

def is_valid(numbers, number):
  visited = set()
  for n in numbers:
    if number - n in visited:
      return True
    visited.add(n)
  return False

def main():
  with open('./input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]
    
  i = 25
  while is_valid(numbers[i-25 : i], numbers[i]):
    i += 1
  invalid = numbers[i]
  print("Part 1: {}".format(invalid))

  tail, head, rolling_sum = 0, 0, numbers[0]
  while rolling_sum != invalid:
    if rolling_sum < invalid:
      head += 1
      rolling_sum += numbers[head]
    else:
      rolling_sum -= numbers[tail]
      tail += 1
    
  ans = min(numbers[tail:head]) + max(numbers[tail:head])
  print("Part 2: {}".format(ans))

if __name__ == '__main__':
  main()