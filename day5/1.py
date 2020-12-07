#!/usr/bin/env python

with open('input.txt') as f:
    seat_ids = f.read().splitlines()

def get_id(bsp):
    row_id = bsp[:7]
    col_id = bsp[-3:]
    final_row = 0
    final_col = 0

    t_row = 127
    b_row = 0
    for direction in row_id:
        if direction == 'F':
            cur_range = round((t_row - b_row) / 2)
            t_row = t_row - cur_range

        if direction == 'B':
            cur_range = round((t_row - b_row) / 2)
            b_row = b_row + cur_range
    
    if row_id[-1:] == 'F':
        final_row = b_row

    if row_id[-1:] == 'B':
        final_row = t_row

    t_col = 7
    b_col = 0
    for direction in col_id:
        if direction == 'L':
            cur_range = round((t_col - b_col) / 2)
            t_col = t_col - cur_range
        if direction == 'R':
            cur_range = round((t_col - b_col) / 2)
            b_col = b_col + cur_range

    if col_id[-1:] == 'L':
        final_col = b_col

    if col_id[-1:] == 'R':
        final_col = t_col

    res = final_row * 8 + final_col
    return res

id_list = []
for each in seat_ids:
    id_list.append(get_id(each))

print(max(id_list))

##Part2
max_list = []
for each in range(127 * 8 + 7):
    max_list.append(each)

for each in id_list:
    max_list.pop(max_list.index(each))

print(max_list)
#cheeze it by lookin' through the list to get part 2