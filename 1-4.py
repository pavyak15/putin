import numpy as np
import matplotlib.pyplot as plt
with plt.xkcd():
    x = np.arange(-100, 100.01, 0.5)
    plt.plot(x, eval(input()))
    plt.show()
