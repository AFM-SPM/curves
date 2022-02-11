import curves.sim as sim
import math
import numpy as np

def test_circle(test_radius, test_n_points):
    # Check that a circle of the correct size
    # and with the correct number of points
    # is returned
    circle = sim.circle(test_radius, test_n_points)
    for index, row in circle.iterrows():
        # assert abs(math.hypot(row['x'], row['y']) - test_radius) <= test_radius * 1e-10
        np.testing.assert_allclose(math.hypot(row['x'], row['y']), test_radius, rtol=1e-10)
