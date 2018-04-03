import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('datos.txt')
t = range(1, len(datos[:,0])+1)
plt.figure()
plt.plot(t, datos[:,0], label = 'no repetidas')
plt.plot(t, datos[:,1], label = 'repetidas')
plt.legend()
plt.savefig('mialbum.pdf')
plt.close()
