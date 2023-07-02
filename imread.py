import cv2
img = cv2.imread("beach.jpg")
cv2.imshow("Image", img)
#gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#cv2.imshow("GRay", gray_img)
cv2.waitKey(0)
#print(gray_img)