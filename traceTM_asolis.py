#!/usr/bin/env python3
import collections
import sys
import csv
from typing import List
import time


#Main
def main():

    file_name = "a_plus.csv"
    with open(file_name, mode ='r')as file:
        csvFile = list(csv.reader(file))
        print(f"Machine: {', '.join(csvFile[0])}")
        inputString = ', '.join(csvFile[2])
        print(f"Initial String: {inputString}")
        startState = ', '.join(csvFile[4])
        acceptState = ', '.join(csvFile[5])
        rejectState = ', '.join(csvFile[6])
        transitions = []

        for line in csvFile[7:]:
                # with open('output_asolis4.txt', 'a') as file:
                #     file.write(f"Problem:{problemNum}\n")
            transitions.append(line)
        
        print(f"Transitions: {transitions}")
                    

                
if __name__ == '__main__':
    main()