# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:27:44 2025

@author: mkranich
"""

import numpy as np
import matplotlib.pyplot as plt
import ltspice as lt

#parse data from .raw file
fpath       = 'tb_clkgen_save.raw'
l           = lt.Ltspice(fpath)
l.parse()

#extract relevant data
time        = l.get_time()
vclk        = l.get_data('v(clkin)')
vp1         = l.get_data('v(p1)')
vp1e        = l.get_data('v(p1e)')
vp2         = l.get_data('v(p2)')
vp2e        = l.get_data('v(p2e)')

#redefine data arrays considering new length
factor = 1/15
length = round(len(time)/factor)


time    = time[1000:1150]
vclk    = vclk[1000:1150]
vp1     = vp1[1000:1150]
vp1e    = vp1e[1000:1150]
vp2     = vp2[1000:1150]
vp2e    = vp2e[1000:1150]

#plot data
#plt.close('all')
plt.figure(6, figsize=(20,10))
plt.plot(time*1e9, vp1, label=r'$\phi_1$')
plt.plot(time*1e9, vp1e, label=r'$\phi_{1d}$')
plt.plot(time*1e9, vp2, label=r'$\phi_2$')
plt.title('Voltage input clock over time')
plt.xlabel('$t$/ns')
plt.ylabel('V')
plt.legend()
plt.grid()