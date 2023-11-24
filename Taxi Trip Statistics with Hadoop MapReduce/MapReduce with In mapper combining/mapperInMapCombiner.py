#!/usr/bin/env python3
import sys
# Initialising the dictionary for storing taxi data.
taxi = dict()
# input comes from standard input STDIN
for line in sys.stdin:
    # Trimming the trailing and leading whitespaces
   line = line.strip()
   taxi_id, kilometers = [word.strip() for word in line.split(',')]
   if taxi_id in taxi.keys():
       taxi[taxi_id] = [taxi[taxi_id][0] + int(kilometers), taxi[taxi_id][1] + 1]
       continue 
   taxi[taxi_id] = [int(kilometers), 1]

for key in taxi.keys():
  # Emitting the key value pairs
  print(f'{key}\t{taxi[key][0]}\t{taxi[key][1]}')
  