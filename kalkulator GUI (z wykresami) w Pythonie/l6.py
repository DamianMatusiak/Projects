import tkinter as tk
import matplotlib as plt
from numpy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def quit():
    global root
    root.destroy()
    
def clear():
    wz.set('')
    tyt.set('')
    osx.set('')
    osy.set('')
    xod.set('')
    xdo.set('')
    yod.set('')
    ydo.set('')
    
def Calc():
    global legend,wz,tyt,osx,osy,xod,xdo,yod,ydo
    zakresxod,zakresxdo = xod.get(),xdo.get()
    zakresyod,zakresydo = yod.get(),ydo.get()
    if zakresxod == '':
        zakresxod = -5
    if zakresxdo == '':
        zakresxdo = 5
    if zakresyod == '':
        zakresyod = -5
    if zakresydo == '':
        zakresydo = 5
    fig = Figure(figsize=(5,5), dpi=100)
    l = fig.add_subplot(111)
    l.set_title(tyt.get())
    l.set_xlabel(osx.get())
    l.set_ylabel(osy.get())
    l.axis([float(zakresxod),float(zakresxdo),float(zakresyod),float(zakresydo)])
    x = arange(float(zakresxod),float(zakresxdo),(float(zakresxdo)-float(zakresxod))/100)
    ylist = wz.get().split(';')
    for wzor in ylist:
        try:
            wzor.index('x')
            y=eval(wzor)
        except:        
            y=[eval(wzor)]*len(x)
        l.plot(x,y,label=wzor)
    l.grid()
    if legend.get():
        l.legend(loc='best')
   
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.show()
    canvas.get_tk_widget().grid(row=0,column=0,columnspan=100)
    #wykres(tytul=tyt.get(),osX=osx.get(),osY=osy.get(),zakresxod=xod.get(),zakresxdo=xdo.get(),zakresyod=yod.get(),zakresydo=ydo.get())
    #
    #print(a)
    
def write(text):
    wz.set(wz.get()[0:a.index(tk.INSERT)]+text+wz.get()[a.index(tk.INSERT):])  
    #print(kwota0.index(tk.INSERT))
    #end = len(k0.get())
    #kwota0.icursor(end-1)

root = tk.Tk()
root.title("Calculating program")

tk.Label(root, text = 'Wzór: f(x)=').grid(row=2,column = 0)
wz = tk.StringVar()
a=tk.Entry(root,textvariable=wz)
a.grid(row = 2,column = 1)

tk.Label(root, text = 'Tytuł wykresu: ').grid(row=3,column = 0)
tyt = tk.StringVar()
b=tk.Entry(root,textvariable=tyt)
b.grid(row = 3,column = 1)
tk.Label(root, text = 'Nazwa osi X: ').grid(row=4,column = 0)
osx = tk.StringVar()
g=tk.Entry(root,textvariable=osx)
g.grid(row = 4,column = 1)
tk.Label(root, text = 'Nazwa osi Y: ').grid(row=5,column = 0)
osy = tk.StringVar()
h=tk.Entry(root,textvariable=osy)
h.grid(row = 5,column = 1)
tk.Label(root, text = 'Zakres X od: ').grid(row=6,column = 0)
xod = tk.StringVar()
c=tk.Entry(root,textvariable=xod)
c.grid(row = 6,column = 1)
tk.Label(root, text = 'do: ').grid(row=6,column = 2)
xdo = tk.StringVar()
d=tk.Entry(root,textvariable=xdo)
d.grid(row = 6,column = 3,columnspan=4)
tk.Label(root, text = 'Zakres Y od: ').grid(row=7,column = 0)
yod = tk.StringVar()
e=tk.Entry(root,textvariable=yod)
e.grid(row = 7,column = 1)
tk.Label(root, text = 'do: ').grid(row=7,column = 2)
ydo = tk.StringVar()
f=tk.Entry(root,textvariable=ydo)
f.grid(row = 7,column = 3,columnspan=4)
legend = tk.IntVar()
tk.Checkbutton(root, text="Legenda", variable=legend).grid(row=9,column=0)



buttons = []
variables = {1: 'sin()',2:'cos()',3:'tan()',4:'arcsin()',5:'arccos()',6:'arctan()',7:'^2',8:'pi',9:'exp()',10:'()',11:'-',12:'+',13:'*',14:'/',15:'sqrt()'}
button1 = tk.Button(root,text='DRAW',command = Calc).grid(row=12,column=3,sticky=tk.N+tk.S+tk.E+tk.W)
button2 = tk.Button(root,text='EXIT',fg='red',command=quit).grid(row = 12, column = 20,sticky=tk.N+tk.S+tk.E+tk.W)
button3 = tk.Button(root,text='Clear all',command=clear).grid(row=12,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
for i in range(1,len(variables)+1):
    if 2+(i-1)//5 == 3:
        col = i-3
    elif 2+(i-1)//5 == 4:
        col = i-8
    elif 2+(i-1)//5 == 2:
        col=i+2
    buttons.append(tk.Button(root,text=variables[i],command=lambda col=variables[i]: write(col)))
    buttons[-1].grid(row=2+(i-1)//5,column=col,sticky=tk.N+tk.S+tk.E+tk.W)
    

fig = Figure(figsize=(5,5), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
canvas.show()
canvas.get_tk_widget().grid(row=0,column=0,columnspan=100)


root.mainloop()