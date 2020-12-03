#!/usr/bin/env python

report_entries = None

with open('input.txt') as f:
  report_entries = f.read().splitlines()

for entry in report_entries:
  for other_entry in report_entries:
    for other_other_entry in report_entries:
      entry = int(entry)
      other_entry = int(other_entry)
      other_other_entry = int(other_other_entry)
      summed = entry + other_entry + other_other_entry
      #print("{0} + {1} + {2} = {3}".format(entry, other_entry, other_other_entry, summed))
      if summed == 2020:
        print("{0} + {1} + {2} = {3}".format(entry, other_entry, other_other_entry, summed))
        print("{0} x {1} x {2} = {3}".format(entry, other_entry, other_other_entry, entry * other_entry * other_other_entry))
