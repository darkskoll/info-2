# clase de 12-2pm post parcial 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,360,360,False)
y = np.sin(np.radians(x))
plt.plot(x,y)
plt.show()