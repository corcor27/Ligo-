from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle


m1_a= np.loadtxt('mass1.txt')
m2_b =np.loadtxt('mass2.txt')
chi_p_c = np.loadtxt('chi_p.txt')
chi_eff_d = np.loadtxt('chi_eff.txt')
mc_e = np.loadtxt('mchirp.txt')
dis_f = np.loadtxt('distance.txt')
ratio_g = np.loadtxt('q.txt')
spin1_h = np.loadtxt('spin1_a.txt')
spin2_i = np.loadtxt('spin2_a.txt')
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
