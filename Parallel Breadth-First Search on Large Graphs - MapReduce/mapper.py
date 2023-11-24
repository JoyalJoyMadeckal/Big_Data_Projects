#!/usr/bin/env python3
"""mapper.py"""

__authors__ = "Joyal Joy Madeckal - s3860476"

import sys

# The function reads the distance's file and convert it into a dictionary.
def getDistances(filepath):
    node_distance_list = []
    with open(filepath) as data:
        for line in data.readlines():
            node_distance_list.append((line.strip().split(':')[0], int(line.strip().split(':')[1])))
    return node_distance_list

# Main program start
if __name__ == "__main__":
    # Reading the node distances file.
    node_distances_map = getDistances('distance.txt')
    for line in sys.stdin:
        # Mapping the node id and outgoing links from current node.
        node_id, outgoing_nodes = line.strip().split(':')[0], (line.strip().split(':')[1]).split()
        # Getting the distance of the node from source
        node_distance = [node for node in node_distances_map if node[0] == node_id][0][1]
        # Emitting the current node data
        print("%s, %s" % (node_id, node_distance))
        # Emitting all the outgoing nodes and the condition will skip nodes with no outgoing links.
        if outgoing_nodes != ['none']:
            for node in outgoing_nodes:
                distance = node_distance + 1
                print("%s, %s" % (node, 9999 if distance > 9999 else distance))

