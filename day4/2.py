#!/usr/bin/env python
import re

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

invalids = []
for passport in new_passport_list:
    for field in req_fields:
        if field not in passport:
            print("{} is invalid.".format(passport))
            invalids.append(passport)
            break

print("{} total passports".format(len(new_passport_list)))
print("{} invalid passports".format(len(invalids)))
print("{} valid passports".format(len(new_passport_list) - len(invalids)))

def check_byr(passport):
    if 'byr' in passport:
        try:
            byr = int(passport['byr'])
        except:
            return False
        if byr >= 1920 and byr <= 2002:
            return True
    return False

def check_iyr(passport):
    if 'iyr' in passport:
        try:
            iyr = int(passport['iyr'])
        except:
            return False
        if iyr >= 2010 and iyr <= 2020:
            return True
    return False

def check_eyr(passport):
    if 'eyr' in passport:
        try:
            eyr = int(passport['eyr'])
        except:
            return False
        if eyr >= 2020 and eyr <= 2030:
            return True
    return False

def check_hgt(passport):
    if 'hgt' in passport:
        hgt = passport['hgt']
        if hgt[-2:] == 'cm':
            try:
                cm = int(hgt[:-2])
            except:
                return False
            if cm >= 150 and cm <= 193:
                return True
        elif hgt[-2:] == 'in':
            try:
                inch = int(hgt[:-2])
            except:
                return False
            if inch >= 59 and inch <= 76:
                return True
    return False

def check_hcl(passport):
    hclre = re.compile(r'[^a-f0-9.]')
    if 'hcl' in passport:
        hcl = passport['hcl']
        if hcl[0] != '#':
            return False
        if len(hcl) != 7:
            return False
        if hclre.search(hcl[1:]):
            return False
    return True
        

def check_ecl(passport):
    color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if 'ecl' in passport:
        ecl = passport['ecl']
        if ecl in color_list:
            return True
    return False

def check_pid(passport):
    if 'pid' in passport:
        pid = passport['pid']
        try:
            int(pid)
        except:
            return False
        if len(pid) == 9:
            return True
    return False

def check_cid(poassport):
    pass

for passport in invalids:
    if passport in new_passport_list:
        new_passport_list.pop(new_passport_list.index(passport))

valid_passports = 0

for passport in new_passport_list:
    if check_byr(passport) and check_iyr(passport) and check_eyr(passport) and check_hgt(passport) and check_hcl(passport) and check_ecl(passport) and check_pid(passport):
        valid_passports += 1

print("There are {} valid passports".format(valid_passports))
