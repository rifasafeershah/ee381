'''
EE 381 Spring 2020 Proj 3B
Name: Rifa Safeer Shah
I.D. #: 017138353
Start Date: 02-19-2020
End Date: 02-24-2020
Description: Simulate a Bernoulli
Random Variable and use it to
make a Markov prorcess.
'''

step = [] #This is where the particle has been.

import random

p_A = float(input("Enter the probability of going from '0' to '1'. "))

p_B = float(input("Enter the probability of going from '1' to '0'. "))

S = int(input("Enter either '0' or '1' for the starting location. "))
step.append(S)
#-------------------------------------------------------------------------------
for i in range(24):
    r = random.uniform(0, 1)
    if  r < p_A and S == 0:
        S = 1
    elif r < p_B and S == 1:
        S = 0
    step.append(S)
#-------------------------------------------------------------------------------

for i in step:
    print(i, end = " ")
