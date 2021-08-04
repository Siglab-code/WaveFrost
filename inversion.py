import numpy as np
import dispersion_R1
import dispersion_R2
import matplotlib.pyplot as plt
from multiprocessing import Pool  
from joblib import Parallel, delayed
import clas  

# load dispersion measurement for R1 and R2 wave
disp1 = np.loadtxt('data/site1_R2.csv')  
disp2 = np.loadtxt('data/site1_R1.csv')  
y_data1 = disp1[:, 1]
y_data2 = disp2[:, 1]
y_data = np.concatenate((y_data1 , y_data2), axis=0) 
omega1 = np.pi*2*disp1[:, 0] 
omega2 = np.pi*2*disp2[:, 0]
loss2 = []
para = []
para_min = []
disp_curve = []  

# define aim function 
def aimfuc(x): 
    global omega1, y_data1, omega2, y_data2, y_data
    para.append(x)
    KKs = np.array([x[11], x[12], x[13]])*10**9
    muus = np.array([x[0], x[1], x[2]])*10** 9
    rho1 = [2600]*3         #np.array([x[8], x[9], x[10], x[11]])
    H = np.array([x[3], x[4], 1]) 
    porosity = np.array([x[5], x[6], x[7]])
    Sr = np.array([x[8], x[9], x[10]]) 
    # calculate theoretical dispersion relation for R2 wave
    yt1 = dispersion_R2.velocity(omega1, KKs, muus, rho1, H, porosity, Sr, len(Sr)) 
    # calculate theoretical dispersion relation for R1 wave
    yt2 = dispersion_R1.velocity(omega2, KKs, muus, rho1, H, porosity, Sr, len(Sr)) 
    # loss11 = np.abs(yt1- y_data1)     # loss function for R2 wave
    loss22 = np.abs(yt2- y_data2)       # loss function for R1 wave
    yt = np.concatenate((yt1, yt2), axis=0)  
    # Monitoring resutls
    plt.clf() 
    disp_curve.append(yt)   
    plotyt = np.array(disp_curve)
    loss = np.sqrt(np.sum(loss22**2))   # define loss function for R1 wave 
    loss2.append(loss)
    loc = np.where(np.array(loss2) == np.array(loss2).min())[0] 
    # store results while searching space
    # np.savetxt('para2.txt', para)
    # np.savetxt('loss2.txt', loss2)
    # np.savetxt('dispersion2.txt', disp_curve)
    plt.clf() 
    plt.plot(omega1 / (2 * np.pi), y_data1, label='measurement')
    plt.plot(omega2 /(2*np.pi), y_data2, label= 'measurement')  
    plt.plot(omega1 / (2 * np.pi), plotyt[loc[0],:len(omega1)], ':', label='Prediction')
    plt.plot(omega2 /(2*np.pi), plotyt[loc[0], len(omega1):], ':', label='Prediction')  
    plt.legend()
    plt.ylim(0, 3000)
    plt.savefig('dispersion_update.png')  
    return np.sqrt(loss)

# Run the optimization (users should run the optimization multiple times with various random 
# initial values to increase the robustness of the inversion results) 
n = 3
Ei = (6, 20) # bulk modulus (GPa)
mui = (4,80) # shear modulus (GPa)
# Hi = (0.5,10) # thickness
# po = (0.1, 0.7) # porosity
# sri = (0.05, 0.95) # degree of saturation of unfrozen water

srch = clas.Searcher(
    objective= aimfuc,
    limits=[mui, mui, mui, (4.1, 4.2), (14.5,15), (0.36, 0.37), (0.46, 0.47), (0.31, 0.32),
           (0.88, 0.89),(0.22, 0.23), (0.97, 0.98), Ei, Ei, Ei],
    num_samp=20,  
    num_resamp=5,
    maximize=False,
    verbose=True
    ) 
a, b = srch.update(50)  
 