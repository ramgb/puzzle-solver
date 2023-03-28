import cv2


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse clicked at", x, y)

# Read the image
img = cv2.imread('jigsaw.jpg')

# Display the image and wait for user to click on a point
cv2.imshow('image', img)
cv2.setMouseCallback("image", mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
