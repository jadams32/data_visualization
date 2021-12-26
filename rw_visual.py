# This file plots the random walk and displays it to the user

from matplotlib import pyplot as plt
from random_walk import Randomwalk

while True:
    # Make a random Walk
    rw = Randomwalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 5), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axis.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    run_again = input("Make another walk? (Y/N): ").lower()
    if run_again == 'n':
        break

