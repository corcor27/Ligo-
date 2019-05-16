import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

injected_value=0.75
m_c = 13.32
Incliations = [0,10,20,30,40,50,60,70,80]
#manually set injection value
#two functions for each text.file, allowing the creations for MPE and 90PE parameter

def chi_p_1_MPE():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    mean_val_1=np.average(saved_chi_p_1)
    MPE_1 = (abs(mean_val_1 - injected_value) / injected_value) * 100
    return MPE_1

def chi_p_1_90PE():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    upper_90_1=np.percentile(saved_chi_p_1, 95)
    mean_val_1=np.average(saved_chi_p_1)
    PE_1 = (abs(upper_90_1 - injected_value) / injected_value) * 100
    return PE_1

def chi_p_2_MPE():
    data = []
    f = open('M40_INC_10.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    mean_val_2=np.average(saved_chi_p_2)
    MPE_2 = (abs(mean_val_2 - injected_value) / injected_value) * 100
    return MPE_2

def chi_p_2_90PE():
    data = []
    f = open('M40_INC_10.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    upper_90_2=np.percentile(saved_chi_p_2, 95)
    mean_val_2=np.average(saved_chi_p_2)
    PE_2 = (abs(upper_90_2 - injected_value) / injected_value) * 100
    return PE_2

def chi_p_3_MPE():
    data = []
    f = open('M40_INC_20.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    mean_val_3=np.average(saved_chi_p_3)
    MPE_3 = (abs(mean_val_3 - injected_value) / injected_value) * 100
    return MPE_3

def chi_p_3_90PE():
    data = []
    f = open('M40_INC_20.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    upper_90_3=np.percentile(saved_chi_p_3, 95)
    mean_val_3=np.average(saved_chi_p_3)
    PE_3 = (abs(upper_90_3 - injected_value) / injected_value) * 100
    return PE_3

def chi_p_4_MPE():
    data = []
    f = open('M40_INC_30.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    mean_val_4=np.average(saved_chi_p_4)
    MPE_4 = (abs(mean_val_4 - injected_value) / injected_value) * 100
    return MPE_4

def chi_p_4_90PE():
    data = []
    f = open('M40_INC_30.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    upper_90_4=np.percentile(saved_chi_p_4, 95)
    mean_val_4=np.average(saved_chi_p_4)
    PE_4 = (abs(upper_90_4 - injected_value) / injected_value) * 100
    return PE_4

def chi_p_5_MPE():
    data = []
    f = open('M40_INC_40.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    mean_val_5=np.average(saved_chi_p_5)
    MPE_5 = (abs(mean_val_5 - injected_value) / injected_value) * 100
    return MPE_5

def chi_p_5_90PE():
    data = []
    f = open('M40_INC_40.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    upper_90_5=np.percentile(saved_chi_p_5, 95)
    mean_val_5=np.average(saved_chi_p_5)
    PE_5 = (abs(upper_90_5 - injected_value) / injected_value) * 100
    return PE_5

def chi_p_6_MPE():
    data = []
    f = open('M40_INC_50.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    mean_val_6=np.average(saved_chi_p_6)
    MPE_6 = (abs(mean_val_6 - injected_value) / injected_value) * 100
    return MPE_6

def chi_p_6_90PE():
    data = []
    f = open('M40_INC_50.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    upper_90_6=np.percentile(saved_chi_p_6, 95)
    mean_val_6=np.average(saved_chi_p_6)
    PE_6 = (abs(upper_90_6 - injected_value) / injected_value) * 100
    return PE_6

def chi_p_7_MPE():
    data = []
    f = open('M40_INC_60.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    mean_val_7=np.average(saved_chi_p_7)
    MPE_7 = (abs(mean_val_7 - injected_value) / injected_value) * 100
    return MPE_7

def chi_p_7_90PE():
    data = []
    f = open('M40_INC_60.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    upper_90_7=np.percentile(saved_chi_p_7, 95)
    mean_val_7=np.average(saved_chi_p_7)
    PE_7 = (abs(upper_90_7 - injected_value) / injected_value) * 100
    return PE_7
def chi_p_8_MPE():
    data = []
    f = open('M40_INC_70.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    mean_val_8=np.average(saved_chi_p_8)
    MPE_8 = (abs(mean_val_8 - injected_value) / injected_value) * 100
    return MPE_8

def chi_p_8_90PE():
    data = []
    f = open('M40_INC_70.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    upper_90_8=np.percentile(saved_chi_p_8, 95)
    mean_val_8=np.average(saved_chi_p_8)
    PE_8 = (abs(upper_90_8 - injected_value) / injected_value) * 100
    return PE_8

def chi_p_9_MPE():
    data = []
    f = open('M40_INC_80.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    mean_val_9=np.average(saved_chi_p_9)
    MPE_9 = (abs(mean_val_9 - injected_value) / injected_value) * 100
    return MPE_9

def chi_p_9_90PE():
    data = []
    f = open('M40_INC_80.0.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    upper_90_9=np.percentile(saved_chi_p_9, 95)
    mean_val_9=np.average(saved_chi_p_9)
    PE_9 = (abs(upper_90_9 - injected_value) / injected_value) * 100
    return PE_9

def chi_p_1():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_1 = [x[52] for x in data ]
    return Chi_p_1 

def chi_p_2():
    data = []
    g = open('M40_INC_50.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_2 = [x[52] for x in data ]
    return Chi_p_2     

def chi_p_3():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_3 = [x[61] for x in data ]
    return Chi_p_3 

def chi_p_4():
    data = []
    g = open('M40_INC_50.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_4 = [x[61] for x in data ]
    return Chi_p_4 


chi_p_INC_0 = chi_p_1()
INC_0_upper_90=np.percentile(chi_p_INC_0, 95)
INC_0_lower_90=np.percentile(chi_p_INC_0, 5)

chi_p_INC_10 = chi_p_2()
INC_10_upper_90=np.percentile(chi_p_INC_10, 95)
INC_10_lower_90=np.percentile(chi_p_INC_10, 5)

chi_p_INC_20 = chi_p_3()
INC_20_upper_90=np.percentile(chi_p_INC_20, 95)
INC_20_lower_90=np.percentile(chi_p_INC_20, 5)

chi_p_INC_30 = chi_p_4()
INC_30_upper_90=np.percentile(chi_p_INC_30, 95)
INC_30_lower_90=np.percentile(chi_p_INC_30, 5)



# recovered values from functions 

run1MPE = chi_p_1_MPE()
run1PE = chi_p_1_90PE()
run2MPE = chi_p_2_MPE()
run2PE = chi_p_2_90PE()
run3MPE = chi_p_3_MPE()
run3PE = chi_p_3_90PE()
run4MPE = chi_p_4_MPE()
run4PE = chi_p_4_90PE()
run5MPE = chi_p_5_MPE()
run5PE = chi_p_5_90PE()
run6MPE = chi_p_6_MPE()
run6PE = chi_p_6_90PE()
run7MPE = chi_p_7_MPE()
run7PE = chi_p_7_90PE()
run8MPE = chi_p_8_MPE()
run8PE = chi_p_8_90PE()
run9MPE = chi_p_9_MPE()
run9PE = chi_p_9_90PE()



# now have values sorted into list

a = [run1MPE,run2MPE,run3MPE,run4MPE,run5MPE,run6MPE,run7MPE,run8MPE,run9MPE]
ae = [run1PE,run2PE,run3PE,run4PE,run5PE,run6PE,run7PE,run8PE,run9PE]

fig = plt.figure()

ax1 = fig.add_subplot(321)
ax1.errorbar(x=Incliations, y=a, yerr=ae, fmt='o', color='g', label = 'Incliation ranges')
ax1.legend(loc='lower right', fontsize=10.5)
ax1.set_title('Inclination_scatter')
ax1.set_ylabel('Precentage error (%)', fontsize=12)
ax1.set_xlabel('Inclination (Degrees)', fontsize=12)
ax1.axis([-10, 90, -15, 25])

ax2 = fig.add_subplot(322)
ax2.plot(Incliations, a, linewidth=2,linestyle='dashed',color='g', label = 'Incliation ranges')
ax2.set_title('Inclination_line')
ax2.set_ylabel('Precentage error (%)', fontsize=12)
ax2.set_xlabel('Inclination (Degrees)', fontsize=12)
ax2.axis([-10, 90, 0, 9])
# plot histograms

ax3 = fig.add_subplot(323)
ax3.hist(chi_p_INC_0,50, facecolor='g', normed=True)
ax3.axvline(x=INC_0_upper_90,linewidth=2,linestyle='dashed',color='k')
ax3.axvline(x=INC_0_lower_90,linewidth=2,linestyle='dashed',color='k')
ax3.axvline(x=injected_value,linewidth=2, color='r')
ax3.set_title('chi_p at Inc 0.0 deg')
ax3.set_ylabel('probability density', fontsize=12)
ax3.set_xlabel('chi_p', fontsize=12)


ax4 = fig.add_subplot(324)
ax4.hist(chi_p_INC_10,50, facecolor='g', normed=True)
ax4.axvline(x=INC_10_upper_90,linewidth=2,linestyle='dashed',color='k')
ax4.axvline(x=INC_10_lower_90,linewidth=2,linestyle='dashed',color='k')
ax4.axvline(x=injected_value,linewidth=2, color='r')
ax4.set_title('Chi_p at Inc 50.0 deg')
ax4.set_ylabel('probability density', fontsize=12)
ax4.set_xlabel('chi_p', fontsize=12)

ax5 = fig.add_subplot(325)
ax5.hist(chi_p_INC_20,50, facecolor='g', normed=True)
ax5.axvline(x=INC_20_upper_90,linewidth=2,linestyle='dashed',color='k')
ax5.axvline(x=INC_20_lower_90,linewidth=2,linestyle='dashed',color='k')
ax5.axvline(x=m_c,linewidth=2, color='r')
ax5.set_title('Mc at Inc 0.0 deg')
ax5.set_ylabel('probability density', fontsize=12)
ax5.set_xlabel('Mc', fontsize=12)

ax6 = fig.add_subplot(326)
ax6.hist(chi_p_INC_30,50, facecolor='g', normed=True)
ax6.axvline(x=INC_30_upper_90,linewidth=2,linestyle='dashed',color='k')
ax6.axvline(x=INC_30_lower_90,linewidth=2,linestyle='dashed',color='k')
ax6.axvline(x=m_c,linewidth=2, color='r')
ax6.set_title('Mc at Inc 50.0 deg')
ax6.set_ylabel('probability density', fontsize=12)
ax6.set_xlabel('Mc', fontsize=12)


fig.tight_layout()
fig.set_figheight(15)
fig.set_figwidth(10)


# Set common labels


plt.savefig("Huge_plot10.png")
