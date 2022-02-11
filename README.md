# Solving the Ising model on a 2D lattice using the Metropolis Algorithm

## Introduction
The Ising model is a simplified model of ferromagnetism, the phenomenon whereby certain materials have a finite magnetisation even in the absence of an external magnetic field. The model treats a ferromagnetic material as consisting of atoms or molecules, arranged in a discrete lattice, with magnetic dipole moments (or ‘spins’) that can point either parallel (‘up’) or anti-parallel (‘down’) to some preferred axis. 

The model predicts the key experimental observation that, below a certain temperature (called the ‘critical temperature), the spins align and therefore the material becomes magnetic (whereas above this critical temperature, the spins are randomly oriented).

This code solves the Ising model for a 2D square lattice using the Metropolis algorithm, in the case of no applied external field. 

<<<<<<< HEAD
##Implementation
The entire program is implemented by the *IsingSystem* class. An object of this class is initialised with attributes that are parameters of the physical system (the size, temperature, exchange energy, and external field). The class contains functions to generate a random lattice (*generate_lattice*), and calculate the total energy (*energy*) and magnetisation (*magnetisation*) of a particular lattice configuration, all of which are also run in the initialisation function. Finally, the class contains a function that runs the Metropolis algorithm and returns a list of lattice configurations (along with the corresponding energy and magnetisation) for each sweep, as well as the mean and mean square energy and magnetisation (which would be the measured macro state values) over all the sweeps (*metropolis*). 
=======
## Implementation
To implement the Metropolis algorithm, I created a class (*IsingSystem*), which can be found in *ising.py*. 
>>>>>>> 2ce63a83b7b4f51139ab0395af716fa17caa9e88

##Files
*Ising.py* contains the *IsingSystem* class described above. It also contains a function to find the autocorrelation of the energy/magnetisation, *autocorrelation*, and decorrelation time, *decorr_time*.

In *EqulibrationN.py*, I run the Metropolis algorithm for a range of lattice sizes (at a fixed temperature that is much less than the critical temperature) and plot the magnetisation and energy of the system after each sweep, in order to check whether the system equilibrates. In *EqulibrationT.py*, I do the same but this time for a range of temperatures (at a fixed lattice size).

In *MacroVariables.py*, I find the average (macrostate) energy, magnetisation, magnetic susceptibility and heat capacity over 50,000 sweeps of the Metropolis algorithm, as a function of temperature. 

##How to use
To run the Metropolis algorithm for a particular system, use the following code:

```
from ising import IsingSystem

system = IsingSystem(size = ,
                    temperature = ,
                    exchange_energy = ,
                    external_field = )
                    
system.metropolis(num_steps = )


```

After running this code, the energy and magnetisation can be found in the variables ``` system.av_E ``` and ``` system.av_M``` respectively, and the mean square fluctuations can be found in ``` system.av_E_2 ``` and ```system.av_M_2```. 
