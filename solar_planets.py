import cv2

img = cv2.imread("C:/Users/gurje/Desktop/Python/C104/P104/solar-system.jpg")
cv2.putText(img, "sun", (20,30), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img, "mercury", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "venus", (190,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow("output", img)
cv2.waitKey(0)