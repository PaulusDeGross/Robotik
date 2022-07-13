import Utility as ut
import Ball

img = ut.load_test_image("img/109.png")
angle = Ball.getAngle(img)

x, y = Ball.getMiddle(img)

print(f"Middle of Ball: x={x} | y={y} | angle={angle}")


ut.drawRobotMiddleCross(img=img, robot_mask=True)
ut.drawCross(img, x, y, 30, color=(255, 255, 0), line_strength=2)
ut.show_test_image(img)
