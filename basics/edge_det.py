import cv2

img = cv2.imread('road.jpg')

blurred = cv2.bilateralFilter(img, 9, 75, 75)
edges = cv2.Canny(blurred, 10, 50)

cv2.imwrite('edges.png', edges)
