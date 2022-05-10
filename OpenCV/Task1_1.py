# --TASK1_1--ÇALIŞMA--
# Thresholding ile Car.jpeg görselinde ki arabayı arkaplandan ayırma
# Adaptive Thresholding

import cv2

image=cv2.imread("Car.jpeg",0)

ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

thresh3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
'''
Adaptive Threshold uygulamalarında mantık görseli belirli piksellere bölüp,
bu piksellerin renk ortalamalarını alarak bu ortalamalara göre
Thresholding işlemini yapmasıdır.
Adaptive Thresholding uygulamasını yapmak için tek değişken yeterlidir.
Oluşturduğumuz thresh2 ve thresh 3 değişkenlerine cv2.adaptiveThreshold fonksiyonunu
çağırıyoruz. 
cv2.adaptiveThreshold() fonksiyonunun yazımı--> 
cv2.adaptiveThreshold(src,MaxValue,adaptiveMethod,thresholdType,blocksize) şeklindedir.
**Burada src parametresi kaynak, yani image değişkenine atadığımız resmimizdir.
**Maxvalue değeri en yüksek değer olan 255 alıyoruz.
**adaptiveMethod değeri için ise;
iki adet adaptivemethod fonksiyonu bulunur.Bunlar cv2.ADAPTIVE_THRESH_MEAN_C ve 
cv2.ADAPTIVE_THRESH_GAUSSIAN_C 'dir. Bu çalışmamız da iki türün de çıktılarını inceleyip
karşılaştırmak için iki türü de çağırıyoruz. Böylece çıktılardan istenilen kaliteyi hangi 
fonksiyonla yakalayacağımızı seçebiliriz.
**thresholdType kısmında ise daha önce öğrendiğimiz istediğimiz 
THRESH_..... kalıbını kullanabiliriz.
Bu çalışmada cv2.THRESH_BINARY kullandık.
**blocksize kısmında ise kaça kaç pikseller içinde ortalama alınıp çıktı verileceğini 
belirledik.burada ki değerler değiştirilip denenerek en iyi çıktı yakalanmaya çalışılır.


'''

cv2.imshow("ORIGINAL",image)
cv2.imshow("SIMPLE THRESHOLDING uygulanmis",thresh1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C uygulanmis",thresh2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C uygulanmis",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()
