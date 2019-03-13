# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.2)
print(x)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
# plt.show()