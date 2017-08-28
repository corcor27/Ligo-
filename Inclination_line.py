import matplotlib.pyplot as plt
a = [6.10, 3.92, 2.74,3.48, 24.84]
b = [57.68, 9.78, 3.34, 5.26, 18.22]
c = [77.34, 0.5, 1.94, 2.36, 30.12]
I = [60.0, 45.0, 30.0, 22.5, 0.0]
ae = [36.24, 23.48, 28.46, 67.66, 48.30]
be = [7.78, 15.9, 23.36, 18.88, 51.72]
ce = [15.38, 28.48, 26.7, 22.86, 47.74]
#plt.errorbar(x=I, y=a, yerr=0, fmt='o', color='g')
#plt.errorbar(x=I, y=b, yerr=0, fmt='>', color='b')
#plt.errorbar(x=I, y=c, yerr=0, fmt='x', color='r')
plt.plot(I, a, linewidth=2,linestyle='dashed',color='g', label = 'M70_q6_spin1x=0.5')
plt.plot(I, b, linewidth=2,linestyle='dashed',color='b', label = 'M80_q7_spin1x=0.5')
plt.plot(I, c, linewidth=2,linestyle='dashed',color='r', label = 'M90_q8_spin1x=0.5')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Percentage error')
plt.title("Estimation of chi_p with varying inclination")
plt.axis([-10, 70, 0, 80])
plt.legend(loc='upper left', fontsize=10.5)
plt.savefig("Inc_line7.png")
