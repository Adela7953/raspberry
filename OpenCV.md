     <영상의 표현방법>
  
  1. 그레이스케일 영상
    -흑백 사진처럼 색상 정보가 없이 오직 밝기 정보만으로 구성된 영상
    -밝기 정볼르 256단게로 표현
    
   1-1) (그레이스케일 영상의 픽셀 값 표현)
    -밝기 성분을 0~255 범위의 정수로 표현
    -프로그래밍 언어에서 표현 방법 :18byte
      -C/C++ => unsigned char
      -PYthon => numpy.uint8
      
  2. 트루컬러 영상
    -컬러 사진처럼 색상 정보를 가지고 있어서 다양한 색상을 표현할 수 있는 영상
    -Red,Green, Blue 색 성분을 256 단계로 표현
    --> 256*256*256 = 16,777,216
    
  3. 영상(image)이란?
    -픽셀(pixel)이 바둑판 모양의 격자에 나열되어 있는 형태
    -픽셀: 영상의 기본 단위 , picture element, 화소
    
  4

```#python
import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('cat.bmp')a
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
```
