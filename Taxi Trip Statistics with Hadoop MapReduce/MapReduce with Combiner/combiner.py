#!/usr/bin/env python3
import sys

current_taxi = None
current_trips = 0
current_kms = 0
taxi = None
# input comes from standard input STDIN
for line in sys.stdin:
    # Trimming the trailing and leading whitespaces
   line = line.strip()
   try:
      # Extracting the taxi and kilometers per trip
      taxi, kms, trips = line.split('\t')
      kms = int(kms)
      trips = int(trips)
   except ValueError:
        continue
   if current_taxi == taxi:
        current_trips += trips
        current_kms += kms
   else:
        if current_taxi:
                # Emitting the key value pairs
                print(f'{current_taxi}\t{current_kms}\t{current_trips}')
        current_trips = trips
        current_kms = kms
        current_taxi = taxi
if current_taxi == taxi:
  # Emitting the key value pairs
  print(f'{current_taxi}\t{current_kms}\t{current_trips}')