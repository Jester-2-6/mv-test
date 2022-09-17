#  imports
from skimage.metrics import structural_similarity as ssim
import argparse, imutils, cv2

# add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second")

args = vars(ap.parse_args())

# read imgs
imgA = cv2.imread(args["first"])
imgB = cv2.imread(args["second"])

# convert to grayscale
grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

# compute ssim
(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold and contour
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# draw contours
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imgA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imgB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
# display
cv2.imshow("Original", imgA)
cv2.imshow("Modified", imgB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
