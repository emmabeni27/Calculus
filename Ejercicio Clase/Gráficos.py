import matplotlib.pyplot as plt
import numpy as np

#plt.plot([5,10,6,-10,15,1]) #paso los puntos pero igual los une. Si le paso un sólo string los considera de y, los valores de x los genera automáticament.
#plt.show()

#plt.plot([10,25,30,60,70,100], [100,200,-100,300,0,-250]) #el primer vector son las x y el segundo vector son las y
#plt.show()

x=np.linspace(0, 30)
y=np.exp(-0.1*x)*np.cos(x)
plt.plot(x,y)
plt.show()

x = np.linspace(0, 30, 1000)
y = np.exp(-0.1*x)*np.cos(x)
plt.plot(x,y)

plt.plot([0,1,2,3,4,5], [5,10,6,-10,15,1], 'r--o', label="Partícula 1")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.title("Una primera aproximación")
plt.text(2,7,"$ P_1 (2,6) $", color="b")
plt.legend()
plt.grid(ls="--", color="#dadada")
plt.show()