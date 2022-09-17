import cv2, imutils

img = cv2.imread("road.jpg")

(h,w) = img.shape[:2]

print('height: ', h, '\n','width: ', w)

(b,g,r) = img[100,100]

print('blue: ', b, '\n','green: ', g, '\n','red: ', r)

img_out = img.copy()
cv2.rectangle(img_out, (1000,1000), (1350,1250), (0,150,255), 5)
cv2.putText(img_out, 'This is an orange box', (1010, 980), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,150,255), 2)

cv2.imwrite("img_out.png", img_out)
