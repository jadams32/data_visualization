# This file plots the random walk and displays it to the user

from matplotlib import pyplot as plt
from random_walk import Randomwalk

while True:
    # Make a random Walk
    rw = Randomwalk()
    rw.fill_walk()
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    run_again = input("Make another walk? (Y/N): ").lower()
    if run_again == 'n':
        break

