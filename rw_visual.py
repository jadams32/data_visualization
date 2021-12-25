# This file plots the random walk and displays it to the user

from matplotlib import pyplot as plt
from random_walk import Randomwalk

# Make a random Walk
rw = Randomwalk()
rw.fill_walk()
# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

