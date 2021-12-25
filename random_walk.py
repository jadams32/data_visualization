# Learning to make the random walk path. A plot that can be used to represent all kinds of data that
# happens randomly. I learned to make this using the python crash course book.

from random import choice

class Randomwalk:
    """A cLass to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
