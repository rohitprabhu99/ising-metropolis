import numpy as np

class IsingSystem:
    
    def __init__(self, size, temperature, exchange_energy, external_field):
        self.N = size
        self.T = temperature
        self.J = exchange_energy
        self.h = external_field
        
        self.lattice = self.generate_lattice()
        
        self.energy()
        self.magnetisation()
        
        
        
    
    def generate_lattice(self):
    
        """
        Generating a 2D lattice with a random spin configuration
        
        Parameters
        ------------
        N:
        size of lattice
        
        Outputs
        ------------
        lattice:
        NxN array with each entry in the array being +1 or -1, representing
        the direction of the spin of the particle on that lattice site
        
        """
        lattice = np.random.choice([-1, 1], (self.N, self.N))
    
        return lattice



    def site_energy(self, site):
        
        """
        Finding the contribution to the total energy from a single lattice site
        
        Parameters
        ------------
        site:
        array indices of lattice site (1x2 array)
        
        
        Outputs
        ------------
        energy:
        energy associated with input lattice site
        
        """
        
        #Extracting x and y indices
        x = site[0]
        y = site[1]
        
        
        
        #Interaction term  (using % operator to apply periodic bc)
        interaction_energy = -1 * self.J * self.lattice[x, y] *(
            self.lattice[(x + 1)% self.N, y] + 
            self.lattice[x, (y + 1) % self.N] + 
            self.lattice[(x -  1)% self.N, y] + 
            self.lattice[x, (y - 1)% self.N]
            )
        
        #External energy term
        external_energy = -self.h * self.lattice[x, y]
        
        
        
        #Total energy
        energy = interaction_energy + external_energy
        
        return energy
    
    

    def energy(self):
        """
        Finding the energy (per lattice site) associated 
        with the lattice in a specific microstate
        
        """    
        E = 0
        for i in range(self.N):
            for j in range(self.N):
                E += self.site_energy([i,j])
            
        
        
        E *= 1./(self.N **2) #Energy per lattice site
       
        self.E = E
    
    def magnetisation(self):
        """
        Finding the overall magnetisation (per lattice site) associated
        with the lattice in a specific microstate
        
        """
        
        M = (np.sum(self.lattice))/(self.N**2) #Overall magnetisation per lattice site
        
        self.M = np.abs(M) #Using the absolute value
 
    


    def metropolis(self, num_steps):
        
        """
        Implementing the Metropolis algorithm, finding the energy and
        magnetisation of the system after each sweep and finding the average (i.e. macrostate)
        energy and magnetisation over all sweeps
        
        Parameters
        ------------
        
        num_steps:
        number of sweeps of Metropolis algorithm to carry out
        
        
        Outputs
        -------------
        
        energy:
        Array containing energy associated with lattice configuration after each
        Metropolis sweep
        (dimensions: (num_steps + 1) x 1)
        
        magnetisation:
        Array containing magnetisation associated with lattice configuration after
        each Metropolis sweep
        (dimensions: (num_steps + 1) x 1)
        
        """
        

        #Creating output variables (which will list values of lattice, energy and magnetisation for each Metropolis sweep)
        
        #Array containing lattice configuration after each Metropolis sweep
        #(dimensions: (num_steps + 1) x N x N)
        self.lattice_list = np.zeros([num_steps + 1, self.N, self.N])
        self.lattice_list[0] = self.lattice
        
        #Array containing energy associated with lattice configuration after each
        #Metropolis sweep
        #(dimensions: (num_steps + 1) x 1)
        self.energy_list = np.zeros(num_steps + 1)
        self.energy_list[0] = self.E
        
        #Array containing magnetisation associated with lattice configuration after
        #each Metropolis sweep
        #(dimensions: (num_steps + 1) x 1)
        self.magnetisation_list = np.zeros(num_steps + 1)
        self.magnetisation_list [0] = self.M
        

        for j in range(1, num_steps + 1):
            
            #Looping through lattice sites in order
            for ix in range(self.N):
                for iy in range(self.N):
                 
                
                  #Energy difference between flipped and unflipped spin
                  delta_energy = -2 * self.site_energy([ix, iy])
                
                
                  #Flipping spin if deltaE is less than 0
                  if delta_energy < 0:
                    self.lattice[ix,iy] *= -1
                    self.E += delta_energy
                    self.M += 2*self.lattice[ix,iy]
                
                  #Otherwise, flipping spin if exp(-deltaE/(kT)) > p, where p is a uniform random number in the range [0,1]
                  elif np.exp(-(delta_energy)/(self.J * self.T)) > np.random.rand():
                      self.lattice[ix,iy] *= -1
                      self.E += delta_energy
                      self.M += 2*self.lattice[ix,iy]
            
            #Assigning updated lattice to lattice_output variable
            self.lattice_list[j] = self.lattice
            
            #Calculating energy and magnetisation for updated lattice configuration
            
            self.energy_list[j] = self.E
            self.magnetisation_list[j] = self.M
            
        #Finding mean and mean square energy and magnetisation
        self.av_E = np.mean(self.energy_list)
        self.av_M = np.mean(self.magnetisation_list)
        
        self.av_E_2 = np.mean(np.square(self.energy_list))
        self.av_M_2 = np.mean(np.square(self.magnetisation_list))
    







def autocorrelation(x, n0):
    
    """
    Finding the autocorrelation of the energy/magnetisation (after the system
    reaches equilibrium)
    
    Parameters
    ------------
    x:
    array of energy/magnetisation associated with each Metropolis sweep
    (dimensions: (Number of Metropolis sweeps + 1) x 1)
    
    n0:
    sweep number at which variable reaches equilibrium
    
    Outputs
    -----------
    corr:
    array autocorrelation as function of 'time' lag
    (where here 'time' is the number of sweeps of the Metropolis algorithm)

    """
    
    #Deleting the function up until the point it reaches equilibrium
    if n0 != 0:
      x = np.delete(x, range(n0))
    
    
    #Calculating autocorrelation for all time lags
    
    mean=np.mean(x)
    var=np.var(x)
    xp=x-mean
    
    lags = np.array(range(x.size))
    
    corr=[1. if l==0 else np.sum(xp[l:]*xp[:-l])/len(x)/var for l in lags]

    return np.array(corr)    
    


def decorr_time(autocorr):
    
    """
    Finding the decorrelation time of a function, given its autocorrelation
    
    Parameters
    ------------
    autocorr: 
    autocorrelation as a function of 'time' lag
    
    Outputs
    -----------
    result:
    index number ('time' lag) at which autocorrelation falls to 1/e
    """
    
    result = 0
    
    for i in range(len(autocorr)):
    
      if autocorr[i] <= 1/np.e:
        result = i
        break
      
    if result == 0:
      return np.nan
    
    else:
      return result
  
