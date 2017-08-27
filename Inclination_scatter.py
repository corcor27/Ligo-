import matplotlib.pyplot as plt
a = [24.84, 6.10, 3.92, 2.74,3.48]
b = [0.0, 57.68, 9.78, 3.34, 5.26]
c = [30.12, 77.34, 0.5, 0.0, 2.36]
I = [90.0, 60.0, 45.0, 30.0, 22.5]
ae = [48.30, 36.24, 23.48, 28.46, 67.66]
be = [0.0, 7.78, 15.9, 23.36, 18.88]
ce = [47.74, 15.38, 28.48, 0.0, 22.86]
plt.errorbar(x=I, y=a, yerr=ae, fmt='o', color='g')
plt.errorbar(x=I, y=b, yerr=be, fmt='+', color='b')
plt.errorbar(x=I, y=c, yerr=ce, fmt='x', color='r')
plt.xlabel('Inclination (degrees)')
plt.ylabel('Percentage error')
plt.savefig("Inc_precent_error.png")
