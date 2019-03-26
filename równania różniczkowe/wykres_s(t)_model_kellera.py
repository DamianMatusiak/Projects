import matplotlib.pyplot as plt
import numpy as np

tau = 0.892;
F = 12.2;
sigma = 9.93;
E0 = 575;
lambd = []
yd = 0.9144
x = [1.85,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69] # czasy
y = [10,20,30,40,50,60,70,80,90,100]                   # odcinki w metrach

from scipy.optimize import curve_fit
    
def func(x,F,tau):
    return F*tau**2*(x/tau+np.exp(-x/tau)-1)

popt,pcov = curve_fit(func,x,y)
x_ = np.linspace(0,10,100)
plt.autoscale(enable=True, axis='both', tight=None)

plt.plot(x,y,'ro',label='pomiary Bolta')
popt,pcov = curve_fit(func,x,y)
plt.plot(x_,func(np.array(x_),*popt),label='krzywa bez rozszerzenia')
plt.legend()
plt.title("Krzywa Kellera (Olimpiada Beijing)")
plt.xlabel('Czas [s]')
plt.ylabel('Dystans [m]')
#plt.savefig('123.pdf')