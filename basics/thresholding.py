import cv2

img = cv2.imread('road.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('thresh.png', thresh)
