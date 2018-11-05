from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from matplotlib import style
from numpy import arange
from math import cos, sin, exp
import tkinter as tk

import heun, euler

style.use('seaborn-whitegrid')

class Plotter(FigureCanvasTkAgg):

	def __init__(self, master):

		figure = Figure(dpi=100)
		super().__init__(figure, master=master)
		self.axes = figure.add_subplot(111, xlabel='x', ylabel='y')
		# self.get_tk_widget().grid(column=0, row=0, sticky='nsew')
		self.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	def update_canvas(self, x0, y0, h, X, N, flag):

		self.x0 = x0
		self.y0 = y0
		self.h  = h
		self.X  = X
		self.N  = N

		self.axes.clear()
		
		if (flag):
			self.plot_approx()
		else:
			self.plot_errors()

		self.axes.legend(fancybox=False)
		self.draw_idle()
	
	def compute_approx_data(self, h=None):
		
		h = self.h if h is None else h

		data_euler = euler.euler_compute(self.x0, self.y0, h, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), self.X)
		data_heun  =   heun.heun_compute(self.x0, self.y0, h, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), self.X)

		return data_euler, data_heun

	def compute_exact(self, x):
		
		return 3/2*exp(-x)*x*(exp(2) + exp(2*x))
	
	def compute_local(self, data, h=None):

		h = self.h if h is None else h

		# compute exact x, y
		x_exact = arange(self.x0, self.X+0.01, h)
		y_exact = [self.compute_exact(x) for x in x_exact]

		# compute local error
		x_list  = [pair[0] for pair in data]
		y_list  = [abs(pair[1]-self.compute_exact(pair[0])) for pair in data]

		return x_list, y_list

	def plot_errors(self):

		data_euler, data_heun = self.compute_approx_data()

		# local errors
		euler = self.compute_local(data_euler)
		heun = self.compute_local(data_heun)
		self.axes.plot(euler[0], euler[1], color='y', label='Euler local', visible=True, linewidth=1.5)
		self.axes.plot(heun[0], heun[1], color='r', label='Heun local', visible=True, linewidth=1.5)

		# euler global
		y_euler = []
		y_heun  = []
		x_list = list(range(1, self.N))
		for i in x_list:
			step = abs(self.X - self.x0) / i
			data_euler, data_heun = self.compute_approx_data(step)
			print(max(self.compute_local(data_euler, step)[1]))
			y_euler.append(max(self.compute_local(data_euler, step)[1]))
			y_heun.append(max(self.compute_local(data_heun, step)[1]))

		self.axes.plot(x_list, y_euler, 'y--', marker='.', label='Euler global', visible=True, linewidth=1)
		self.axes.plot(x_list, y_heun, 'r--', marker='.', label='Heun global', visible=True, linewidth=1)

	def plot_approx(self):

		print('x, y, h, X, N = ', self.x0, self.y0, self.h, self.X, self.N)

		# comput exact x, y
		x_exact = arange(self.x0, self.X+0.01, self.h)
		y_exact = [3/2*exp(-x)*x*(exp(2) + exp(2*x)) for x in x_exact]
		self.axes.plot(x_exact, y_exact, color='c', label='Exact', visible=True, marker='.')

		data_euler, data_heun = self.compute_approx_data()
 
 		# euler approx
		x_list = [pair[0] for pair in data_euler]
		y_list = [pair[1] for pair in data_euler]
		self.axes.plot(x_list, y_list, color='y', label='Euler', visible=True, linewidth=1)

		# heun approx
		x_list = [pair[0] for pair in data_heun]
		y_list = [pair[1] for pair in data_heun]
		self.axes.plot(x_list, y_list, color='r', label='Heun', visible=True, linewidth=1)

