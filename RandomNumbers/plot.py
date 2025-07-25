import numpy as np
from matplotlib import pyp 

numlist = np.loadtxt("linear_congruent_random_numbers.txt")

plt.hist(numlist, bins = 10)
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()
