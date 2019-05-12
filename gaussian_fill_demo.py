import numpy as np
from matplotlib import pyplot as plt
from gaussian_fill import do_gaussian_fill

def eg_fnc(x):
    return np.sin((x / 1.5 -3.0)**2)+1


xdata = np.linspace(0, 10, 100)
ydata = eg_fnc(xdata)

#unc = 1
unc = np.sqrt(ydata)

fig, ax = plt.subplots()

ax.plot(xdata, ydata, marker='None', ls='-', color='C0')

do_gaussian_fill(xdata, ydata, ax, unc, 4, 1000)

fig.savefig('demo.png')

fig2, ax2 = plt.subplots()

ax2.plot(xdata, ydata, marker='None', ls='-', color='C0')
ax2.plot(xdata, ydata+unc, marker='None', ls='--', color='C0', alpha=0.6)
ax2.plot(xdata, ydata-unc, marker='None', ls='--', color='C0', alpha=0.6)
ax2.plot(xdata, ydata+(2*unc), marker='None', ls='--', color='C0', alpha=0.3)
ax2.plot(xdata, ydata-(2*unc), marker='None', ls='--', color='C0', alpha=0.3)
ax2.plot(xdata, ydata+(3*unc), marker='None', ls='--', color='C0', alpha=0.1)
ax2.plot(xdata, ydata-(3*unc), marker='None', ls='--', color='C0', alpha=0.1)


do_gaussian_fill(xdata, ydata, ax2, unc, 4, 1000)

fig2.savefig('demo_2.png')
