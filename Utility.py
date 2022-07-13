import cv2
import numpy as np
from _thread import start_new_thread
import Values as val


def load_test_image(path):
    img = cv2.imread(path)
    return img


def show_test_image(img, title=""):
    cv2.imshow(title, img)
    cv2.waitKey(0)


def unwrap(img):
    img = cv2.warpPolar(img, (val.MIRROR_RADIUS, 360), val.CENTER_IMAGE, val.MIRROR_RADIUS,
                        cv2.WARP_POLAR_LINEAR + cv2.WARP_FILL_OUTLIERS)[:,  # Abwickeln des Bildes
          val.ROBOT_RADIUS:val.MIRROR_RADIUS]  # Zuschneiden des Bildes
    return img


def drawCross(img, x_middle, y_middle, size=50, color=(0, 0, 0), line_strength=1):
    x_pt1 = [int(x_middle - size / 2), int(y_middle)]
    x_pt2 = [int(x_middle + size / 2), int(y_middle)]
    y_pt1 = [int(x_middle), int(y_middle - size / 2)]
    y_pt2 = [int(x_middle), int(y_middle + size / 2)]
    cv2.line(img, x_pt1, x_pt2, color, line_strength)
    cv2.line(img, y_pt1, y_pt2, color, line_strength)
    return img


def drawRobotMiddleCross(
        img,
        c_diameter,
        robot_offset=val.CENTER_IMAGE,
        robot_mask=False
):
    w = img.shape[1]
    h = img.shape[0]

    x_pt1 = [int(val.CENTER_IMAGE[0] + c_diameter / 2), int(val.CENTER_IMAGE[1])]
    x_pt2 = [int(val.CENTER_IMAGE[0] - c_diameter / 2), int(val.CENTER_IMAGE[1])]
    y_pt1 = [int(val.CENTER_IMAGE[0]), int(val.CENTER_IMAGE[1] + c_diameter / 2)]
    y_pt2 = [int(val.CENTER_IMAGE[0]), int(val.CENTER_IMAGE[1] - c_diameter / 2)]

    if robot_mask:
        cv2.circle(img, val.CENTER_IMAGE, val.ROBOT_RADIUS, (0, 0, 0), -1)
    cv2.circle(img, val.CENTER_IMAGE, int(c_diameter / 2), (0, 0, 255), 1)

    cv2.line(img, y_pt1, y_pt2, (0, 0, 255), 1)
    cv2.line(img, x_pt1, x_pt2, (0, 0, 255), 1)
    return img
