import cv2

myimage = cv2.imread("img.png",1)
numbertwoimage = cv2.imread("gratisography-cool-cat-800x525.jpg")
print(myimage, numbertwoimage)

cv2.imshow('mythumbnail', myimage)
cv2.waitKey(5000)
cv2.imshow('mythumbnail', numbertwoimage)
cv2.waitKey(5000)
