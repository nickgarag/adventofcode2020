#!/usr/bin/env python

report_entries = None

with open('input.txt') as f:
  report_entries = f.read().splitlines()

for entry in report_entries:
  for other_entry in report_entries:
    entry = int(entry)
    other_entry = int(other_entry)
    summed = entry + other_entry
    #print("{0} + {1} = {2}".format(entry, other_entry, summed))
    if summed == 2020:
      print("{0} + {1} = {2}".format(entry, other_entry, summed))
      print("{0} x {1} = {2}".format(entry, other_entry, entry * other_entry))
