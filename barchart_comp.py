from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

pram =['m1', 'm2', 'chi_p', 'chi_eff', 'Mc','q', 'spin1']
N=7

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
  


lal_v=(8.322, 16.185, 5.2, 5.607, 29.673, 28.070, 50)

lal_e= (2.06, 33.83, 42, 29.673, 10.837, 58.596, 82.8)




fig, ax = plt.subplots()
rects1 = ax.bar(ind, lal_v, width, color='g', yerr=lal_e)

pycbc_v = (10.29, 23.73, 73.2, 18.457, 6.855, 38.947, 55.6)
pycbc_e = (2.00, 38.27, 54.6, 38.551, 11.751, 67.017, 79)  


rects2 = ax.bar(ind + width, pycbc_v, width, color='b', yerr=pycbc_e)

# add some text for labels, title and axes ticks
ax.set_ylabel('Percentage Error')
ax.set_title('Lal v Pycbc')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('m1', 'm2', 'chi_p', 'chi_eff', 'Mc','q', 'spin1'))

autolabel(rects1)
autolabel(rects2)

ax.legend('Lal', 'Pycbc')
plt.savefig("comp_test.png")
