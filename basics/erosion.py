import cv2
import numpy as np

img = cv2.imread('road.jpg')

kernel = np.ones((5,5), np.uint8)

img_dilated = cv2.dilate(img, kernel, iterations=1)
img_eroded = cv2.erode(img, kernel, iterations=1)

img_eroded_and_dilated = cv2.dilate(img_eroded, kernel, iterations=1)

cv2.imwrite('dilated.png', img_dilated)
cv2.imwrite('eroded.png', img_eroded)

cv2.imwrite('eroded_and_dilated.png', img_eroded_and_dilated)
