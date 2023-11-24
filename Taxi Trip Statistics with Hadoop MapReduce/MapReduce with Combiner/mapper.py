#!/usr/bin/env python3
import sys
# input comes from standard input STDIN
for line in sys.stdin:
    # Trimming the trailing and leading whitespaces
    line = line.strip()
    # Extracting the taxi and kilometers per trip
    taxi, kms = [word.strip() for word in line.split(',')]
    # Emitting the key-value pairs
    print(f'{taxi}\t{kms}\t1')