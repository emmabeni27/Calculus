import matplotlib.pyplot as plt
import numpy as np
import math
import pylab as pl

t = np.linspace(0, 2*math.pi, 10000)
x = np.cos(t)
y = np.sin(t) #usar plt que es mas compatibla aca q math
plt.plot(x,y)
plt.show()

t = np.linspace(-10, 20, 10000)
z = t**2+1/3*t
plt.plot(t,z)
plt.show()

x = np.linspace(0, 2*math.pi, 10000)
y = 10*np.cos(x)
plt.plot(x,y)
plt.show()

t = np.linspace(0, 2*math.pi, 10000)
x=math.cos(t)
y=math.sen(t)
plt.plot(x,y)
plt.show()