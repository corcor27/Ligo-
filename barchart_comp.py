from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

pram =['m1', 'm2', 'chi_p', 'chi_eff', 'Mc','q', 'spin1']
N=7

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
  

#run14

lal_v=(8.322, 16.185, 5.2, 5.607, 29.673, 28.070, 2.59)
lal_e= (2.06, 33.83, 42, 29.673, 10.837, 58.596, 18.7)
pycbc_v = (10.29, 23.73, 73.2, 18.457, 6.855, 38.947, 1.03)
pycbc_e = (2.00, 38.27, 54.6, 38.551, 11.751, 67.017, 16.23)  

#run22

#lal_v=(2.893, 5.13, 24.8, 30.88, 1.521, 8.43, 3.29)
#lal_e= (2.48, 13.28, 48.2, 42.647, 4.371, 22.891, 5.17)
#pycbc_v = (6.26, 8.89, 79.6, 35.29, 1.913, 16.867, 17.529)
#pycbc_e = (2.27, 19.64, 71.44, 49.706, 4.57, 39.75, 7.411)  

#run31

#lal_v=(1.105, 9.74, 8.8, 37, 4.85, 11.2, 0.714)
#lal_e= (6.43, 24.98, 84.8, 78.5, 12.35, 32, 32.857)
#pycbc_v = (2.805, 15.38, 84.4, 51.5, 7.19, 18.4, 2.14)
#pycbc_e = (3.712, 24.78, 77.2, 77.5, 10.70, 36, 11.19)  




fig, ax = plt.subplots()
rects1 = ax.bar(ind, lal_v, width, color='g', yerr=lal_e, label = 'Lal inference')




rects2 = ax.bar(ind + width, pycbc_v, width, color='b', yerr=pycbc_e, label = 'Pycbc inference')

# add some text for labels, title and axes ticks
ax.set_ylabel('Percentage Error')
ax.set_title('Lal v Pycbc-RunB')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('m1', 'm2', 'chi_p', 'chi_eff', 'Mc','q', 'spin1'))
plt.ylim((0,200))
plt.xlabel('Parameters')
plt.legend(loc='upper left', fontsize=10.5)
plt.savefig("RunB_comparsions.png")
