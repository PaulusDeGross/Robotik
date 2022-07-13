import cv2
import numpy as np
import math
import Utility as ut
import Values as val


def getMiddle(frame):
    """
    Gets the middle of the Ball using a mask

    :param frame:
    :return:
    """
    lower = np.array(val.BALL_COLOR[0])
    upper = np.array(val.BALL_COLOR[1])

    mask = cv2.inRange(frame, lower, upper)
    x, y, w, h = cv2.boundingRect(mask)
    return [math.floor(x + w / 2), math.floor(y + h / 2)]


def getAngle(frame):
    """
    Gets the Angle of the Ball using the unwrapped image

    :param frame: unwrapped frame
    :return: y: the
    """
    frame = ut.unwrap(frame)
    x, y = getMiddle(frame)
    return y