import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,21)
y = 2 * x + 5
plt.title("Line plot")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()

