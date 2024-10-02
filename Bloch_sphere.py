import numpy as np
import matplotlib.pyplot as plt
from qutip import Bloch
b = Bloch()
theta = np.pi/4  
phi = 0  
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)
b.add_vectors([x, y, z])
b.render()
plt.show()