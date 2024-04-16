import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.axvline(x=0, color = 'r')
plt.axhline(y=0, color = 'r')

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

x = np.arange(-5.0, 5.0, 0.1)
y = elu(x)
plt.plot(x, y, linestyle = '-')
plt.title('ELU 함수')
plt.xlabel('x')
plt.ylabel('ELU(x)')
plt.grid(True, linestyle = '--')
plt.show()