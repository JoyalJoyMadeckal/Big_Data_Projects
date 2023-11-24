#!/usr/bin/env python3
import sys

# Initialising the variables
current_row = None
current_col = None
current_value = None
row = None
column = None
values =  []

# The method will calculate the value of each element in the resultant matrix
def calculate_element(data):
    summed_value = 0
    for index in range(0, len(data), 2):
        try:
            # Summing up the values after taking the product of the respective elements
            summed_value += int(data[index]) * int(data[index + 1])
        except:
            continue
    # Returning after subtracting respective value from the summed values
    return(int(data[-1]) - summed_value)

# Main program start
if __name__ == "__main__":
    for line in sys.stdin:
        if line:
            # Extracting the required values after reading the mapper input line
            row, column, value = line.split('\t')[0], line.split('\t')[1], line.split('\t')[3]

            # Reading the values contributing to a single element in the resultant matrix
            if current_row == row and current_col == column:
                values.append(value)
            else:
                if current_row and current_col:
                    # Calculating the element value for the resultant matrix
                    element_value = calculate_element(values)
                    # Emiitting the element value for an element in the resultant matrix
                    print('%s\t%s\t%s' % (current_row,current_col,element_value))
                values =  []
                current_row = row
                current_col = column
                values.append(value)

    # Calculating the value for the last element of the resultant matrix
    if current_row and row and current_row == row and current_col == column:
        element_value = calculate_element(values)
        print('%s\t%s\t%s' % (current_row,current_col,element_value))