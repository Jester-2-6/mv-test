import cv2

star = cv2.imread('star.jpg')
dot = cv2.imread('dot.jpg')

sub_result = cv2.subtract(star, dot)

cv2.imwrite('sub_result.png', sub_result)
