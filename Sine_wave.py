import matplotlib.pyplot as plt

import numpy as np


Fs = 8000
f = 5
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x/Fs)
z = np.cos(2*np.pi*f*x/Fs)

fig=plt.figure(1)

plt.subplot(211)
plt.plot(x/Fs, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')


plt.subplot(212)
plt.plot(x/Fs, z)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

plt.close()
