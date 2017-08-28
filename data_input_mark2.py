from __future__ import division
import numpy as np


#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest

g = open('run88_data.txt', 'r')

    
    #create empty list to store numerics of interest

data = []



for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
m1_a= [ x[28] for x in data]
m2_b =[x[31] for x in data ]
chi_p_c = [x[52] for x in data ]
chi_eff_d = [x[46] for x in data ]
mc_e = [x[46] for x in data ]
dis_f = [x[46] for x in data ]
ratio_g = [x[46] for x in data ]

#plt.figure(1)
a_u=np.percentile(m1_a, 95)
a_m=np.average(m1_a)
b_u=np.percentile(m2_b, 95)
b_m=np.average(m2_b)
c_u=np.percentile(chi_p_c, 95)
c_m=np.average(chi_p_c)
d_u=np.percentile(chi_eff_d, 95)
d_m=np.average(chi_eff_d)
e_u=np.percentile(chi_p_c, 95)
e_m=np.average(chi_p_c)
f_u=np.percentile(chi_eff_d, 95)
f_m=np.average(chi_eff_d)

a1 = 


print(Lal_upper_90,mean_val)
