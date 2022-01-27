import pandas as pd

def curvature(curve: pd.DataFrame, adjacent: int = 1, closed: bool = True) -> pd.DataFrame:
    # Returns a dataframe with columns x, y, and RoC
    # x and y come from the input dataframe, c is the radius
    # of curvateure at each point
    # adjacent specified how many points adjacent to the
    # current point should be taken into account when
    # calculating curvature
    # closed specifies if the curve is closed
    pass