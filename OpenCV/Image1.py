import cv2
from matplotlib import pyplot

image= cv2.imread("Car.jpeg",0)

cv2.imshow("ImageWindow",image)

pyplot.imshow(image,cmap="gray")
pyplot.show()

x=cv2.waitKey(0)
if x==27:
    print("ESC key pressed")
elif x==ord("a"):
    print("a key pressed")
    cv2.imwrite("Cargrey.jpeg",image)

#cv2.destroyWindow("ImageWindow")

cv2.destroyAllWindows()