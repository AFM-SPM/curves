import pandas as pd
import math

def circle(radius: float, n_points: int) -> pd.DataFrame:
    """
    Generate a circle of points.

    Returns a dataframe with columns 'x' and 'y' corresponding to 
    points uniformly spaced in a circular formation. 

    Parameters 
    ----------
    radius : float
        The radius of the circle 
    n_ponts : int 
        The number of points that the circle should be
        comprised of.

    Returns
    ----------
    out : pandas.DataFrame
        Dataframe containing columns 'x' and 'y' as coordinates
        for points on the circle.

    """

    points = [(math.cos(2*math.pi/n_points*x)*radius,math.sin(2*math.pi/n_points*x)*radius) for x in range(0,n_points+1)]
    df = pd.DataFrame(data=points, columns=['x','y'])
    return df