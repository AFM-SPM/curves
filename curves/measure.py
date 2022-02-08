import pandas as pd
import numpy as np
import math



def curvature(curve: pd.DataFrame, adjacent: int = 1, closed: bool = True) -> pd.DataFrame:
    # Returns a dataframe with columns x, y, and RoC
    # x and y come from the input dataframe, c is the radius
    # of curvateure at each point
    # adjacent specified how many points adjacent to the
    # current point should be taken into account when
    # calculating curvature
    # closed specifies if the curve is closed

    curvature = []
    contour = 0
    coordinates = np.zeros([2, adjacent * 2 + 1])
    for i, (x, y) in enumerate(curve):
        # Extracts the coordinates for the required number of points and puts them in an array
        if closed or (adjacent < i < len(curve) - adjacent):
            for j in range(adjacent * 2 + 1):
                coordinates[0][j] = curve[i - j][0]
                coordinates[1][j] = curve[i - j][1]

            # Calculates the angles for the tangent lines to the left and the right of the point
            theta1 = math.atan((coordinates[1][adjacent] - coordinates[1][0]) / (
                    coordinates[0][adjacent] - coordinates[0][0]))
            theta2 = math.atan((coordinates[1][-1] - coordinates[1][adjacent]) / (
                    coordinates[0][-1] - coordinates[0][adjacent]))

            left = coordinates[:, :adjacent + 1]
            right = coordinates[:, -(adjacent + 1):]

            xa = np.mean(left[0])
            ya = np.mean(left[1])

            xb = np.mean(right[0])
            yb = np.mean(right[1])

            # Calculates the curvature using the change in angle divided by the distance
            dist = math.hypot((xb - xa), (yb - ya))
            curvature.append([i, contour, (theta2 - theta1) / dist])

            contour = contour + math.hypot(
                (coordinates[0][adjacent] - coordinates[0][adjacent - 1]),
                (coordinates[1][adjacent] - coordinates[1][adjacent - 1]))

        curve.at[i, 'Curvature'] = curvature

    return curve
