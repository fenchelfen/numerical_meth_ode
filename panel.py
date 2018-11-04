from tkinter import ttk
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure
from math import cos, sin

import heun, euler

class Plotter(FigureCanvasTkAgg):

	def __init__(self, master):

		figure = Figure()
		self = FigureCanvasTkAgg(figure, master=master)

		axis = figure.add_subplot(111)
		# data = euler.euler_compute(1, 1, 10, lambda x, y: cos(x)-y, 100)
		data = euler.euler_compute(0, 1, 0.1, lambda x, y: -2*pow(y, 2) + x*y + pow(x, 2), 125)

		x_list = [pair[0] for pair in data]
		y_list = [pair[1] for pair in data]

		curve = axis.plot(x_list, y_list)
		# curve = axis.plot(range(90), [cos(x) for x in range(90)])

		self.get_tk_widget().grid(column=0, row=0, sticky='nsew')
	

class MainApplication(ttk.Frame):
	
	def __init__(self, master, *args, **kwargs):

		self = ttk.Frame(root, padding='5 5 5 5')
		self.grid(column=0, row=0, sticky='nsew')
		
		frame = ttk.Frame(self, borderwidth=8)
		frame.grid(column=0, row=0, sticky='nsew')
		frame.rowconfigure(0, weight=1)
		
		notes = ttk.Notebook(frame)
		notes.grid(column=0, row=0, sticky='nsew')
		notes.rowconfigure(0, weight=1)
		# notes.rowconfigure(1, weight=1)
		
		page1 = ttk.Frame(notes)
		page2 = ttk.Frame(notes)
		
		page1.rowconfigure(0, weight=1)
		page1.columnconfigure(0, weight=1)
		# page1.rowconfigure(1, weight=1)
		# page1.columnconfigure(1, weight=1)
		
		notes.add(page1, text='Approximations')
		notes.add(page2, text='Errors')
		
		plot = Plotter(page1)
	
		## Input frame
		input_frame = ttk.Labelframe(self, text='Parameters')
		input_frame.grid(column=1, row=0, sticky='nsew')
		input_frame.rowconfigure(0, weight=1)
		input_frame.rowconfigure(1, weight=5)
		input_frame.rowconfigure(2, weight=5)
		input_frame.rowconfigure(3, weight=5)
		input_frame.rowconfigure(4, weight=5)
		input_frame.columnconfigure(0, weight=1)
		
		field_x0 = tk.StringVar()
		label_x0 = ttk.Label(input_frame, text='x0')
		entry_x0 = ttk.Entry(input_frame, textvariable=field_x0)
			
		field_y0 = tk.StringVar()
		label_y0 = ttk.Label(input_frame, text='y0')
		entry_y0 = ttk.Entry(input_frame, textvariable=field_y0)

		field_X  = tk.StringVar()
		label_X  = ttk.Label(input_frame, text='X')
		entry_X  = ttk.Entry(input_frame, textvariable=field_X)

		field_N  = tk.StringVar()
		label_N  = ttk.Label(input_frame, text='N')
		entry_N  = ttk.Entry(input_frame, textvariable=field_N)

		label_x0.grid(column=0, row=1, sticky='new')
		label_y0.grid(column=0, row=1, sticky='ew')
		label_X.grid(column=0, row=2, sticky='new')
		label_N.grid(column=0, row=2, sticky='ew')
		
		entry_x0.grid(column=1, row=1, sticky='new')
		entry_y0.grid(column=1, row=1, sticky='ew')
		entry_X.grid(column=1, row=2, sticky='new')
		entry_N.grid(column=1, row=2, sticky='ew')

		
		for child in input_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
		
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		root.columnconfigure(0, weight=1)


root = tk.Tk()
root.title('Numerical methods')
root.minsize(800, 600)
# root.maxsize(800, 600)
root.geometry('+5+30')

MainApplication(root)
root.mainloop()
