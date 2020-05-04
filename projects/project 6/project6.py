'''
EE 381 spring 2020 - The year of the Corona virus!
Project 6
Name: Rifa Safeer Shah
I.D. #: 017138353
Start Date: 5/4/2020
End Date: 5/4/2020
Description: Simulation of a Markov walk
'''

p = float(input("Enter probabilty of a jump. "))
S = int(input("Enter the starting position. "))
N = int(input("Enter the boundary position. "))
J = int(input("Enter the number of jumps wanted. "))
#----------------------------------------------------
import random
#----------------------------------------------------
for k in range(J):
    
    r = random.uniform(0,1)

    if S == 0: # Left Boundary
        S = 1
    elif S == N: # Right Boundary
        S = N - 1
    elif (S < N) and (S > 0): # Middle
        if r < p: # Bernoulli
            S = S + 1
        else:
            S = S - 1
    print(S) # Watch the particle move.
