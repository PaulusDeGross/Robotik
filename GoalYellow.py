import cv2
import numpy as np
import math
import Utility as ut
import Values as val


def getMiddle(frame):
    """
    Gets the middle of the Ball using a mask

    :param frame:
    :return: middle of the ball in x, y coords
    """
    lower = np.array(val.GOAL_Y_COLOR[0])  # BALL_COLOR[0] consists of 3 Values: Blue Min, Green Min, Red Min
    upper = np.array(val.GOAL_Y_COLOR[1])  # BALL_COLOR[1] consists of 3 Values: Blue Max, Green Max, Red Max

    mask = cv2.inRange(frame, lower, upper)
    x, y, w, h = cv2.boundingRect(mask)
    return [math.floor(x + w / 2), math.floor(y + h / 2)]


def getAngle(frame):
    """
    Gets the Angle of the Ball using the unwrapped image

    :param frame: unwrapped frame
    :return: the angle of the ball relative to the front of the robot
    """
    frame = ut.unwrap(frame)
    x, y = getMiddle(frame)
    if y >= 180:
        return 360 - y
    return -y


def getDistance(frame):
    raise NotImplementedError


def getData(frame):
    angle = getAngle(frame)
    distance = getDistance(frame)
    return angle, distance