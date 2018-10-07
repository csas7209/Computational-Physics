"""
Erstes Beispiel: Eulermethode zur Loesung einer DGL eines radioaktiven Zerfalls
Autor: Gaston Gruber
"""

import numpy as np
import matplotlib.pyplot as plt

#Loesung einer DGL mit der Euler Methode

#Euleralgorithmus
def Euleralg(dt,gamma,y0,t):
    #Zeitschritte
    deltagamma=dt*gamma
    x=np.linspace(0,t,int(t/dt))
    #erzeuge eintrage von y
    y=np.zeros(int(t/dt))
     #fixiere Anfangswert
    y[0]=y0
    #Euleralgorithmus
    for i in range(1,int(t/dt)):
        y[i]=y[i-1]-dt*(gamma*y[i-1])
    return y,x,gamma,deltagamma
        

#Anfangswerte definieren
dt=0.01
gamma=2
y0=1
tm=10
t=np.arange(0,tm,0.01)
#Euleralgorithmus ausführen
y,x,gamma,deltagamma=Euleralg(dt,gamma,y0,tm)


#analytische Losung

def f(t):
    return y0*np.exp(-2*t)

#Vergleich der beiden Varianten


"""
Darstellung der fuer verschiedene Gamma. Jedoch kein subplot, da umstaendlicher in diesem zusammenhang
"""
fig = plt.figure(dpi=96)
ax = fig.add_subplot(111)
ax.set_xlabel(r'Zeit $t$')
ax.set_ylabel(r'$y(t)$')
ax.plot(x,y,'b-', label='numerical')
ax.plot(t,f(t),'r-', label='analytic')
ax.legend(loc='upper right')
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax.text(0.80, 0.75, '$\gamma \Delta$= %.2f'% deltagamma, transform=ax.transAxes, bbox=props)
#ax.title (r'Losung DGL eines radioaktiven Zerfalls, $\gamma = %.2f$' % deltagamma)
plt.grid(True)
#plt.savefig('dgmitt.pdf')
plt.show()

    
    

    

