import cv2
import numpy as np
import math
import Utility as ut
import Values as val

def getMiddle(frame):
    """
    Gets the middle of the Yellow Goal using a mask

    :param frame:
    :return: middle of the ball in x, y coords
    """
    lower = np.array(val.GOAL_Y_COLOR[0])  # BALL_COLOR[0] consists of 3 Values: Blue Min, Green Min, Red Min
    upper = np.array(val.GOAL_Y_COLOR[1])  # BALL_COLOR[1] consists of 3 Values: Blue Max, Green Max, Red Max

    mask = cv2.inRange(frame, lower, upper)
    x, y, w, h = cv2.boundingRect(mask)
    return [math.floor(x + w / 2), math.floor(y + h / 2), w, h]


def getAngleTan(frame):
    """
    Gets the Angle of the yellow goal using a tangent using tan^-1(m)

    :param frame:
    :return:
    """
    x, y, w, h = getMiddle(frame)
    x = x - val.CENTER_IMAGE[0]
    y = val.CENTER_IMAGE[1] - y
    print(f"{x}, {y}")

    if x > 0 and y < 0:
        return math.degrees(np.arctan(y / x) + math.pi * 2)
    elif x < 0 and y < 0:
        return math.degrees(np.arctan(y / x) + math.pi * 3)
    elif x > 0 and y > 0:
        return math.degrees(np.arctan(y / x))
    elif x < 0 and y > 0:
        return math.degrees(np.arctan(y / x) + math.pi)


def getAngle(frame):
    """
    Gets the Angle of the Yellow Goal using the unwrapped image

    :param Any frame: unwrapped frame
    :return: the angle of the goal relative to the front of the robot
    """
    frame = ut.unwrap(frame)
    x, y, w, h = getMiddle(frame)
    if h < 360:
        if y >= 180:
            return 360 - y
        return -y
    else:
        frame = ut.scrollImage(frame)
        x, y, w, h = getMiddle(frame)
        if y >= 180:
            return 360 - y
        return 180 - y


def getDistance(frame):
    raise NotImplementedError


def getData(frame):
    angle = getAngle(frame)
    distance = getDistance(frame)
    return angle, distance