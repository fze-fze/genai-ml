import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 2*x + 1

xs = np.arange(-5, 5, 0.125)
ys = f(xs)
plt.plot(xs, ys)
plt.show()
