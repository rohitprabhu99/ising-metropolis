#%%
import numpy as np
import matplotlib.pyplot as plt

from ising import IsingSystem

#%%

"""
Measuring how average magnetisation and energy varies with temperature in 
a 10x10 lattice
"""

#Lattice sizes
N = 10

#Array of temperatures
T_array = np.array(np.linspace(0.1, 3, 30))

#Number of sweeps of Metropolis algorithm
num_steps = 50000


#Arrays containing thermodynamic variables for each temperature 
E = np.zeros(T_array.size)
M = np.zeros(T_array.size)

E_2 = np.zeros(T_array.size)
M_2 = np.zeros(T_array.size)

C = np.zeros(T_array.size)
chi = np.zeros(T_array.size)




#Finding average magnetisation and energy for each temperature and lattice size 

    
for j in range(T_array.size):
    
    #Creating the system
    system = IsingSystem(size = N,
                      temperature = T_array[j],
                      exchange_energy = 1,
                      external_field = 0)
    
    #Running Metropolis
    system.metropolis(num_steps)
    
    E[j] = system.av_E
    E_2[j]  = system.av_E_2

    M[j] = system.av_M
    M_2[j] = system.av_M_2
        
        
    C[j] = E_2[j] - np.square(E[j])
    chi[j] = M_2[j] - np.square(M[j])
    




np.save('MacroVariables_E', E)
np.save('MacroVariables_M', M)
np.save('MacroVariables_C', C)
np.save('MacroVariables_chi', chi)



#%%
"""
Plotting average magnetisation and energy against temperature
"""

E = np.load('MacroVariables_E.npy')
M = np.load('MacroVariables_M.npy')
C = np.load('MacroVariables_C.npy')
chi = np.load('MacroVariables_chi.npy')

fig1, ax = plt.subplots()

ax.plot(T_array, M, 'o', color = 'darkorange')
ax.set_xlabel("Temperature/$(J/k_B)$")
ax.set_ylabel ("Magnetisation/$\mu$")

fig1.tight_layout()

plt.savefig('Magnetisation(T).pdf')


fig2, ax = plt.subplots()

ax.plot(T_array, E, 'o', color = 'darkorange')
ax.set_xlabel("Temperature/$(J/k_B)$")
ax.set_ylabel ("Energy/J")

fig2.tight_layout()

plt.savefig('Energy(T).pdf')


#%%
"""
Plotting heat capacity and magnetisation against temperature
"""

fig3, ax = plt.subplots()

ax.plot(T_array, C, 'o',  color = 'darkorange')
ax.set_xlabel("Temperature/$(J/k_B)$")
ax.set_ylabel ("Heat capacity")

fig3.tight_layout()

plt.savefig('C(T).pdf')


fig4, ax = plt.subplots()

ax.plot(T_array, chi, 'o',  color = 'darkorange')
ax.set_xlabel("Temperature/$(J/k_B)$")
ax.set_ylabel ("Magnetic Susceptibility")

fig4.tight_layout()

plt.savefig('Chi(T).pdf')

