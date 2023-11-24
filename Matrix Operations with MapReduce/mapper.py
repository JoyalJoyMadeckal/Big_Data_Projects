#!/usr/bin/env python3
import sys

# Storing the information about matrix sizes
nrow_M = int(sys.argv[1])
ncol_M = int(sys.argv[2])
nrow_N = int(sys.argv[3])
ncol_N = int(sys.argv[4])
nrow_X = int(sys.argv[5])
ncol_X = int(sys.argv[6])

# Main program start
if __name__ == "__main__":
    # Reading all the input files line by line
    for line in sys.stdin:
        # Extracting the values from the line
        id, row, values = int(line.split(',')[0]), int(line.split(',')[1]), list(map(int, line.split(',')[2:]))
        # Looping through each element of the matrix and emitting the values based on the id of the matrices.
        for index, value in enumerate(values):
            if id == 1:
                for i in range(ncol_N):
                    print('%s\t%s\t%s\t%s' % (row,i,index,value))
                continue
            if id == 2:
                for i in range(nrow_M):
                    print('%s\t%s\t%s\t%s' % (i,index,row,value))
            if id == 3:
                    # Added the value 999999 so that the value will come at the end after sorting for an element
                    # in the resultant matrix. This is the value to be considered for subtraction.
                    print('%s\t%s\t%s\t%s' % (row,index,999999,value))
        

