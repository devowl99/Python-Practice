import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.axvline(x=0, color = 'r')
plt.axhline(y=0, color = 'r')

def relu(x):
    return np.maximum(0, x)

x = np.arange(-10.0, 10.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.title('ReLU_고려대세종_2019270626_한시현')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True, linestyle = '--')
plt.show()