# asolis4_TOCProject2
## Team name: 
asolis4
## Names of all team members: 
Anaregina Solis
## Link to github repository:
https://github.com/asolis5405/asolis4_TOCProject2.git
## Which project options were attempted
Program 1: Tracing NTM Behavior
## Approximately total time spent on project: 
8 hours
## The language you used, and a list of libraries you invoked.
Python: csv, collections, math
## How would a TA run your program (did you provide a script to run a test case?)
On the file you can modify the csv file being read in as well as the input string you would like to test. Once you have saved the file you can type the following in the command line:
- chmod +x ./traceTM_asolis4.py
- ./traceTM_asolis4.py
## A brief description of the key data structures you used, and how the program functioned.
The key data structures I used were a dictionary and a deque. The dictionary maps pairs of a state and input symbol to a list of possible transitions. This dictionary defines how the machine moves between states based on the symbol read from the tape. The deque is used to store paths representing the sequence of configurations the TM explores, enabling efficient breadth-first traversal of all possible paths. Each path is a list of configurations, where each configuration is a tuple consisting of the tape's left side, the current state, and the tape's right side. The program functions by simulating a non-deterministic Turing Machine. It explores all possible paths until either an accept state is reached, a reject state is reached, or the maximum depth is met. 
## A discussion as to what test cases you added and why you decided to add them
I used the following test cases:
- a_plus.csv : This test case came from Professor Kogge and it tests for strings that belong to the language a+. With this test case, my code accepted the string “aaaaa” and rejected “aaaba” which tells me my code worked correctly. 
- abc_star.csv : This test case came from Professor Kogge and it tests for strings that belong to the language a*b*c*. With this test case, my code accepted the string “aabbcc” and rejected “ajc” which tells me my code worked correctly.
- 10plus1.csv : I wrote this test case and it tests for strings that belong to the language 1(0+)1. With this test case, my code accepted the string “10001” and rejected “11” which tells me my code worked correctly.
- equal_01s.csv: This test case came from Professor Kogge and it tests for strings that belong to the language 0^n1^n. With this test case, my code accepted the string “0011” and rejected “011” which tells me my code worked correctly.
## An analysis of the results, What was the approximate complexity of your program?
No timings or plots were called for. I would say the approximate complexity of my program is O(n).
## A description of how you managed the code development and testing.
I managed the code development by using print statements to keep track of how the csv file was being read in, how the transitions in the dictionary were being processed, and what each configuration looked like along the way. This really helped solve issues faster since I could see any errors being made. Wherever I tested a csv file and got incorrect output I would mainly add print statements to pinpoint exactly where the code went wrong. 
## Did you do any extra programs, or attempted any extra test cases
I did attempt an extra test case however it was very similar to one I was already using so I decided to not add it to my final repository. I also attempted another test case for the language a^nb^2n, however, I was unable to get the transitions to work properly. 

