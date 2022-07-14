import Utility as ut
import Ball
import GoalYellow
import GoalBlue

img = ut.load_test_image("img/375.png")

ball_angle = Ball.getAngle(img)
ball_x, ball_y = Ball.getMiddle(img)

gy_angle = GoalYellow.getAngle(img)
gy_x, gy_y = GoalYellow.getMiddle(img)

gb_angle = GoalBlue.getAngle(img)
gb_x, gb_y = GoalBlue.getMiddle(img)


print(f"Middle of ball: x={ball_x} | y={ball_y} | angle={ball_angle}")
print(f"Middle of yellow goal: x={gy_x} | y={gy_y} | angle={gy_angle}")
print(f"Middle of blue goal: x={gb_x} | y={gb_y} | angle={gb_angle}")


ut.drawCross(img, ball_x, ball_y, 30, color=(255, 255, 0), line_strength=2)
ut.drawCross(img, gy_x, gy_y, 30, color=(0, 174, 255), line_strength=2)
ut.drawCross(img, gb_x, gb_y, 30, color=(255, 0, 0), line_strength=2)
ut.drawVector(img, 10, 0)

ut.drawRobotMiddleCross(img=img, robot_mask=False)
ut.show_test_image(img)
