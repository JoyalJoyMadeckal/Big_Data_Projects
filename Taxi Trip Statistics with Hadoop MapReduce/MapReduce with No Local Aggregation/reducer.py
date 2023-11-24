#!/usr/bin/env python3
import sys
# Initialising some basic variables
current_taxi = None
current_trips = 0
current_kms = 0
taxi = None
# input comes from STDIN
for line in sys.stdin:
   # Trimming the trailing and leading whitespaces
   line = line.strip()
   # Extracting the taxi and kilometers per trip
   taxi, kms = line.split('\t')
   try:
      kms = int(kms)
   except ValueError:
        continue
   if current_taxi == taxi:
        current_trips += 1
        current_kms += kms
   else:
        if current_taxi:
                # Emitting the key value pairs
                print(f'{current_taxi}, {current_trips}, {round(current_kms/current_trips, 2)}')
        current_trips = 1
        current_kms = kms
        current_taxi = taxi
if current_taxi == taxi:
  # Emitting the key value pairs
  print(f'{current_taxi}, {current_trips}, {round(current_kms/current_trips, 2)}')