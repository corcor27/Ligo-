from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest

g = open('run89_data.txt', 'r')

    
    #create empty list to store numerics of interest

data = []



for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p = [x[61] for x in data ]
#    chi_eff = [x[46] for x in data ]
#plt.figure(1)

#pycbc_data= np.loadtxt('run32_chi_p.txt')

Lal_upper_90=np.percentile(chi_p, 95)
Lal_lower_90=np.percentile(chi_p, 5)
#pycbc_upper_90=np.percentile(pycbc_data, 95)
#pycbc_lower_90=np.percentile(pycbc_data, 5)
plt.hist(chi_p,50, facecolor='green', normed=True, 'Lal')
#plt.hist(pycbc_data,50, normed=True, color='b')
plt.xlabel('mc')
plt.axvline(x=Lal_lower_90,linewidth=2,linestyle='dashed',color='m',label = '90% interval')
plt.axvline(x=Lal_upper_90,linewidth=2,linestyle='dashed',color='m')
#plt.axvline(x=pycbc_lower_90,linewidth=2,linestyle='dashed',color='k')
#plt.axvline(x=pycbc_upper_90,linewidth=2,linestyle='dashed',color='k')
plt.axvline(x=21.2,linewidth=2, color='r',label = 'Injected value')
plt.axis([15, 30, 0, 0.8])
plt.ylabel('probability density')
plt.savefig("Run89-mc.png")



#plt.figure(2)
#plt.hist(m2_freq,50, normed=True)
#plt.xlabel('m2')
#plt.ylabel('probability density')

#plt.figure()
#plt.hist(chi_p,50, normed=True)
#plt.xlabel(r'$\chi_p$')
#plt.ylabel('probability density')
