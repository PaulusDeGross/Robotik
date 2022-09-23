import Utility as ut
import numpy as np
import Ball
import GoalYellow
import GoalBlue

img = ut.load_test_image("img/109.png")

ball_angle = Ball.getAngle(img)
ball_middle = Ball.getMiddle(img)
ball_x = ball_middle[0]
ball_y = ball_middle[1]

gy_angle = GoalYellow.getAngle(img)
gy_middle = GoalYellow.getMiddle(img)
gy_x = gy_middle[0]
gy_y = gy_middle[1]

gb_angle = GoalBlue.getAngle(img)
gb_middle = GoalBlue.getMiddle(img)
gb_x = gb_middle[0]
gb_y = gb_middle[1]


print(f"Middle of ball: x={ball_x} | y={ball_y} | angle={ball_angle}")
print(f"Middle of yellow goal: x={gy_x} | y={gy_y} | angle={gy_angle}")
print(f"Middle of blue goal: x={gb_x} | y={gb_y} | angle={gb_angle}")


ut.drawCross(img, ball_x, ball_y, 30, color=(0, 111, 255), line_strength=2)
ut.drawCross(img, gy_x, gy_y, 30, color=(0, 255, 255), line_strength=2)
ut.drawCross(img, gb_x, gb_y, 30, color=(255, 0, 0), line_strength=2)

ut.drawRobotMiddleCross(img=img, robot_mask=False)

ut.show_test_image(img)