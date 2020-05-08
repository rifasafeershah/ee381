#The Simulation of a Continuous Uniform RV.
#Using the histogram available in Python.
#
import math
import random
import matplotlib.pyplot as plt #Alias is plt

n = 10000

x = [] #Empty List for uniform
y = [] #Empty List for expontial
Lambda = 0.5 #Parameter in expontial distribution

for i in range(n):
    r = random.uniform(0,1) #Discrete Uniform
    x.append(r) #List of uniformlly distributed random numbers
    e = (-1 / Lambda) * math.log(1 - r, math.e) #the inverse CDF
    y.append(e) #List of random exponentially distributed random numbers
#-------------------------------------------------------------------------
#Below is making histograms
b = max(x)
a = min(x)
R = b - a #The range of data

intervals = int(math.ceil(math.sqrt(n)))
width = (R / intervals) #Class Width

plt.subplot(2, 1, 1)
plt.hist(x, intervals, normed = width) #normed has been depricated
plt.subplot(2, 1, 2)
plt.hist(y, intervals, normed = width) #The graph of exponential RV
