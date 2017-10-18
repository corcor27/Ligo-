import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."


def chi_p_1()



data = []

#m1=24th index
#m2 = 27th index    
    
#print parameters    
    #loop over all lines the file and add each column to the list as a tuple

for line in g:
    data.append([float(x) for x in line.split()])
#add parameters as required
#    m1_freq= [ x[28] for x in data]
#    m2_freq =[x[31] for x in data ]
chi_p = [x[51] for x in data ]
#    chi_eff = [x[46] for x in data ]
#plt.figure(1)
