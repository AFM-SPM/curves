import pandas as pd

def circle(radius: float, n_points: int) -> pd.DataFrame:
    # Returns a dataframe with columns `x` and `y`
    # These are the co-ordinates of points on a circle of
    # specified radius, with n_points evenly spaced
    dfcircle = pd.DataFrame(index=range(0, n_points * 2))
    for i in range(0, n_points):
        x = -radius + i * radius * 2 / n_points
        y = (radius ** 2 - x ** 2) ** 0.5
        dfcircle.at[i, 'x'] = x
        dfcircle.at[i, 'y'] = y
    for i in range(n_points, n_points*2):
        x = radius - (i - n_points) * radius * 2 / n_points
        y = (radius ** 2 - x ** 2) ** 0.5
        dfcircle.at[i, 'x'] = x
        dfcircle.at[i, 'y'] = y

    return dfcircle
