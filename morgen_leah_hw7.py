import astropy as ast 
from astropy import units as u 
import numpy as np
from matplotlib import pyplot as plt


f = np.loadtxt('sed.txt', delimiter =",", skiprows=3)
print(f)

wl = f[:,0] #wavelength is in the first column
lu = f[:,1] #luminosity is the second column



plt.loglog(wl,lu)
plt.plot(wl, lu)
plt.title("wavelength vs luminosity") 
plt.ylabel("luminosity")
plt.xlabel("wavelength")
plt.show()
plt.savefig("wavelength_vs_luminosity", dpi = 300)

lower_limit = np.where(wl< 10) 
print("10",lower_limit)

wl *= u.micron
lu *= u.Lsun/u.micron

integral = (np.trapz(lu[0:833], x = -wl[0:833])).to(u.erg/u.s)

print("spectral energy distribution integral", integral)

