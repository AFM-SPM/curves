import curves.sim as sim

def test_circle(test_radius, test_n_points):
    # Check that a circle of the correct size
    # and with the correct number of points
    # is returned
    circle = sim.circle(test_radius, test_n_points)