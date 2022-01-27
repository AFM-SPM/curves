import pytest

@pytest.fixture
def test_radius():
    return 5.37

@pytest.fixture
def test_n_points():
    return 10

def test_circle(test_radius, test_n_points):
    # Check that a circle of the correct size
    # and with the correct number of points
    # is returned
    pass 