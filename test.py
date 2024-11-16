import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load an color image in grayscale
img = cv2.imread('ai-generated-8762055_1920.png', cv2.IMREAD_GRAYSCALE)

# Show the image
plt.imshow(cv2.cvtColor(img, cv2.COLORMAP_RAINBOW))
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()