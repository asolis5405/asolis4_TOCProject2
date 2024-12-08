#!/usr/bin/env python3
import csv
from collections import deque
import math


def test_input(start_state, accept_state, reject_state, transitions, input_string, max_depth):
    #initialize the configuration
    initial_config = ("", start_state, input_string)
    #use deque to store paths
    queue = deque([[initial_config]])
    #count transitions made
    steps = 0
    #keep track of depth
    max_depth_reached = 0
    #count total transitions
    total_transitions = 0
    #count any non-leaf nodes for the calculation of degree of nondeterminism
    non_leaf_nodes = 0

    while queue:
        #get next path
        path = queue.popleft()
        #get current configuration
        current_config = path[-1]
        left, state, right = current_config
        #update max_depth
        max_depth_reached = max(max_depth_reached, len(path) - 1)

        #check for accept state
        if state == accept_state:
            print(f"String accepted in {steps} transitions.")
            print(f"Depth of tree: {max_depth_reached}")
            print_nondeterminism(total_transitions, non_leaf_nodes)
            print_path(path)
            return

        #check for reject state or if max_depth has been reached
        if state == reject_state or steps >= max_depth:
            continue

        #get next symbol and create transition key
        head_symbol = right[0] if right else "_"
        key = (state, head_symbol)

        #check if a transition can be made
        if key in transitions:
            #increase non-leaf node count if it is able to transition
            non_leaf_nodes += 1

            for next_state, write_symbol, direction in transitions[key]:
                #create the new configuration
                new_left = left
                new_right = right

                #move in the correct direction
                if direction == "L":
                    new_left = left[:-1] if left else ""
                    new_right = left[-1] + write_symbol + right[1:] if left else "_" + right[1:]
                elif direction == "R":
                    new_left = left + write_symbol
                    new_right = right[1:] if len(right) > 1 else ""
                else:  #if no direction
                    new_right = write_symbol + right[1:]

                new_config = (new_left, next_state, new_right)
                #add new path to queue and increment transitions
                queue.append(path + [new_config])
                total_transitions += 1

        steps += 1

    #if accept is not reached
    print(f"String rejected or max depth reached.")
    print(f"Depth of tree: {max_depth_reached}")
    print(f"Total transitions: {total_transitions}")
    print_nondeterminism(total_transitions, non_leaf_nodes)

#function to find the degree of nondeterminism
def print_nondeterminism(total_transitions, non_leaf_nodes):
    if non_leaf_nodes == 0:
        print("Degree of nondeterminism: 0")
    else:
        degree = math.ceil(total_transitions / non_leaf_nodes)
        print(f"Degree of nondeterminism: {degree}")

#function to find the sequence of configurations from start to finish
def print_path(path):
    print("Path of configurations:")
    for config in path:
        left, state, right = config
        print(f"{left}[{state}]{right}")

# Main function
def main():
    file_name = "a_plus.csv"  #CSV file
    with open(file_name, mode='r') as file:
        csvFile = list(csv.reader(file))

        print(f"Machine Name: {', '.join(csvFile[0])}")

        input_string = "aaa"  #choose input string
        print(f"Initial String: {input_string}")

        start_state = csvFile[4][0]
        accept_state = csvFile[5][0]
        reject_state = csvFile[6][0]

        transitions = {}
        for line in csvFile[7:]:
            current_state, read_symbol, next_state, write_symbol, direction = line
            key = (current_state, read_symbol)
            if key not in transitions:
                transitions[key] = []
            transitions[key].append((next_state, write_symbol, direction))

    max_depth = 50

    #run TM
    test_input(start_state, accept_state, reject_state, transitions, input_string, max_depth)

if __name__ == '__main__':
    main()

# with open('output_asolis4.txt', 'a') as file:
                #     file.write(f"Problem:{problemNum}\n")