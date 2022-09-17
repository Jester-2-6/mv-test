#  imports
import argparse, imutils, cv2

# add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")

args = vars(ap.parse_args())

# read image
img = cv2.imread(args["first"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=10, minSize=(750, 750))

# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
# show the detected cat faces

cv2.imwrite("img.png", img)
