import cv2
import numpy as np
from matplotlib import pyplot



image=cv2.imread("Car.jpeg")
image_norm=cv2.normalize(image,None,alpha=0,beta=250,norm_type=cv2.NORM_MINMAX)

cv2.imshow("ORIGINAL",image)
cv2.imshow("NORMALIZE EDILMIS",image_norm)

histogram=cv2.calcHist([image_norm],[0],None,[256],[0,256])

pyplot.plot(histogram)
pyplot.show()


cv2.waitKey(0)
cv2.destroyAllWindows()