#!/usr/bin/env python

passwords = None

with open('passwords.txt') as f:
  passwords = f.read().splitlines()

total_valid = 0

for password in passwords:
  policy = password.split(": ")[0]
  match_letter = policy[-1:]
  match_letter_min = policy.split("-")[0]
  match_letter_max = policy.split("-")[1].split(" ")[0]

  password = password.split(": ")[1]
  letter_count = 0

  for letter in password:
    if letter == match_letter:
      letter_count += 1

  if int(match_letter_min) <= letter_count <= int(match_letter_max):
    total_valid += 1

print("{} valid passwords.".format(total_valid))