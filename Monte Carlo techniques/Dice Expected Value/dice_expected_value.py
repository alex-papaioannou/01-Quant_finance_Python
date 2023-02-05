import random
import numpy
import scipy.stats
numpy.set_printoptions(threshold=20)

# Dummy approach
N=1000
sum=0
for i in range(N):
    sample = random.randint(1,7)
    sum += sample
expected_value=sum/N
print("The expected value of a fair dice is:", expected_value)

# More elegant approach
N = 1000
roll = numpy.zeros(N, dtype=int)
expectation = numpy.zeros(N)
for i in range(N):
    roll[i] = numpy.random.randint(1, 7)
for i in range(1, N):
    expectation[i] = numpy.mean(roll[0:i])
