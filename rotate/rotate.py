#  imports
import argparse, imutils, cv2

# add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")

args = vars(ap.parse_args())

# read image
img = cv2.imread(args["first"])

# loop over the rotation angles
for angle in range(0, 360, 15):
    rotated = imutils.rotate(img, angle)
    cv2.imshow("Rotated (Problematic)", rotated)
    cv2.waitKey(0)
    
# correct rotation
for angle in range(0, 360, 15):
    rotated = imutils.rotate_bound(img, angle)
    cv2.imshow("Rotated (Correct)", rotated)
    cv2.waitKey(0)
