#!/usr/bin/env python3
from collections import deque
import csv

def BFS(transitions):


    return


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
            transitions.append(line)
        BFS(transitions)
                    

                
if __name__ == '__main__':
    main()