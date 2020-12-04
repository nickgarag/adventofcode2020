#!/usr/bin/env python

with open('slope.txt') as f:
  slope = f.read().splitlines()



def get_trees(slope, down_interval, right_interval):
  row_len = len(slope[0])
  slope_size = len(slope)
  down = 0
  right = 0
  tree_count = 0
  dot_count = 0

  while down < slope_size:
    if right > row_len - 1:
      right_position = right - row_len
      right = 0
      right += right_position
    if slope[down][right] == '#':
      tree_count += 1
    if slope[down][right] == '.':
      dot_count += 1
    down += down_interval
    right += right_interval

  print("There are {} trees.".format(tree_count))
  print("There are {} dots.".format(dot_count))

  return tree_count

slope_list = [[1,1], [1,3], [1,5], [1, 7], [2,1]]
tree_list = []

for pair in slope_list:
  tree_list.append(get_trees(slope, *pair))
print(tree_list)

tree_result = 1
for tree in tree_list:
  tree_result = tree_result * tree
print(tree_result)
