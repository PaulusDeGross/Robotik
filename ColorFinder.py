import cv2
import numpy as np
import Utility as ut
import Values as val

VALS = val.GOAL_B_COLOR
PATH = "img/109.png"


def empty(i):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Blue min", "Trackbars", VALS[0][0], 255, empty)
cv2.createTrackbar("Blue max", "Trackbars", VALS[1][0], 255, empty)
cv2.createTrackbar("Green min", "Trackbars", VALS[0][1], 255, empty)
cv2.createTrackbar("Green max", "Trackbars", VALS[1][1], 255, empty)
cv2.createTrackbar("Red min", "Trackbars", VALS[0][2], 255, empty)
cv2.createTrackbar("Red max", "Trackbars", VALS[1][2], 255, empty)

while True:

    img = cv2.imread(PATH)

    b_min = cv2.getTrackbarPos("Blue min", "Trackbars")
    b_max = cv2.getTrackbarPos("Blue max", "Trackbars")
    g_min = cv2.getTrackbarPos("Green min", "Trackbars")
    g_max = cv2.getTrackbarPos("Green max", "Trackbars")
    r_min = cv2.getTrackbarPos("Red min", "Trackbars")
    r_max = cv2.getTrackbarPos("Red max", "Trackbars")

    lower = np.array([b_min, g_min, r_min])
    upper = np.array([b_max, g_max, r_max])

    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    x, y, w, h = cv2.boundingRect(mask)
    rect = cv2.rectangle(result.copy(), (x, y), (x + w, y + h), (255, 255, 0), 1)
    rect2 = cv2.rectangle(img.copy(), (x, y), (x + w, y + h), (255, 255, 0), 1)
    x_m = x + w / 2
    y_m = y + h / 2

    x1 = [int(x_m - w / 2), int(y_m)]
    x2 = [int(x_m + w / 2), int(y_m)]
    y1 = [int(x_m), int(y_m - h / 2)]
    y2 = [int(x_m), int(y_m + h / 2)]

    cv2.line(rect2, x1, x2, (255, 255, 0), 1)
    cv2.line(rect2, y1, y2, (255, 255, 0), 1)

    cv2.line(rect, x1, x2, (255, 255, 0), 1)
    cv2.line(rect, y1, y2, (255, 255, 0), 1)

    print(f"Middle: x = {x + w / 2} | y = {y + h / 2}")

    ut.drawCross(rect2, x_middle=int(val.CENTER_IMAGE[0]), y_middle=int(val.CENTER_IMAGE[1]), color=(0, 255, 0),
                 line_strength=2)
    ut.drawCross(mask, x_middle=int(val.CENTER_IMAGE[0]), y_middle=int(val.CENTER_IMAGE[1]), color=(0, 255, 0),
                 line_strength=2)
    ut.drawCross(rect, x_middle=int(val.CENTER_IMAGE[0]), y_middle=int(val.CENTER_IMAGE[1]), color=(0, 255, 0),
                 line_strength=2)
    ut.drawCross(rect2, x_middle=int(x_m), y_middle=int(y_m), color=(0, 0, 255), line_strength=2)
    ut.drawCross(mask, x_middle=int(x_m), y_middle=int(y_m), color=(0, 0, 255), line_strength=2)
    ut.drawCross(rect, x_middle=int(x_m), y_middle=int(y_m), color=(0, 0, 255), line_strength=2)

    cv2.imshow("BGR", rect2)
    cv2.imshow("MASK", mask)
    cv2.imshow("RES", rect)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
