import numpy as np 

def color_histogram(x_min, y_min, x_max, y_max,
                frame, hist_bin):
    
    #print("frame",frame)
    xmin = min(x_min,x_max)
    xmax = max(x_min,x_max)
    ymin = min(y_min,y_max)
    ymax = max(y_min,y_max)
    #print(xmin,xmax,ymin,ymax,"coords")
    #print(frame.shape)
    selected_frame = frame[ymin:ymax,xmin:xmax,:]
    #print(selected_frame)
    a,_ = np.histogram(selected_frame[:,:,0], bins=hist_bin, range=(0,255))
    #print(selected_frame[:,:,0].shape,"selected shape")
    #print(selected_frame[:,:,0])
    b ,_= np.histogram(selected_frame[:,:,1], bins=hist_bin, range=(0,255))
    c ,_= np.histogram(selected_frame[:,:,2], bins=hist_bin, range=(0,255))
    #print(a,"a")
    if(a.sum()==0):
        raise Exception("shit")
    #print(a)
    a= a/a.sum()
    b= b/b.sum()
    c= c/c.sum()
    hist =np.append(a,b)
    hist = np.append(hist,c)
    #print(hist,"hist")
    return hist