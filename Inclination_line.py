import matplotlib.pyplot as plt
a = [24.84, 6.10, 3.92, 2.74,3.48]
b = [0.0, 57.68, 9.78, 3.34, 5.26]
c = [30.12, 77.34, 0.5, 0.0, 2.36]
I = [90.0, 60.0, 45.0, 30.0, 22.5]
ae = [48.30, 36.24, 23.48, 28.46, 67.66]
be = [0.0, 7.78, 15.9, 23.36, 18.88]
ce = [47.74, 15.38, 28.48, 0.0, 22.86]
#plt.errorbar(x=I, y=a, yerr=0, fmt='o', color='g')
#plt.errorbar(x=I, y=b, yerr=0, fmt='>', color='b')
#plt.errorbar(x=I, y=c, yerr=0, fmt='x', color='r')
plt.plot(I, a, linewidth=2,linestyle='dashed',color='g', label = 'M70_q6_spin1x=0.5')
plt.plot(I, b, linewidth=2,linestyle='dashed',color='b', label = 'M80_q7_spin1x=0.5')
plt.plot(I, c, linewidth=2,linestyle='dashed',color='r', label = 'M90_q8_spin1x=0.5')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Percentage error')
plt.axis([20, 100, 0, 80])
plt.legend(loc='upper left', fontsize=10.5)
plt.savefig("Inc_line2.png")
