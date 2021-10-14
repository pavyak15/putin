import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-100, 100.01, 0.5)
plt.plot(x, np.log((x**2 + 1) * np.exp(-abs(x) / 10)) / np.log(1 + np.tan(1/1 + (np.sin(x))*2)))
plt.show()
