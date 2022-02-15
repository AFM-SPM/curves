import curves.measure as measure
import curves.sim as sim
import numpy as np

def test_curvature(test_curve, test_radius):
    # Check that the right radius of curvature
    # is returned
    curvature = measure.curvature(test_curve, closed=True)
    for index, row in curvature.iterrows():
        print(row['Curvature'])
        np.testing.assert_allclose(row['Curvature'], 1/test_radius, 0.2)


