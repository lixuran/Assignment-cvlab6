import numpy as np
def propagate(particles, frame_height, frame_width, params):
    model = params["model"]
    sig_pos = params["sigma_position"]
    sig_v = params["sigma_velocity"]
    #print("particles",particles)
    new_particless = np.zeros(particles.shape)
    for i in range(particles.shape[0]):
        if model ==0:
            A= np.array([[1,0],[0,1]])
            b= np.random.normal([0,0],[sig_pos,sig_pos])
        else:
            A = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]])
            b = np.random.normal([0,0,0,0],[sig_pos,sig_pos,sig_v,sig_v])
        
        #print(A.shape)
        #print(b.shape)
        new_particles =A@particles[i].reshape(-1,1)+b.reshape(-1,1)
        #print(new_particles)
        if (new_particles[0]>frame_width):
            new_particles[0] = frame_width
    
        new_particles[0] = min(frame_width-1, new_particles[0])
        new_particles[0] = max(0, new_particles[0])
        new_particles[1] = min(frame_height-1, new_particles[1])
        new_particles[1] = max(0, new_particles[1])
        new_particless[i] = np.squeeze(new_particles)
    return new_particless