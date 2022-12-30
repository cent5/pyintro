import matplotlib.pyplot as plt
import numpy as np


# Draw a sine wave
x = np.linspace(0, 7, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
