import numpy as np
def estimate(particles, particles_w):
    #particles: numofparticles*particledimension
    #particles_w: numofparticles*1?
    #print('parti',particles)
    #print(particles_w)
    #print("mean",np.mean(particles*particles_w.reshape(-1,1),0)/np.sum(particles_w)   )
    return np.sum(particles*particles_w.reshape(-1,1),0)/np.sum(particles_w)   