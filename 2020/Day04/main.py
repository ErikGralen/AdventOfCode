#! /usr/bin/python3
# -*- coding: utf-8 -*-
import re, sys

def validate_year(year, low, high):
    return low <= int(year) <= high and len(year) ==4
    
fields = {
    "byr": lambda x: validate_year(x, 1920, 2002),
    "iyr": lambda x: validate_year(x, 2010, 2020),
    "eyr": lambda x: validate_year(x, 2020, 2030),
    "hgt": lambda x: ((x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or 
                      (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
    "hcl": lambda x:  re.match(r"^#[a-f\d]{6}$", x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x:  re.match(r"^\d{9}$", x)
}   

def main():
  has_fields = 0
  valid = 0
    
  with open('./input.txt', 'r') as f:
    for line in f.read().split('\n\n'):
      id = dict(re.findall(r"(?P<k>\S*):(?P<v>\S*)", line))
          
      if id.keys() >= fields.keys():
        has_fields += 1
        valid += all(func(id[field]) for field, func in fields.items())
                
  print("Part 1: {}".format(has_fields))
  print("Part 2: {}".format(valid))


if __name__ == '__main__':
  main()