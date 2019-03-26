import matplotlib.pyplot as plt
import numpy as np

tau = 0.892;
F = 12.2;
sigma = 9.93;
E0 = 575;
lambd = []
yd = 0.9144
x = [1.85,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69]
a = [19.4,35.3,39.6,41.4,42.4,43.9,43.9,43.9,43.4,40]
y = [i*0.27777778 for i in a]

plt.plot(x,y,'r.');


from scipy.optimize import curve_fit
    
def func(x,a,b):
    return a*b*(1-np.exp(-x/b))


popt,pcov = curve_fit(func,x,y)
x_ = np.linspace(0,10,100)
plt.autoscale(enable=True, axis='both', tight=None)
plt.plot(x,y,'ro',label='pomiary')
plt.plot(x_,func(np.array(x_),*popt),label='dopasowane parametry')
print(*popt)
plt.xlabel('Czas [s]')
plt.ylabel('Szybkosc [m/s]')

F = 12.2
tau = 0.892
y = F*tau*(1-np.exp(-x_/tau))
plt.plot(x_,y,label='standardowe parametry')
plt.legend()

plt.savefig('ostatnie 2 krzywe.pdf')
