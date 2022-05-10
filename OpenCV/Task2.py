
import cv2
import numpy as np

image=cv2.imread("Car.jpeg")

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
'''
hsv değişkeni atayıp cv2.cvtColor fonkisyonu ile , image değişkenine atamış 
olduğumuz Car.jpeg resmini OpenCV'de default olarak gelen BGR renk uzayından
HSV renk uzayına taşıdık.
'''

lower_red =np.array([170,100,100])
upper_red =np.array([180,255,255])
lower_red_=np.array([1,50,50])
upper_red_=np.array([10,255,255])
'''
burada HSV renk uzayının değerlerinin oldupu görseli açıp ,kırmızı renge denk gelen
kısımları NumPy dizileri ile değişkenlerimize atadık.([H,S,V])
Kırmızı renk tonları HSV renk skalasında başta ve sonda oldugundan iki kısmı da ayrı ayrı
almak zorunda kaldık.(kırmızı H değeri 168-169 lardan başlıyor 180 de bitiyor.
devamında kırmızı tonlarını skalanın başında tekrar görüyoruz. burada kırmızı H değeri
0 dan başlıyor yaklaşık 10-11'e kadar gidiyor.
Eğer burada kırmızı renk degil mavi veya yeşil renk tonlarını kullanmış olsaydık,
renk skalasında kırmızı renkte oldugu gibi kesintiye uğramadıgı için , ayrı ayrı yazmamıza
gerek kalmayacaktı.
'''


mask= cv2.inRange(hsv,lower_red,upper_red)
mask_=cv2.inRange(hsv,lower_red_,upper_red_)
'''
burada inRange fonksiyonu ile mask ve mask_ değişkenlerine threshold uygulandı.
'''

mask_result=mask+mask_
'''
iki değişkeni birleştirip max_result fonksiyonuna atadık.
Böylece 170-180 H değerleri arasından gelen kırmızı threshold  görüntüleri ile
0-10 H arasından gelen kırmızı threshold görüntüleri birleşmiş oldu. 
Car.jpeg resminde görülen kırmızı aracın bazı kısımlarında 170-180H bazı kısımlarında
0-10H aralıgında kırmızı tonları oldugu için birleştiğinde daha net bir görüntü aldık.
'''


cv2.imshow("ORIGINAL",image)
cv2.imshow("MASK edilmis",mask_result)

cv2.waitKey(0)
cv2.destroyAllWindows()



