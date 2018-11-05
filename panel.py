from ttkthemes import themed_tk
from tkinter import ttk
import tkinter as tk
import sys

import time

import plotter

LARGE_FONT= ('Helvetica', 9)

class MainApplication(ttk.Frame):

	field_x0: tk.StringVar 
	field_y0: tk.StringVar
	field_X : tk.StringVar
	field_h : tk.StringVar
	field_N : tk.StringVar

	def __init__(self, master, *args, **kwargs):

		super().__init__(root, padding='5 5 5 5')
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
		
		plot = plotter.Plotter(page1)
	
		## Input frame
		input_frame = ttk.Labelframe(self, text='Parameters')
		input_frame.grid(column=1, row=0, sticky='nsew')
		input_frame.rowconfigure(0, weight=1)
		input_frame.rowconfigure(1, weight=5)
		input_frame.rowconfigure(2, weight=5)
		input_frame.rowconfigure(3, weight=5)
		input_frame.rowconfigure(4, weight=5)
		input_frame.rowconfigure(5, weight=5)
		input_frame.columnconfigure(0, weight=1)
		
		global field_x0, field_y0, field_X, field_h, field_N
		field_x0 = tk.StringVar()
		field_y0 = tk.StringVar()
		field_X  = tk.StringVar()
		field_h  = tk.StringVar()
		field_N  = tk.StringVar()

		label_x0 = ttk.Label(input_frame, text='x0')
		entry_x0 = ttk.Entry(input_frame, textvariable=field_x0)
			
		label_y0 = ttk.Label(input_frame, text='y0')
		entry_y0 = ttk.Entry(input_frame, textvariable=field_y0)

		label_X  = ttk.Label(input_frame, text='X')
		entry_X  = ttk.Entry(input_frame, textvariable=field_X)

		label_h = ttk.Label(input_frame, text='h')
		entry_h = ttk.Entry(input_frame, textvariable=field_h)

		label_N  = ttk.Label(input_frame, text='N')
		entry_N  = ttk.Entry(input_frame, textvariable=field_N)

		label_x0.grid(column=0, row=1, sticky='new')
		label_y0.grid(column=0, row=1, sticky='ew')
		label_X.grid(column=0, row=2, sticky='new')
		label_h.grid(column=0, row=2, sticky='ew')
		label_N.grid(column=0, row=3, sticky='new')
		
		entry_x0.grid(column=1, row=1, sticky='new')
		entry_y0.grid(column=1, row=1, sticky='ew')
		entry_X.grid(column=1, row=2, sticky='new')
		entry_h.grid(column=1, row=2, sticky='ew')
		entry_N.grid(column=1, row=3, sticky='new')

		button   = ttk.Button(input_frame, text='Plot', command=lambda: self.redraw(plot))
		button.grid(column=0, row=4, columnspan=2, sticky='ew')

		self.master.after(200, lambda: entry_x0.focus())
		self.master.after(200, lambda: root.bind('<Return>', lambda e: self.redraw(plot)))

		for child in input_frame.winfo_children():
			if isinstance(child, ttk.Label):
				child.config(font=LARGE_FONT)
			child.grid_configure(padx=5, pady=5)
		
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		root.columnconfigure(0, weight=1)

	
	def redraw(self, plot):

		global field_x0, field_y0, field_X, field_h, field_N
		x0 = float(field_x0.get())
		y0 = float(field_y0.get())
		X  = float(field_X.get())
		h  = float(field_h.get())
		N  = float(field_N.get())
		plot.update_canvas(x0, y0, h, X, N)

root = themed_tk.ThemedTk()
root.set_theme('clam')
style = ttk.Style()
# style.configure('.', font=LARGE_FONT)

root.title('Numerical methods')
root.minsize(800, 600)
# root.maxsize(800, 600)
root.geometry('+5+30')

MainApplication(root)
root.mainloop()
