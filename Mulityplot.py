import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

injected_value=0.5



def chi_p_1_MPE():
    data = []
    g = open('run88_data.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    mean_val_1=np.average(saved_chi_p_1)
    MPE_1 = (abs(mean_val_1 - injected_value) / injected_value) * 100
    return MPE_1

def chi_p_1_90PE():
    data = []
    g = open('run88_data.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    upper_90_1=np.percentile(saved_chi_p_1, 95)
    mean_val_1=np.average(saved_chi_p_1)
    PE_1 = (abs(upper_90_1 - injected_value) / injected_value) * 100
    return PE_1
run1MPE = chi_p_1_MPE()
run1PE = chi_p_1_90PE()
print(run1MPE,run1PE) 
   

