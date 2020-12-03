#!/usr/bin/env python

passwords = None

with open('passwords.txt') as f:
  passwords = f.read().splitlines()

total_valid = 0

for password in passwords:
  policy = password.split(": ")[0]
  match_letter = policy[-1:]
  match_letter_pos1 = policy.split("-")[0]
  match_letter_pos2 = policy.split("-")[1].split(" ")[0]

  pos1 = int(match_letter_pos1) - 1
  pos2 = int(match_letter_pos2) - 1

  password = password.split(": ")[1]
  if password[pos1] == match_letter and password[pos2] != match_letter:
    total_valid += 1
  elif password[pos1] != match_letter and password[pos2] == match_letter:
    total_valid += 1
  else:
    #nomatch
    pass

print("{} total valid password".format(total_valid))
    
