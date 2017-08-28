from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

pram =['m1', 'm2', 'chi_p', 'chi_eff', 'Mc', 'Distance', 'q', 'spin1']
lal_v=[8.322, 16.185, 5.2, 5.607, 29.673, 28.070, 50]
lal_e=[2.06, 33.83, 42, 29.673, 10.837, 58.596, 82.8] 
pycbc_v=[10.29, 23.73, 73.2, 18.457, 6.855, 38.947, 55.6]
pycbc_e=[2.00, 38.27, 54.6, 38.551, 11.751, 67.017, 79]       

N=8
ind = np.arange(N)    # the x locations for the groups
width = 0.4
fig, ax = plt.subplots()

lal = ax.bar(ind, lal_v,width, color='b', label = 'LAL')                  #percentage error
#pycbc = ax.bar(ind + width, pycbc_mass1 , width, color='y')                           #actual values
pycbc = ax.bar(ind + width, pycbc_v, width, color='r', label = 'PyCBC')      #percentage errors


ax.set_ylabel('percentage error')
ax.set_xlabel('parameters')
ax.set_title('pycbc v lal percentage errors')
ax.set_xticks(ind + width)
ax.set_xticklabels (param)
plt.legend()
plt.savefig("comp_test.png")
