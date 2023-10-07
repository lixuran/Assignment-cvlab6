from color_histogram import color_histogram
import numpy as np
from chi2_cost import chi2_cost
def observe(particles, frame, bbox_height, bbox_width,hist_bin, hist, sigma_ob):
    particles_w=np.zeros(particles.shape[0])
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    # get hist for each particle
    for i in range(particles.shape[0]):
        x_center = particles[i,0]
        y_center = particles[i,1]
        x_min = round(max( x_center - bbox_width/2,0))
        x_max = round(min( x_center + bbox_width/2,frame_width-1))
        y_min = round(max( y_center - bbox_height/2,0))
        y_max = round(min( y_center + bbox_height/2,frame_height-1))
        cur_hist = color_histogram(x_min, y_min, x_max, y_max,
                    frame, hist_bin)
        # get x2 distance
        x2_dis = chi2_cost(cur_hist,hist)
        #print(x2_dis,"dis")
        #get weight 
        particles_w[i] = 1/(np.sqrt(np.pi*2)*sigma_ob)*np.exp(-x2_dis**2/(2*sigma_ob**2))
        #print("p wegiht",particles_w[i])
    return particles_w