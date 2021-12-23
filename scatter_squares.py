# Here I recreate the scatter plot project from the book python crash course.

# Importing pyplot and giving it the alis plt
from matplotlib import pyplot as plt

# X and Y values using list comprehension and range
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# styling and color maps for the plot
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 5100, 0, 150000000000])

# Here we show the plot and then save a copy in the same folder
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
