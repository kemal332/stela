import cv2
import pytesseract
from PIL import Image
import numpy as np

img = cv2.imread("harder.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("start")
print(pytesseract.image_to_string(img))
print("end")

cv2.imshow("result", img)
cv2.waitKey(0)
