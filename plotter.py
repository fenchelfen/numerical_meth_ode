from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from matplotlib import style
from math import cos, sin, exp

import heun, euler

style.use('seaborn-whitegrid')

class Plotter(FigureCanvasTkAgg):

	def __init__(self, master):

		figure = Figure(dpi=100)
		self = FigureCanvasTkAgg(figure, master=master)

		axes = figure.add_subplot(111, xlabel='x', ylabel='y')
		data_euler = euler.euler_compute(1, 0, 0.1, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), 50)
		data_heun  =   heun.heun_compute(1, 0, 0.1, lambda x, y: 3*x*pow(exp(1), x) - y*(1 - 1/x), 50)
		# data = euler.euler_compute(1, 1, 0.1, lambda x, y: pow(sin(x), 2) + y*(1/tan(x)), 25)
		

		x_list = [x/10 for x in range(10, 61)]
		y_list = [3/2*exp(-x)*x*(exp(2) + exp(2*x)) for x in x_list]
		axes.plot(x_list, y_list, color='c', marker='.', linewidth=1, visible=True, label='Exact')

		x_list = [pair[0] for pair in data_euler]
		y_list = [pair[1] for pair in data_euler]
		axes.plot(x_list, y_list, color='y', label='Euler', visible=True, linewidth=1)

		x_list = [pair[0] for pair in data_heun]
		y_list = [pair[1] for pair in data_heun]
		axes.plot(x_list, y_list, color='r', label='Heun', visible=True, linewidth=1)

		# axes.plot(range(90), [cos(x) for x in range(90)])
		axes.legend(fancybox=False)

		self.get_tk_widget().grid(column=0, row=0, sticky='nsew')

