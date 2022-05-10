# --TASK1_1_1--ÇALIŞMA--
# Thresholding ile Car.jpeg görselinde ki arabayı arkaplandan ayırma
# otsu Thresholding
import cv2

image=cv2.imread("Car.jpeg",0)

ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

thresh3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

ret,thresh4=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
otsu thresholding uygulamaların da yazım simple thresholding ile  benzerdir. 
fakat farkı eşik değeri kendimiz oluşturmayız. 0-255 aralığını veririz. 
Otomatik işlem yapılır . seçtiğimiz THRESH_... fonkisyonuna ek olarak + ile 
THRESH_OTSU eklenir böylece otsu thresholding işlemi gerçekleştirilmiş olur.
Diğer Threshlenmiş gorsellerle karşılaştırıp inceleriz.
'''


cv2.imshow("ORIGINAL",image)
cv2.imshow("SIMPLE THRESHOLDING uygulanmis",thresh1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C uygulanmis",thresh2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C uygulanmis",thresh3)
cv2.imshow("THRESH_OTSU uygulanmis",thresh4)

cv2.waitKey(0)
cv2.destroyAllWindows()
