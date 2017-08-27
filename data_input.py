from __future__ import division
import numpy as np


#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest

g = open('run93_data2.txt', 'r')

    
    #create empty list to store numerics of interest

data = []



for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p = [x[52] for x in data ]
#    chi_eff = [x[46] for x in data ]
#plt.figure(1)


Lal_upper_90=np.percentile(chi_p, 95)

mean_val=np.average(chi_p)
print(Lal_upper_90,mean_val)
