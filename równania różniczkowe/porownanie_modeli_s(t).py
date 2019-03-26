import matplotlib.pyplot as plt
import numpy as np

x = [1.85,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69] # czasy Bolta
y = [10,20,30,40,50,60,70,80,90,100]                   # odcinki w metrach

from scipy.optimize import curve_fit
    
def func(x,F,tau):
    return F*tau**2*(x/tau+np.exp(-x/tau)-1)           # wzór na dystans (model Kellera)

def func1(x,F,tau,c):
    return tau*F+c*tau**2-0.5*(c*tau*x)-tau*(tau*F+c*tau**2)*(np.exp(-x/tau)-1) # wzór na dystans z rozszerzeniem Tibshiraniego

x_ = np.linspace(0,10,100)



popt,pcov = curve_fit(func,x,y)             # dopasowanie krzywej Kellera
pop1,pop2 = curve_fit(func1,x,y)            # dopasowanie krzywej - model Tibshiraniego

# rysowanie krzywych wraz z rzeczywistymi pomiarami
plt.plot(x,y,'ro',label='Pomiary Bolta')
plt.plot(x_,func(np.array(x_),*popt),label='Krzywa Kellera')            
plt.plot(x_,func1(np.array(x_),*pop1),label='Krzywa Tibshiraniego')

# ustawienia wykresu
plt.autoscale(enable=True, axis='both', tight=None)
plt.legend()
plt.title("Porównanie modelu Kellera i Tibshiraniego")
plt.xlabel('Czas [s]')
plt.ylabel('Dystans [m]')

# zapis wykresu w pliku pdf
plt.savefig('porownaniedrog.pdf')