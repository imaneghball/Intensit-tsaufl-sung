import cv2
import numpy as np
img=cv2.imread("lenagray.jpg",0)
def intnsitätÄnderung(img,Farbtiefe):
    histZahl=[]
    numCut=2**Farbtiefe
    Range=round(255/numCut)
    range2=0
    outImage=np.zeros(img.shape,dtype="uint8")
    while True:
        range2=range2+Range
        if range2>255:
            break
        histZahl.append(range2)
    histZahl.append(255)
    for k in range(len(histZahl)):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i,j]>histZahl[k]:
                    outImage[i,j]=histZahl[k+1]
    cv2.imwrite(f"{Farbtiefe} FarbeTief.jpg",outImage)
    return outImage
out=intnsitätÄnderung(img,1)
cv2.imshow("out",out)
while True:
    key=cv2.waitKey(0) & 0xFF
    if key==27: break
