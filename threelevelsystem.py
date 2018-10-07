# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:23:54 2018
Three Level System
@author: Gaston
"""
import numpy as np
import matplotlib.pyplot as plt

#Erzeuge Matrix zum Lösen der DGL
def matrixEq(E1,E2,E3):
    E=np.array([E1,E2,E3])
    w=np.zeros((3,3))
    for i in range(0,3):
        for j in range(0,3):
            w[i][j]=abs(E[j]-E[i])   
    omega=np.array([[-w[0][1],0,w[0][2]],[w[0][1],-w[1][2],0],[0,w[1][2],-w[0][2]]])
    return omega

def Euleralg(nrSteps,omega,N0,x0,xk):
    #Zeitschritte
    delta=(xk-x0)/(nrSteps)
    x=np.linspace(x0,xk,nrSteps)
    #erzeuge eintrage von y
    N=np.zeros((3,nrSteps))
     #fixiere Anfangswert
    for i in range(0,3):
        N[i][0]=N0[i]
    for i in range(1,nrSteps):
        N[:,i]=N[:,i-1]+delta*np.dot(omega,N[:,i-1])
    return N,x


omega1=matrixEq(1,3,2)



N,x=Euleralg(100,omega1,[10,10,10],0,10)


fig = plt.figure(dpi=96)
ax = fig.add_subplot(111)
ax.set_xlabel(r'Zeit $t$')
ax.set_ylabel(r'$y$')
ax.plot(x,N[0,:],'b-', label='state1')
ax.plot(x,N[1,:],'g-', label='state2')
ax.plot(x,N[2,:],'y-', label='state3')
ax.legend(loc='upper right')
plt.show()
