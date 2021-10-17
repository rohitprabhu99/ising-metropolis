import numpy as np
import matplotlib.pyplot as plt

from ising import IsingSystem
from ising import generate_lattice
from ising import metropolis



"""
Investigating how the number of sweeps required to reach equilibrium varies 
with temperature

Using a 10x10 lattice throughout
"""
#Lattice size
N = 25

#Creating array of temperatures to investigate
T_array = np.array([0.1, 0.5, 1, 2, 2.2, 2.4, 2.6, 3])

#Number of sweeps of Metropolis algorithm
num_steps = 5000

#Arrays containing magnetisation and energy for each sampled microstate 
E_T = np.zeros((T_array.size, (num_steps + 1)))
M_T = np.zeros((T_array.size, (num_steps + 1)))

#Looping over lattice sizes
for j in range(T_array.size):
    #Creating system
    system = IsingSystem(size = N, 
                          temperature = T_array[j], 
                          exchange_energy = 1,
                          external_field = 0)
    
    #Running Metropolis
    system.metropolis(num_steps)
    E_N[j, :] = system.energy_list
    M_N[j, :] = system.magnetisation_list
#%%
"""
Plotting microstate magnetisation as function of number of sweeps
"""

fig1, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4,2, figsize = (30, 8))

ax1.plot(M_T[0], color = 'darkred')
ax1.set_xlabel("Number of sweeps")
ax1.set_ylabel ("Magnetisation/$\mu$")
ax1.set_title("T=0.1/$(J/k_B)$")

ax2.plot(M_T[1], color = 'darkred')
ax2.set_xlabel("Number of sweeps")
ax2.set_ylabel ("Magnetisation/$\mu$")
ax2.set_title("T=0.5/$(J/k_B)$")

ax3.plot(M_T[2], color = 'darkred')
ax3.set_xlabel("Number of sweeps")
ax3.set_ylabel ("Magnetisation/$\mu$")
ax3.set_title("T=1.0/$(J/k_B)$")

ax4.plot(M_T[3], color = 'darkred')
ax4.set_xlabel("Number of sweeps")
ax4.set_ylabel ("Magnetisation/$\mu$")
ax4.set_title("T=2.0/$(J/k_B)$")

ax5.plot(M_T[4], color = 'darkred')
ax5.set_xlabel("Number of sweeps")
ax5.set_ylabel ("Magnetisation/$\mu$")
ax5.set_title("T=2.2/$(J/k_B)$")

ax6.plot(M_T[5], color = 'darkred')
ax6.set_xlabel("Number of sweeps")
ax6.set_ylabel ("Magnetisation/$\mu$")
ax6.set_title("T=2.4/$(J/k_B)$")

ax7.plot(M_T[6], color = 'darkred')
ax7.set_xlabel("Number of sweeps")
ax7.set_ylabel ("Magnetisation/$\mu$")
ax7.set_title("T=2.6/$(J/k_B)$")

ax8.plot(M_T[7], color = 'darkred')
ax8.set_xlabel("Number of sweeps")
ax8.set_ylabel ("Magnetisation/$\mu$")
ax8.set_title("T=3.0/$(J/k_B)$")

fig1.tight_layout()

plt.savefig('Equilibration_M(T)_10x10.pdf')


"""
Plotting microstate energy as function of number of sweeps
"""

fig2, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4,2, figsize = (30, 8))

ax1.plot(E_T[0], color = 'navy')
ax1.set_xlabel("Number of sweeps")
ax1.set_ylabel ("Energy/J")
ax1.set_title("T=0.1/$(J/k_B)$")

ax2.plot(E_T[1], color = 'navy')
ax2.set_xlabel("Number of sweeps")
ax2.set_ylabel ("Energy/J")
ax2.set_title("T=0.5/$(J/k_B)$")

ax3.plot(E_T[2], color = 'navy')
ax3.set_xlabel("Number of sweeps")
ax3.set_ylabel ("Energy/J")
ax3.set_title("T=1.0/$(J/k_B)$")

ax4.plot(E_T[3], color = 'navy')
ax4.set_xlabel("Number of sweeps")
ax4.set_ylabel ("Energy/J")
ax4.set_title("T=2.0/$(J/k_B)$")

ax5.plot(E_T[4], color = 'navy')
ax5.set_xlabel("Number of sweeps")
ax5.set_ylabel ("Energy/J")
ax5.set_title("T=2.2/$(J/k_B)$")

ax6.plot(E_T[5], color = 'navy')
ax6.set_xlabel("Number of sweeps")
ax6.set_ylabel ("Energy/J")
ax6.set_title("T=2.4/$(J/k_B)$")

ax7.plot(E_T[6], color = 'navy')
ax7.set_xlabel("Number of sweeps")
ax7.set_ylabel ("Energy/J")
ax7.set_title("T=2.6/$(J/k_B)$")

ax8.plot(E_T[7], color = 'navy')
ax8.set_xlabel("Number of sweeps")
ax8.set_ylabel ("Energy/J")
ax8.set_title("T=3.0/$(J/k_B)$")

fig2.tight_layout()

plt.savefig('Equilibration_E(T)_10x10.pdf')
