import cv2
import numpy as np


def empty(i):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Blue min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Blue max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Green min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Green max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Red min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Red max", "Trackbars", 255, 255, empty)

while True:

    img = cv2.imread("img/375.png")

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
    print(f"Middle: x = {x + w / 2} | y = {y + h / 2}")

    cv2.imshow("BGR", img)
    cv2.imshow("MASK", mask)
    cv2.imshow("RES", rect)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
