import pytest

import curves.sim as sim

@pytest.fixture
def test_radius():
    return 5.37

@pytest.fixture
def test_n_points():
    return 10

@pytest.fixture
def test_curve(test_radius, test_n_points):
    return sim.circle(test_radius, test_n_points)