import numpy as np
from scipy.stats import bernoulli

sample_size=100000

prob_A=6/11
prob_B=5/11
prob_AorB=7/11


#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B= bernoulli.rvs(size= sample_size, p = prob_B)
sample_AorB= bernoulli.rvs(size= sample_size, p = prob_AorB)

A_nonzero = np.nonzero(sample_A == 1)
B_nonzero = np.nonzero(sample_B == 1)
AorB_nonzero = np.nonzero(sample_AorB == 1)
n_A= np.size(A_nonzero)
n_B= np.size(B_nonzero)
n_AorB= np.size(AorB_nonzero)

#calculating P(A intersection B):
prob_AB= (n_A + n_B - n_AorB)/sample_size
print("P(A intersection B) = ", prob_AB)

#calculating P(A|B) and P(B|A)
print("P(A|B) = ", prob_AB/prob_B)
print("P(B|A) = ", prob_AB/prob_A)