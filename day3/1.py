#!/usr/bin/env python

with open('slope.txt') as f:
  slope = f.read().splitlines()

slope_size = len(slope)
down = 0
right = 0

tree_count = 0
dot_count = 0
while down < slope_size:
  if right == 33:
    right = 0
  print(down, right, slope[down][right])
  if slope[down][right] == '#':
    tree_count += 1
  if slope[down][right] == '.':
    dot_count += 1
  down += 1
  right += 3


print("There are {} trees.".format(tree_count))
print("There are {} dots.".format(dot_count))

    
    
