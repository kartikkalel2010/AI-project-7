import cv2

image = cv2.imread('368938.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800,500)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimension: [image.shape]")