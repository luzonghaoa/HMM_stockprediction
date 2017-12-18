import myHMM  
import numpy as np
import sys
import random

if sys.version_info.major == 3:
    xrange = range
hmm = myHMM.myHMM()
#s = [0,1]
a = np.array([[0.2,0.8],[0.6,0.4]])
b = np.array([[0.8,0.1,0.1],[0.1,0.6,0.3]])
pi = [0.5,0.5]
y = []
for i in range(0,10):
    y.append(random.randint(0,2))

x = hmm.HMMViterbi(a,b,y,pi)

print(x)