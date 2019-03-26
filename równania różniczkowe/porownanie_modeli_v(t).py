import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x_ = np.linspace(0,10,100)                              # zbiór x potrzebnych do narysowania krzywych
x = [1.85,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69]  # czasy Bolta w momentach, gdy przebiegł 10m, 20m, ..., 100m
a = [19.4,35.3,39.6,41.4,42.4,43.9,43.9,43.9,43.4,40]   # szybkość Bolta w wybranych odcinkach w km/h
y = [i*0.27777778 for i in a]                           # szybkość Bolta w m/s


def func(x,a,b):     
    return a*b*(1-np.exp(-x/b))                         # wzór z modelu Kellera

def func1(x,a,b,c):
    return a*b+b**2*c-c*x*b-(a*b+b**2*c)*np.exp(-x/b)   # wzór z modelu Tibshiraniego

# dopasowanie krzywych
popt,pcov = curve_fit(func,x,y)
pop1, pop2 = curve_fit(func1,x,y)

#rysowanie krzywych 
plt.plot(x,y,'ro',label='Międzyczasy Bolta')
plt.plot(x_,func(np.array(x_),*popt),label='Krzywa Kellera')
plt.plot(x_,func1(np.array(x_),*pop1),label='Krzywa Tibshiraniego')

# ustawienia wykresu
plt.autoscale(enable=True, axis='both', tight=None)
plt.xlabel('Czas [s]')
plt.ylabel('Szybkość [m/s]')
plt.title('Porównanie modelu Kellera i Tibshiraniego')
plt.legend()

# zapis wykresu do pliku pdf
plt.savefig('Tibshirani-keller-szybkosci.pdf')