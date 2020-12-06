#!/usr/bin/env python

with open('input.txt') as f:
    passports = f.read().splitlines()

all_passports = []
this_passport = []
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

#Put each passport in its own list. 
x = 0
while x < len(passports):
    #add items to each individual passport list
    if passports[x] == "":
        this_passport = []
    this_passport.extend(passports[x].split(' '))
    for item in this_passport:
        if item == '':
            this_passport.pop(this_passport.index(item))
    if this_passport not in all_passports:
        all_passports.append(this_passport)
    x += 1

new_passport_list = []
x = 0
for passport in all_passports:
    passport_dict = {}
    for item in passport:
        key = item.split(':')[0]
        value = item.split(':')[1]
        passport_dict[key] = value
    new_passport_list.append(passport_dict)

invalids = 0
for passport in new_passport_list:
    for field in req_fields:
        if field not in passport:
            print("{} is invalid.".format(passport))
            invalids += 1
            break

print("{} total passports".format(len(new_passport_list)))
print("{} invalid passports".format(invalids))
print("{} valid passports".format(len(new_passport_list) - invalids))