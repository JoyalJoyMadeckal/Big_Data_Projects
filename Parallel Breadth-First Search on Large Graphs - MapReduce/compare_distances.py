__authors__ = "Joyal Joy Madeckal - s3860476"

from mapper import getDistances

# Main program start
if __name__ == "__main__":
    # Getting the previous distances.
    distance = getDistances('distance.txt')
    # Getting the new distances from the current execution
    distance1 = getDistances('distance1.txt')
    
    # Emits whether the distances are the same.
    if len(distance) == len(distance1) and len([node for node in distance if node in distance1]) == len(distance):
        print(1)
    else:
        print(0)
