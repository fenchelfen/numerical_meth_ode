# FIXME PLEASE numerical_meth_ode 📈 

### Introduction
This is a `Python3/Tkinter` application for plotting approximations of a differential equation solution using the following methods:

* Euler
* Heun (Improved Euler)
* Runge-Kutta

Here is the initial value problem (IVP)

$$\begin{cases}
	y^{\prime} &=& 3xe^{x} - y\ (1-\frac{1}{x})  \\
	y\ (1) &=& 0
\end{cases}$$

This document shows how to get the exact solution of the IVP and then demostrates all of the methods listed above.

#### Contents
1. Exact solution
2. Methods overview
3. Application overview

### 1. Exact solution
Linear, nonhomogeneous ode of the first degree
$$y^{\prime} = 3xe^{x} - y\ (1-\frac{1}{x})$$
Lets find the general solution first.

Solve the complementary equation
$$y^{\prime} + y\ (1 - \frac{1}{x}) = 0$$
Turn it into separable form and apply integration
$$\begin{align} &\int{\frac{dy}{y}} = \int{(\frac{1}{x}-1)dx} \\  \\&\ln{|y|}  = \ln{|x|} - x + C  \\ \\ &y = xke^{-x}\end{align}$$
Assume that k equals = 1. To find the general solution, apply substitution
$$\begin{cases}
	y &=& uy_1 \\
	y^{\prime} &=& u'y_1 + uy_1
\end{cases}$$
where y~1~ is the solution of the complementary.

Substituting y' and y into the intial equation, we get
$$\begin{align} &u' = \frac{3xe^{x}}{y_1}  \\ \\ &u = \int{\frac{3xe^x dx}{xe^{-x}}}\end{align}$$

Substituting y back and integrating gives the general solution
$$\begin{align} &y = xe^{-x} \int{\frac{3xe^{x} dx}{xe^{-x}}} \\ \\
&y = x\frac{3xe^{x}}{2} + Ce^{-x}\end{align}$$

Using the initial conditions given, we derive the constant C
$$C = \frac{-3e^{2}}{2}$$
Thus, we have the IVP solution
$$y = \frac{3xe^{-x}}{2}(e^{2x} - e^2)$$

-------


### 2. Methods overview

All approximations below are computed with the following parameters:

* x0 = 1
* y0 = 0
* X = 5
* h = 0.1
* n0 = 3
* N = 9

#### Comparison with the exact solution

The first figure shows the plots on a relatively large scale and the step is tiny, so it is not easy to see how approximations differ from the exact solution.

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Approximations.png )

Here we can clearly observe that Euler approximation gradually goes much lower than the exact. This fact has a good explanation, we are trying to approximate a function which is convex.

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Approximations_zoom.png)

#### Local errors

Local error continues upwards as x grows, we were lucky enough to get a predictable function.

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Local.png)

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Local_zoom.png)

#### Total errors

Total error continues downwards as the number of grid cells increases.

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Total.png)
-------

### 3. Application overview

Tkinter is a stock framework for Python which is relatively simple and reliable, this is why I have chosen it. Despite the fact that Tkinter does not have a particulary great outlook, it was fixed by means of `ttk` -- a themed widget set.

Since the application is fully educational in nature, the standard python3 functionality was used (e.g. `pow` and `exp`).

Each method (Euler, Heun and Runge-Kutta) is implemented as a separate module. Though this is not the best design decision, those modules were implemented long before the assignment was given. Thus, they were heavilly tested and could be easily integrated with the rest.

Plotting is made by an autonomous class `Plotter` which inherits from tkinter's backend `Canvas`. This is made for the purpose of modularity, now plotter can be embedded in almost any kind of tkinter interface.

Application was structured following the rules listed on [https://stackoverflow.com/a/17470842/9308909]()


All graphics is handled by a custom class `MainApplication` which inherits from `ttk.Frame`.

Inside the window there are two instances of `ttk.Frame` input and plotting. First frame containts `ttk.Notebook` with several objects of `tkk.Frame` holding our canvas for drawing.

#### Interesting snippets

Tkinter interface initialization.

```Python
def __init__(self, master, *args, **kwargs):

    super().__init__(root, padding='5 5 5 5')
    self.grid(column=0, row=0, sticky='nsew')

    frame = ttk.Frame(self, borderwidth=8)
    frame.grid(column=0, row=0, sticky='nsew')
    frame.rowconfigure(0, weight=1)

    notes = ttk.Notebook(frame)
    notes.grid(column=0, row=0, sticky='nsew')
    notes.rowconfigure(0, weight=1)

    page1 = ttk.Frame(notes)
    page2 = ttk.Frame(notes)
    page3 = ttk.Frame(notes)

    notes.add(page1, text='Approximations')
    notes.add(page2, text='Local')
    notes.add(page3, text='Total')

    plot1 = plotter.Plotter(page1)
    plot2 = plotter.Plotter(page2)
    plot3 = plotter.Plotter(page3)

    <...>

```
A function for updating plots when the input is changed.

```Python
def update_canvas(self, x0, y0, h, X, n0, N, flag):

     self.x0 = x0
     self.y0 = y0
     self.h  = h
     self.X  = X
     self.N  = N
     self.n0 = n0

     self.axes.clear()

     plots = {
         0: self.plot_approx,
         1: self.plot_local,
         2: self.plot_total
     }

     plots.get(flag, 'No such plot')()

     self.axes.legend(fancybox=False)
     self.draw_idle()

```

```Python
def heun_compute(x0, y0, h, func, X):

    x, y = x0, y0
    pairs = list()
    while (x <= X):
        pairs.append((x,y));
        y = heun_new(x, y, h, func)
        x += h
    return pairs

```

#### UML and packages

![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/Plotter__inherit__graph.png)  ![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/MainApplication__inherit__graph.png) ![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/packages_Pyreverse.png)


![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/inherit_graph_2.png)
![GitHub](https://github.com/fenchelfen/numerical_meth_ode/blob/master/Pictures/inherit_graph_1.png)

#### Author
Mikhail Lyamets BS17-07

