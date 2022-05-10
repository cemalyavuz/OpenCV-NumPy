# --TASK1--ÇALIŞMA--
# Thresholding ile Car.jpeg görselinde ki arabayı arkaplandan ayırma
#Simple Thresholding

import cv2

image=cv2.imread("Car.jpeg",0)
'''thresholding işlemi için görüntü gri tonlamada olmalıdır.
Bunun için görüntümüzü imread ederken 0 kullanılmadılır. '''

ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
'''
kullanılan eşik için ret , çıktı eşikli görüntü için
 thresh 1 değişkenleri atandı.  cv2.threshold fonksiyonu eşik uygulamak için çağrılır.
 cv2.threshold kullanımı--> threshold(src,thresh,maxval,type[ ,dst]) şeklindedir.
 **Burada src kullanacağımız kaynak adıdır. Üzerinde işlem yapacağımız Car.jpeg resmimiz
 image değişkeninin içinde olduğu için kaynak olarak image değişkeni atarız.
 **Thresh belirlediğimiz eşik değeridir. Burada eşik değerini 127 olarak belirledik
 (global değer olarak 127 kullanılıyor neden ? 100 kullansak temiz, istediğimiz sonucu 
 alamaz mıydık?). image değişkenine atadıgımız resmimiz de ,belirlediğimiz eşik değerinin 
 altında kalan pikseller eşik değerini geçemediği için 0 yapılır.
 ** maxval için en yüksek parametre olan 255 değerini atadık.
 ** type[,dst] için cv2 modülünü kullanarak çeşitli THRESH uygulayıcılarından birini 
 çağırırız.THRESH_BINARY kullandık.
 
 '''
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_OTSU)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_MASK)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh6=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh7=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
ret,thresh8=cv2.threshold(image,127,255,cv2.THRESH_TRIANGLE)
'''
cv2 modulunde bulunan bütün THRESH fonksiyonlarını incelemek için tıpkı
 thresh1 değişkeninde olduğu gibi çağırıyoruz.
'''


cv2.imshow("ORIGINAL",image)
cv2.imshow("THRESH_BINARY uygulanmis",thresh1)
''' 
cv2.imshow komutu ile resmimizin yani image'in "ORIGINAL" adı ile gösterilmesini saglarız.
daha sonra tekrar cv2.imshow komutu ile resmimizin THRESHOLDİNG uygulanmış hali olan 
"THRESH_BINARY uygulanmis" adı verilen thresh1 ' in gösterilmesini sağlarız.
'''

cv2.imshow("THRESH_BINARY_INV uygulanmis",thresh2)
cv2.imshow("THRESH_OTSU uygulanmis",thresh3)
cv2.imshow("THRESH_MASK uygulanmis",thresh4)
cv2.imshow("THRESH_TRUNC uygulanmis",thresh5)
cv2.imshow("THRESH_TOZERO uygulanmis",thresh6)
cv2.imshow("THRESH_TOZERO_INV uygulanmis",thresh7)
cv2.imshow("THRESH_TRIANGLE uygulanmis",thresh8)
'''
cv2 modulünün sağladığı bütün THRESH fonksiyonlarının çıktılarını inceliyoruz.
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
son olarak cv2.waitKey() komutuna 0 yazarak açılacak olan penceremizin otomatik olarak
kapatılmasını önleriz. cv2.destroyAllWindows() komutu ile işlem sonunda açık olan tüm 
pencerelerimizi herhangi bir tuşla kapatırız.
'''