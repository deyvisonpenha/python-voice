import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

# criando o sinal
dt = 0.001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f_clean = f
f = f + 2.5*np.random.randn(len(t))

plt.plot(t,f,color='c', LineWidth=1.5, label='Noisy')
plt.plot(t,f_clean, color='k', LineWidth=2, label='Clean')
plt.xlim(t[0],t[-1])
plt.legend()
