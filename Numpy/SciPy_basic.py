'''
Numpy는 고성능의 다차원 배열 객체와 이를 다룰 도구를 제공합니다.
numpy를 바탕으로 만들어진 SciPy는, numpy 배열을 다루는 많은 함수를 제공하며
다양한 과학, 공학분야에서 유용하게 사용됩니다.
공식페이지 : https://docs.scipy.org/doc/scipy/reference/index.html
'''

'''
SciPy는 이미지를 다룰 기본적인 함수들을 제공합니다. 예를들자면, 디스크에 저장된 이미지를 numpy 배열로 읽어 들이는 
함수가 있으며, numpy 배열을 디스크에 이미지로 저장하는 함수도 있고, 이미지의 크기를 바꾸는 함수도 있습니다. 
이 함수들의 간단한 사용 예시입니다:
'''

#from scipy.misc import imread
from scipy.misc import imread, imsave, imresize

# JPEG 이미지를 numpy 배열로 읽어들이기
img = imread('assets/cat.jpg')
print(img.dtype, img.shape)  # 출력 "uint8 (400, 248, 3)"

# 각각의 색깔 채널을 다른 상수값으로 스칼라배함으로써
# 이미지의 색을 변화시킬 수 있습니다.
# 이미지의 shape는 (400, 248, 3)입니다;
# 여기에 shape가 (3,)인 배열 [1, 0.95, 0.9]를 곱합니다;
# numpy 브로드캐스팅에 의해 이 배열이 곱해지며 붉은색 채널은 변하지 않으며,
# 초록색, 파란색 채널에는 각각 0.95, 0.9가 곱해집니다
img_tinted = img * [1, 0.95, 0.9]

# 색변경 이미지를 300x300픽셀로 크기 조절.
img_tinted = imresize(img_tinted, (300, 300))

# 색변경 이미지를 디스크에 기록하기
imsave('assets/cat_tinted.jpg', img_tinted)
