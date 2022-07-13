import Utility as ut
import Ball

img = ut.load_test_image("img/375.png")

ut.drawRobotMiddleCross(img=img, c_diameter=420, robot_mask=False)

img = ut.unwrap(img)
#x, y = Ball.getMiddle(img)
#print(f"Middle of Ball: x={x} | y={y}")


#ut.drawCross(img, x, y, 30, line_strength=2)
ut.show_test_image(img)