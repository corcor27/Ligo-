from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

test=(1,2.3,3,4,5,6,6,7,7,88,9,)

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest


f = open('run32samples.txt', 'r')

    
    #create empty list to store numerics of interest

data = []

#m1=24th index
#m2 = 27th index    
    
#print parameters    
    #loop over all lines the file and add each column to the list as a tuple

for line in f:
    data.append([float(x) for x in line.split()])
#add parameters as required
m1_freq= [ x[24] for x in data]
#    m2_freq =[x[27] for x in data ]
#    chi_p = [x[46] for x in data ]
#    chi_eff = [x[46] for x in data ]
#plt.figure(1)
plt.hist(m1_freq,50, normed=True)
plt.xlabel('m1')
plt.ylabel('probability density')
plt.axis([70, 95, 0, 0.16])
plt.savefig("Run32_attempt2_mass1.png")
#plt.figure(2)
#plt.hist(m2_freq,50, normed=True)
#plt.xlabel('m2')
#plt.ylabel('probability density')

#plt.figure()
#plt.hist(chi_p,50, normed=True)
#plt.xlabel(r'$\chi_p$')
#plt.ylabel('probability density')
