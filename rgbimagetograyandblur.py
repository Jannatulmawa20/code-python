import cv2
naturalimg = cv2.imread("img.png")
imgGray = cv2.cvtColor(naturalimg, cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 0)
print(naturalimg)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Gray image", imgGray)
cv2.imshow("orginal image", naturalimg)
cv2.waitKey(0)