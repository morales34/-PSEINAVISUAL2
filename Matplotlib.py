#introduccion a Matplotlib

#Matplotlib tutorial for beginners

#1. Introduction
#2. Overview of Python Visualization Tools
#3. Introduction to Matplotlib
#4. Import Matplotlib

#import matplotlib
#import matplotlib.pyplot
#import matplotlib.pyplot as plt

# Import dependencies

import Numpy as np
import Pandas as pd

# Import Matplotlib

import Matplotlib,pyplot as plt 

#5. Displaying Plots in Matplotlib

#Plotting from a script
#Plotting from an IPython shell
#Plotting from a Jupyter notebook

x1 = np.linspace(0, 10, 100)


# create a plot figure
fig = plt.figure()

plt.plot(x1, np.sin(x1), 'y*')
plt.plot(x1, np.cos(x1), '--');

#6. Matplotlib Object Hierarchy

#7. Matplotlib API Overview
#8. Pyplot API

"""plt.gcf ( ) # get current figure

plt.gca ( ) # get current axes"""

# create a plot figure
plt.figure()


# create the first of two panels and set current axis
plt.subplot(1, 2, 1)   # (rows, columns, panel number)
plt.plot(x1, np.sin(x1))


# create the second of two panels and set current axis
plt.subplot(1, 2, 2)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1));


# get current figure information

print(plt.gcf())


# get current axis information

print(plt.gca())

#Visualization with Pyplot

plt.plot([1, 2, 3, 4])
plt.ylabel('Numbers')
plt.xlabel('eje x')
plt.show()

#plot() - A versatile command

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


#State-machine interface

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()

#Formatting the style of plot

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


#Working with NumPy arrays

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

#9. Object-Oriented API

# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)


# Call plot() method on the appropriate object
ax[0].plot(x1, np.sin(x1), 'b-')
ax[1].plot(x1, np.cos(x1), 'b-');

#Objects and Reference


fig = plt.figure()

x2 = np.linspace(0, 5, 10)
y2 = x2 ** 2

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x2, y2, 'r')

axes.set_xlabel('x2')
axes.set_ylabel('y2')
axes.set_title('title');

#Figure and Axes

"""fig = plt.figure()

ax = plt.axes()"""

fig = plt.figure()

ax = plt.axes()

#10. Figure and Subplots

#fig = plt.figure()

#ax1 = fig.add_subplot(2, 2, 1)

"""ax2 = fig.add_subplot(2, 2, 2)

ax3 = fig.add_subplot(2, 2, 3)

ax4 = fig.add_subplot(2, 2, 4)"""


#11. First plot with Matplotlib

plt.plot([1, 3, 2, 4], 'b-')

plt.show( )

#Specify both Lists

"""x3 = range(6)

plt.plot(x3, [xi**2 for xi in x3])

plt.show()"""

x3 = np.arange(0.0, 6.0, 0.01) 

plt.plot(x3, [xi**2 for xi in x3], 'b-') 

plt.show()

#12. Multiline Plots

x4 = range(1, 5)

plt.plot(x4, [xi*1.5 for xi in x4])

plt.plot(x4, [xi*3 for xi in x4])

plt.plot(x4, [xi/3.0 for xi in x4])

plt.show()

#13. Parts of a Plot

#14. Saving the Plot

# Saving the figure

fig.savefig('plot1.png')


# Explore the contents of figure

from IPython.display import Image

Image('plot1.png')


# Explore supported file formats


fig.canvas.get_supported_filetypes() 

#15. Line Plot

# Create figure and axes first
fig = plt.figure()

ax = plt.axes()

# Declare a variable x5
x5 = np.linspace(0, 10, 1000)


# Plot the sinusoid function
ax.plot(x5, np.sin(x5), 'b-'); 

#16. Scatter Plot

x7 = np.linspace(0, 10, 30)

y7 = np.sin(x7)

plt.plot(x7, y7, 'o', color = 'black');

#17. Histogram

data1 = np.random.randn(1000)

plt.hist(data1); 

#18. Bar Chart

data2 = [5. , 25. , 50. , 20.]

plt.bar(range(len(data2)), data2)

plt.show() 

#19. Horizontal Bar Chart


data2 = [5. , 25. , 50. , 20.]

plt.barh(range(len(data2)), data2)

plt.show() 

#20. Error Bar Chart

x9 = np.arange(0, 4, 0.2)

y9 = np.exp(-x9)

e1 = 0.1 * np.abs(np.random.randn(len(y9)))

plt.errorbar(x9, y9, yerr = e1, fmt = '.-')

plt.show();


#21. Stacked Bar Chart
A = [15., 30., 45., 22.]

B = [15., 25., 50., 20.]

z2 = range(4)

plt.bar(z2, A, color = 'b')
plt.bar(z2, B, color = 'r', bottom = A)

plt.show()


#22. Pie Chart

plt.figure(figsize=(7,7))

x10 = [35, 25, 20, 20]

labels = ['Computer', 'Electronics', 'Mechanical', 'Chemical']

plt.pie(x10, labels=labels);

plt.show()

#23. Boxplot
data3 = np.random.randn(100)

plt.boxplot(data3)

plt.show();

#24. Area Chart

# Create some data
x12 = range(1, 6)
y12 = [1, 4, 6, 8, 4]

# Area plot
plt.fill_between(x12, y12)
plt.show()


plt.stackplot(x12, y12)

#25. Contour Plot
# Create a matrix
matrix1 = np.random.rand(10, 20)

cp = plt.contour(matrix1)

plt.show()

plt.contour(matrix.N)
#26. Styles with Matplotlib Plots

print(plt.style.availabe)

# View list of all available styles

print(plt.style.available)

plt.style.use('seaborn-bright')

# Set styles for plots

plt.style.use('seaborn-bright')

#27. Adding a grid

x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.grid(True)

plt.show()

#28. Handling axes

x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.axis()   # shows the current axis limits values

plt.axis([0, 5, -1, 13])

plt.show()

x15 = np.arange(1, 5)

plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)

plt.xlim([1.0, 4.0])

plt.ylim([0.0, 12.0])

#29. Handling X and Y ticks

u = [5, 4, 9, 7, 8, 9, 6, 5, 7, 8]

plt.plot(u)

plt.xticks([2, 4, 6, 8, 10])
plt.yticks([2, 4, 6, 8, 10])

plt.show()

#30. Adding labels

plt.plot([1, 3, 2, 4])

plt.xlabel('This is the X axis')

plt.ylabel('This is the Y axis')

plt.show()


#31. Adding a title

plt.plot([1, 3, 2, 4])

plt.title('First Plot')

plt.show()

#32. Adding a legend

x15 = np.arange(1, 5)

fig, ax = plt.subplots()

ax.plot(x15, x15*1.5)
ax.plot(x15, x15*3.0)
ax.plot(x15, x15/3.0)

ax.legend(['Normal','Fast','Slow']);


x15 = np.arange(1, 5)

fig, ax = plt.subplots()

ax.plot(x15, x15*1.5, label='Normal')
ax.plot(x15, x15*3.0, label='Fast')
ax.plot(x15, x15/3.0, label='Slow')

ax.legend();

#33. Control colours

x16 = np.arange(1, 5)

plt.plot(x16, 'r')
plt.plot(x16+1, 'g')
plt.plot(x16+2, 'b')

plt.show()

#34. Control line styles

x16 = np.arange(1, 5)

plt.plot(x16, '--', x16+1, '-.', x16+2, ':')

plt.show()

#35. Summary
