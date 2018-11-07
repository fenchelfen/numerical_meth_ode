from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from matplotlib import style
from numpy import arange
from math import cos, sin, exp
import tkinter as tk

import heun, euler, rk

style.use('seaborn-whitegrid')

class Plotter(FigureCanvasTkAgg):

    const: int

    def __init__(self, master):

        figure = Figure(dpi=100)
        super().__init__(figure, master=master)
        self.axes = figure.add_subplot(111, xlabel='x', ylabel='y')
        # self.get_tk_widget().grid(column=0, row=0, sticky='nsew')
        self.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_canvas(self, x0, y0, h, X, n0, N, flag):

        self.x0 = x0
        self.y0 = y0
        self.h  = h
        self.X  = X
        self.N  = N
        self.n0 = n0

        self.axes.clear()
        self.update_const()
        
        plots = {
            0: self.plot_approx,
            1: self.plot_local,
            2: self.plot_total
        }

        plots.get(flag, 'No such plot')()

        self.axes.legend(fancybox=False)
        self.draw_idle()
    
    def compute_approx_data(self, h=None):
        
        h = self.h if h is None else h

        data_euler = euler.euler_compute(self.x0, self.y0, h, lambda x, y: 3*x*exp(x) - y*(1 - 1/x), self.X)
        data_heun  =   heun.heun_compute(self.x0, self.y0, h, lambda x, y: 3*x*exp(x) - y*(1 - 1/x), self.X)
        data_rk    =       rk.rk_compute(self.x0, self.y0, h, lambda x, y: 3*x*exp(x) - y*(1 - 1/x), self.X)

        return data_euler, data_heun, data_rk

    def compute_exact(self, x):
        
        return 3*x*exp(x)/2 + self.C*x*exp(-x)
    
    def update_const(self):

        self.C = self.y0/(self.x0*exp(self.x0)) - 3/2
    
    def compute_local(self, data, h=None):

        h = self.h if h is None else h

        # compute exact x, y
        x_exact = arange(self.x0, self.X+0.01, h)
        y_exact = [self.compute_exact(x) for x in x_exact]

        # compute local error
        x_list  = [pair[0] for pair in data]
        y_list  = [abs(pair[1]-self.compute_exact(pair[0])) for pair in data]

        return x_list, y_list

    def plot_local(self):

        data_euler, data_heun, data_rk = self.compute_approx_data()

        # local errors
        euler = self.compute_local(data_euler)
        heun  = self.compute_local(data_heun)
        rk    = self.compute_local(data_rk)

        self.axes.plot(euler[0], euler[1], color='y', marker=',', label='Euler local', visible=True, linewidth=1.5)
        self.axes.plot(heun[0], heun[1], color='r', marker=',', label='Heun local', visible=True, linewidth=1.5)
        self.axes.plot(rk[0], rk[1], color='m', marker=',', label='Runge-Kutta local', visible=True, linewidth=1.5)

    def plot_total(self):

        # total errors
        y_euler = []
        y_heun  = []
        y_rk    = []
        x_list = list(range(self.n0, self.N+1))
        for i in x_list:
            step = abs(self.X - self.x0) / i
            data_euler, data_heun, data_rk = self.compute_approx_data(step)
            print(max(self.compute_local(data_euler, step)[1]))
            y_euler.append(max(self.compute_local(data_euler, step)[1]))
            y_heun.append(max(self.compute_local(data_heun, step)[1]))
            y_rk.append(max(self.compute_local(data_rk, step)[1]))

        self.axes.plot(x_list, y_euler, 'y--', marker='.', label='Euler total', visible=True, linewidth=1)
        self.axes.plot(x_list, y_heun, 'r--', marker='.', label='Heun total', visible=True, linewidth=1)
        self.axes.plot(x_list, y_rk, 'm--', marker='.', label='Runge-Kutta total', visible=True, linewidth=1)

    def plot_approx(self):

        print('x, y, h, X, N, n0 = ', self.x0, self.y0, self.h, self.X, self.N, self.n0)

        # comput exact x, y
        x_exact = arange(self.x0, self.X+0.01, self.h)
        y_exact = [self.compute_exact(x) for x in x_exact]
        self.axes.plot(x_exact, y_exact, color='c', label='Exact', visible=True, marker='.')

        data_euler, data_heun, data_rk = self.compute_approx_data()
 
        # euler approx
        x_list = [pair[0] for pair in data_euler]
        y_list = [pair[1] for pair in data_euler]
        self.axes.plot(x_list, y_list, color='y', label='Euler', visible=True, linewidth=1)

        # heun approx
        x_list = [pair[0] for pair in data_heun]
        y_list = [pair[1] for pair in data_heun]
        self.axes.plot(x_list, y_list, color='r', label='Heun', visible=True, linewidth=1)

        # runge-kutta approx
        x_list = [pair[0] for pair in data_rk]
        y_list = [pair[1] for pair in data_rk]
        self.axes.plot(x_list, y_list, color='m', label='Runge-Kutta', visible=True, linewidth=1)
