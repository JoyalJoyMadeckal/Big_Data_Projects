#!/usr/bin/env python3
"""reducer.py"""

__authors__ = "Joyal Joy Madeckal - s3860476"

import sys

# Main program start
if __name__ == "__main__":
    current_node = None
    current_distance = 0

    for line in sys.stdin:
        # Extracting the node and distance
        node_id, distance = line.split(',')[0].strip(), line.split(',')[1].strip()
        
        # The block will reduce the data based on the distance of the nodes to the source.
        if current_node != node_id:
            # Emitting the data with lowest distance from the source.
            if current_node:
                print(f'{current_node}: {current_distance}')
            current_node = node_id
            current_distance = distance
        else:
            if current_distance > distance:
                current_distance = distance
    
    # Emitting the data for the last node in loop
    if current_node == node_id:
        print(f'{current_node}: {current_distance}')

        
        


