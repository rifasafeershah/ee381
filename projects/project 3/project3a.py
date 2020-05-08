'''
EE 381 Spring 2020 Proj 3A
Name: Rifa Safeer Shah
I.D. #: 017138353
Start Date: 02-19-2020
End Date: 02-24-2020
Description: Simulate a Bernoulli
Random Variable and use it to
make a Markov process.
'''
import random

p = float(input('Enter the probability of success. '))
T = int(input('Enter number of trials. '))

for j in range(T):

    r = random.uniform(0, 1)
    if r < p:
        print('1', end = ' ') #Success
    else:
        print('0', end = ' ') #Failure
