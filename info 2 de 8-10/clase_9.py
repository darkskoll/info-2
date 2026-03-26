# clase despues del parcial  19/03/26
import matplotlib.pyplot as plt
import numpy as np

b = np.random.randint(100, size=(10,4))
#print(x.ndim)
#print(x.itemsize)
#print(x.size)
#print(x.shape)
#print(x.dtype)
#print(x.nbytes)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

print(x.size)
print(x.itemsize)
print(x.ndim)
print(x.shape)
print(x.dtype)
print(x.nbytes)

print(np.sin(90))
print(np.sin(np.radians(90)))
print(np.cos(np.radians(90)))

# traza la función seno
plt.plot(x, y)
plt.title("y = sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()



#x = np.linspace(0,360,360,False)
#y = np.sin(np.radians(x))
#plt.plot(x,y)
#plt.show()