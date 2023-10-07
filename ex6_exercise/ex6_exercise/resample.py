import numpy as np
def resample(particles, particles_w):
    n_particles = particles.shape[0]
    total_w = particles_w.sum()
    #print(particles_w.shape)
    #print(particles_w)
    #print(particles_w/total_w)
    if total_w>0:
        index = np.random.choice(n_particles,n_particles,p=particles_w/total_w)
    else:
        index = np.random.choice(n_particles,n_particles)
    return particles[index],particles_w[index] 