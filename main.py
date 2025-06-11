import cv2

image = cv2.imread('368938.jpg')

gray_Image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_Image = cv2.resize(gray_Image,(244,224))

cv2.imshow('Processed Image', resized_Image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg', resized_Image)
    print("Image saved successfully!")
else:
    print("Image not saved.")

cv2.destroyAllWindows()

print(f"Processed Image Dimension:{resized_Image.shape}")

