from __future__ import division
import numpy as np


#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest

g = open('run33_data.txt', 'r')

    
    #create empty list to store numerics of interest

data = []



for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
m1_a= [ x[28] for x in data]
m2_b =[x[31] for x in data ]
chi_p_c = [x[52] for x in data ]
chi_eff_d = [x[69] for x in data ]
mc_e = [x[61] for x in data ]
dis_f = [x[58] for x in data ]
ratio_g = [x[70] for x in data ]
spin1_h = [x[48] for x in data ]
spin2_i = [x[50] for x in data ]
#plt.figure(1)
a_u=np.percentile(m1_a, 95)
a_m=np.average(m1_a)
b_u=np.percentile(m2_b, 95)
b_m=np.average(m2_b)
c_u=np.percentile(chi_p_c, 95)
c_m=np.average(chi_p_c)
d_u=np.percentile(chi_eff_d, 95)
d_m=np.average(chi_eff_d)
e_u=np.percentile(mc_e, 95)
e_m=np.average(mc_e)
f_u=np.percentile(dis_f, 95)
f_m=np.average(dis_f)
g_u=np.percentile(ratio_g, 95)
g_m=np.average(ratio_g)
h_u=np.percentile(spin1_h, 95)
h_m=np.average(spin1_h)
i_u=np.percentile(spin2_i, 95)
i_m=np.average(spin2_i)



print(a_u,a_m,b_u,b_m,c_u,c_m,d_u,d_m,e_u,e_m,f_u,f_m,g_u,g_m,h_u,h_m,i_u,i_m)
