import cv2
import numpy as np


# Creating mouse callback function
def draw_circle(event, x, y, flags, param):
    if (event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img, (x, y), 50, (123, 125, 200), -1)
    # Creating a black image, a window and bind the function to window


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()