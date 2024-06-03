
# Matplotlib Exercises

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline is used if you are using Jupyter Notebook or Google Colab
%matplotlib inline

# Data
x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Exercise 1
# Create a figure object called fig using plt.figure()
fig = plt.figure()

# Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
ax = fig.add_axes([0, 0, 1, 1])

# Plot (x, y) on that axes and set the labels and titles to match the plot below:
ax.plot(x, y)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')

# Display the plot
fig

# Exercise 2
# Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])

# Plot (x, y) on both axes. And call your figure object to show it.
ax1.plot(x, y)
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_title('Title')

ax2.plot(x, y)
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_title('Title')

# Display the plot
fig

# Exercise 3
# Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
fig = plt.figure()

main_axis = fig.add_axes([0, 0, 1, 1])
inset_axis = fig.add_axes([0.2, 0.5, 0.4, 0.4])

# Plot (x, z) on the main axes
main_axis.plot(x, z)
main_axis.set_xlabel('X Label')
main_axis.set_ylabel('Z Label')
main_axis.set_title('Main Plot')

# Plot (x, y) on the inset axes
inset_axis.plot(x, y)
inset_axis.set_xlabel('X Label')
inset_axis.set_ylabel('Y Label')
inset_axis.set_title('Inset Plot')
inset_axis.set_xlim(20, 22)
inset_axis.set_ylim(30, 50)

# Display the plot
fig

# Exercise 4
# Use plt.subplots(nrows=1, ncols=2) to create the plot below.
fig, axes = plt.subplots(nrows=1, ncols=2)

# Plot (x, y) and (x, z) on the axes. Play around with the linewidth and style
axes[0].plot(x, y, 'b--', linewidth=2)  # Dashed blue line
axes[1].plot(x, z, 'r', linewidth=3)    # Solid red line

# Display the plot
fig

# See if you can resize the plot by adding the figsize() argument in plt.subplots() and copying and pasting your previous code.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

# Plot (x, y) and (x, z) on the axes. Play around with the linewidth and style
axes[0].plot(x, y, 'b--', linewidth=2)  # Dashed blue line
axes[1].plot(x, z, 'r', linewidth=3)    # Solid red line

# Display the plot
fig
