from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest

g = open('run32samples.txt', 'r')
data = []
a = open('run89_data.txt', 'r')
data1 = []
b = open('run92_data.txt', 'r')
data2 = []
c = open('run95_data.txt', 'r')
data3 = []
d = open('run98_data.txt', 'r')
data4 = []


    
for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p = [x[52] for x in data ]
#    chi_eff = [x[46] for x in data ]
#plt.figure(1)
for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p1 = [x[52] for x in data ]
for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p2 = [x[52] for x in data ]
for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p3 = [x[52] for x in data ]
for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p4 = [x[52] for x in data ]



Lal_upper_90=np.percentile(chi_p, 95)
Lal_lower_90=np.percentile(chi_p, 5)
#pycbc_upper_90=np.percentile(pycbc_data, 95)
#pycbc_lower_90=np.percentile(pycbc_data, 5)
plt.hist(chi_p,50, facecolor='green', normed=True)
plt.hist(chi_p1,50, facecolor='b', normed=True)
plt.hist(chi_p2,50, facecolor='k', normed=True)
plt.hist(chi_p3,50, facecolor='y', normed=True)
plt.hist(chi_p4,50, facecolor='green', normed=True)
#plt.hist(pycbc_data,50, normed=True, color='b')
plt.xlabel('chi_p')
#plt.axvline(x=Lal_lower_90,linewidth=2,linestyle='dashed',color='m')
#plt.axvline(x=Lal_upper_90,linewidth=2,linestyle='dashed',color='m')
#plt.axvline(x=pycbc_lower_90,linewidth=2,linestyle='dashed',color='k')
#plt.axvline(x=pycbc_upper_90,linewidth=2,linestyle='dashed',color='k')
plt.axvline(x=0.5,linewidth=2, color='r')
plt.axis([0, 1, 0,8 ])
plt.ylabel('probability density')
plt.savefig("mix-plot3_lal.png")



#plt.figure(2)
#plt.hist(m2_freq,50, normed=True)
#plt.xlabel('m2')
#plt.ylabel('probability density')

#plt.figure()
#plt.hist(chi_p,50, normed=True)
#plt.xlabel(r'$\chi_p$')
#plt.ylabel('probability density')
