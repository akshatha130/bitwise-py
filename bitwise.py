import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)
img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,255),-1)

bitAnd = cv2.bitwise_and(img2,img1)
bitOr = cv2.bitwise_or(img2,img1)
bitXor = cv2.bitwise_xor(img1,img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("And",bitAnd)
cv2.imshow("or",bitOr)
cv2.imshow("xor",bitXor)
cv2.imshow("not1",bitNot1)
cv2.imshow("not2",bitNot2)

cv2.waitKey()
cv2.destroyAllWindows()

