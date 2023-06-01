import cv2

img = cv2.imread('ucak.jpeg', cv2.IMREAD_GRAYSCALE)

#k=3
img_blur3 = cv2.GaussianBlur(img, (3,3), 0)

edge = cv2.Canny(img_blur3, 20, 30)
cv2.imwrite('canny-gauss3.png',edge)

edge = cv2.Canny(img_blur3, 40, 50)
cv2.imwrite('canny-gauss4.png',edge)

#k=5
img_blur5 = cv2.GaussianBlur(img, (5,5), 0)

edge = cv2.Canny(img_blur5, 20, 30)
cv2.imwrite('canny-gauss5.png',edge)

edge = cv2.Canny(img_blur5, 40, 50)
cv2.imwrite('canny-gauss6.png',edge)
