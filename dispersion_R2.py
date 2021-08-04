from scipy.optimize import minimize  
import numpy as np
import matplotlib
import ice_elastic
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
from multiprocessing import Pool,Process, Pipe   
from joblib import Parallel, delayed  


def velocity(omega, KKs, muus, rho1, H1, porosity, Sr, n1):  
    z2 = np.zeros(len(omega)) 
    def final(ii):
        v = 0 
        i = omega[ii] 
        def fun(k):
            def phaseP(term1, term2, term3, term4):
                coef = [term1, -term2, term3, -term4]
                root = 1/np.real(np.sqrt(np.roots(coef))) 
                return  np.abs(root[1])
            def phaseS(term1, term2, term3):
                coef = [term1, -term2, term3]
                root = 1/np.real(np.sqrt(np.roots(coef))) 
                return np.abs(root[0]) 
            KKi = [3.53*10**9]*n1; Kww = [2.25*10**9]*n1
            muui = [1.80*10**9]*n1
            phiw1 = [porosity*Sr] ; phii1 = [porosity - porosity*Sr] 
            kappas = 1*10**(-13)*phiw1[0]**3/(1-(phiw1[0]+phii1[0]))**3 
            kappai = 5*10**(-5)*((phiw1[0]+phii1[0])/phii1[0])**2 *(phiw1[0]/((1-(phiw1[0]+phii1[0]))))**3    
            b013 = 0  
            matrix = ice_elastic.f(i, k, KKs, KKi, muus, muui, rho1, H1, phiw1, phii1, b013,  
                            kappas, kappai, Kww, n1, phaseP, phaseS) 
            matrix1 = np.array(matrix) 
            matrix2 = (np.real(matrix1)) 
            matrix2 = matrix2/np.max(np.abs(matrix2))
            sign, logdet = np.linalg.slogdet(matrix2)
            return sign* np.exp(logdet)

        phase_min = 50; phase_max = 1000; space =1000
        phase = np.linspace(phase_min,phase_max,space)  

        if ii == 0: 
            for j in range(space-1):
                a = fun(i/phase[j])  
                b = fun(i/phase[j+1])  
                if (a*b)<= 0  and j !=0:  
                    root1 =  optimize.root(fun,i/phase[j]) 
                    v = i/root1.x
                    break

        if ii != 0:
            for j in range(space-1):
                a = fun(i/phase[j])  
                b = fun(i/phase[j+1])  
                if (a*b)<= 0  and j !=0:  
                    root1 =  optimize.root(fun,i/phase[j]) 
                    v = i/root1.x
                    break
           
        return  v   # Return one value at a angular frequency
   
    z2 = Parallel(n_jobs=-1)(delayed(final)(i) for i in range(len(omega))) 
    z2 = np.array([z2], dtype=np.float64) 
    return z2.flatten()
 
