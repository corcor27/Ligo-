import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

injected_value=0.5
a = run88_data.txt

def chi_p_1():
    data = []
    g = open('a', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    upper_90_1=np.percentile(saved_chi_p_1, 95)
    mean_val_1=np.average(saved_chi_p_1)
    chi_p_1_MPE = (abs(mean_val_1 - injected_value) / injected_value) * 100
    chi_p_1_90PE = ( abs(upper_90_1 - injected_value) / injected_value) * 100
    return chi_p_1_MPE,chi_p_1_90PE
chi_p_file1 = chi_p_1 ()
print(chi_p_file1)

   

