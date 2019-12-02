# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:42:43 2019

@author: SHF_W
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 
              20.0, 40.0, 60.0, 80.0])

y = np.array([0.50505332505407008, 1.1207373784533172, 2.1981844719020001,
              3.1746209003398689, 4.2905482471260044, 6.2816226678076958,
              11.073788414382639, 23.248479770546009, 32.120462301367183, 
              44.036117671229206, 54.009003143831116, 102.7077685684846, 
              185.72880217806673, 256.12183145545811, 301.97120103079675])

# Our model is y = a * x, so things are quite simple, in this case...
# x needs to be a column vector instead of a 1D vector for this, however.
x = x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y)
print(np.shape(x))
print(np.shape(y))

plt.plot(x, y, 'bo')
plt.plot(x, a*x, 'r-')
plt.show()