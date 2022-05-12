import numpy as np
import cv2 as cv
ciz = False
beyazmod = True
siyahmod= True
ix,iy = -1,-1

def cizim(event,x,y,flags,param):
    global ix,iy,ciz,beyazmod,siyahmod
    if event == cv.EVENT_LBUTTONDOWN:
        ciz = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE and beyazmod == True:
        if ciz == True:
            cv.circle(img,(x,y),5,(255,255,255),-1)
        else:
            pass
    elif event == cv.EVENT_MOUSEMOVE and siyahmod==False:
        if ciz ==True:
            cv.circle(img,(x,y),10,(0,0,0),-1)
        else:
            pass
    elif event == cv.EVENT_LBUTTONUP:
        ciz = False


img = np.zeros((512,512,3), np.uint8)
img[:]=(100,70,90)
cv.namedWindow('image')
cv.setMouseCallback('image',cizim)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('w'):
        beyazmod = not beyazmod

    elif k == ord("b"):
        siyahmod = not siyahmod

    elif k == 27:
        break

cv.destroyAllWindows()





