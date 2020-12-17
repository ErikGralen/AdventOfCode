#! /usr/bin/python3
# -*- coding: utf-8 -*-

def calc_ID(code):
  t = str.maketrans("FBLR", "0101")
  b = code.translate(t)
  return int(b,2)

def main():  
  mx, mn, sm = 0, 2000, 0

  with open('./input.txt', 'r') as f:
    for line in f.read().split('\n'):
        i = calc_ID(line)
        mx = max(i,mx)
        mn = min(i,mn)
        sm += i
        
  true_sum = int(mx*(mx+1)/2 - (mn-1)*(mn)/2)
  seat = true_sum - sm
                
  print("Part 1: {}".format(mx))
  print("Part 2: {}".format(seat))

if __name__ == '__main__':
  main()