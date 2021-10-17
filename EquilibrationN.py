import numpy as np
import matplotlib.pyplot as plt

from ising import IsingSystem



#%% Equilibration(N)
"""
Checking that systems of different sizes equilibrate after 50000 sweeps of the 
Metropolis algorithm (for T << T_c)

Using T = 1 throughout
"""
#Creating array of lattice sizes to investigate
N_array = np.array([10, 20, 30, 40])

#Number of sweeps of Metropolis algorithm
num_steps = 50000

#Arrays containing magnetisation and energy for each sampled microstate in each lattice size
E_N = np.zeros((N_array.size, (num_steps + 1)))
M_N = np.zeros((N_array.size, (num_steps + 1)))

#Looping over lattice sizes
for j in range(N_array.size):
    #Creating system
    system = IsingSystem(size = N_array[j], 
                          temperature = 1, 
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

fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (15, 8))

ax1.plot(M_N[0], color = 'darkred')
ax1.set_xlabel("Number of sweeps")
ax1.set_ylabel ("Magnetisation/$\mu$")
ax1.set_title("10x10 lattice")

ax2.plot(M_N[1], color = 'darkred')
ax2.set_xlabel("Number of sweeps")
ax2.set_ylabel ("Magnetisation/$\mu$")
ax2.set_title("20x20 lattice")

ax3.plot(M_N[2], color = 'darkred')
ax3.set_xlabel("Number of sweeps")
ax3.set_ylabel ("Magnetisation/$\mu$")
ax3.set_title("30x30 lattice")

ax4.plot(M_N[3], color = 'darkred')
ax4.set_xlabel("Number of sweeps")
ax4.set_ylabel ("Magnetisation/$\mu$")
ax4.set_title("40x40 lattice")

fig1.tight_layout()

plt.savefig('Equilibration_M(N).pdf')

"""
Plotting microstate magnetisation as function of number of sweeps
"""

fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (15, 8))

ax1.plot(E_N[0], color = 'navy')
ax1.set_xlabel("Number of sweeps")
ax1.set_ylabel ("Energy/J")
ax1.set_title("10x10 lattice")

ax2.plot(E_N[1], color = 'navy')
ax2.set_xlabel("Number of sweeps")
ax2.set_ylabel ("Energy/J")
ax2.set_title("20x20 lattice")

ax3.plot(E_N[2], color = 'navy')
ax3.set_xlabel("Number of sweeps")
ax3.set_ylabel ("Energy/J")
ax3.set_title("30x30 lattice")

ax4.plot(E_N[3], color = 'navy')
ax4.set_xlabel("Number of sweeps")
ax4.set_ylabel ("Energy/J")
ax4.set_title("40x40 lattice")

fig2.tight_layout()

plt.savefig('Equilibration_E(N).pdf')

