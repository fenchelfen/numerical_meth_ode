from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from matplotlib import style
from math import cos, sin, exp

import heun, euler

style.use('seaborn-whitegrid')

class Plotter(FigureCanvasTkAgg):

	def __init__(self, master):

		figure = Figure(dpi=100)
		super().__init__(figure, master=master)
		self.axes = figure.add_subplot(111, xlabel='x', ylabel='y')
		self.get_tk_widget().grid(column=0, row=0, sticky='nsew')

		self.exact = self.axes.plot()
		self.euler = self.axes.plot()
		self.heun  = self.axes.plot()

	def update_canvas(self, x0, y0, h, X, N):

		print('x, y, h, X, N = ', x0, y0, h, X, N)
		data_euler = euler.euler_compute(x0, y0, h, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), X)
		data_heun  =   heun.heun_compute(x0, y0, h, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), X)
		# data = euler.euler_compute(1, 1, 0.1, lambda x, y: pow(sin(x), 2) + y*(1/tan(x)), 25)

		# x_list = [x/10 for x in range(10, 61)]
		# y_list = [3/2*exp(-x)*x*(exp(2) + exp(2*x)) for x in x_list]
		# self.exact = self.axes.plot(x_list, y_list, color='c', marker='.', linewidth=1, visible=True, label='Exact')
 
 
		self.axes.clear()
		x_list = [pair[0] for pair in data_euler]
		y_list = [pair[1] for pair in data_euler]
		print(y_list)
		self.axes.plot(x_list, y_list, color='y', label='Euler', visible=True, linewidth=1)

		x_list = [pair[0] for pair in data_heun]
		y_list = [pair[1] for pair in data_heun]
		self.axes.plot(x_list, y_list, color='r', label='Heun', visible=True, linewidth=1)

		self.axes.legend(fancybox=False)
		self.draw_idle()

