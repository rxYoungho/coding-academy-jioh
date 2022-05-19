# import cv2
# import numpy as np
# import matplotlib.pylab as plt

# # 이미지를 그레이 스케일로 읽기
# img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/commax.png', cv2.IMREAD_GRAYSCALE) 
# # 경계 값을 130으로 지정  ---①
# _, t_130 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)        
# # 경계 값을 지정하지 않고 OTSU 알고리즘 선택 ---②
# t, t_otsu = cv2.threshold(img, -1, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
# print('otsu threshold:', t)                 # Otsu 알고리즘으로 선택된 경계 값 출력


# imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
# for i , (key, value) in enumerate(imgs.items()):
#     plt.subplot(1, 3, i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([]); plt.yticks([])

# plt.show()

# import cv2
 
# # reading the images
# circle = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/init.png')
# star = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/800.png')
 
# # subtract the images
# subtracted = cv2.subtract(star, circle)
 
# # TO show the output
# cv2.imshow('image', subtracted)
 
# # To close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import numpy as np
# import cv2
# # img = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/800.png')
# Z = value.reshape((-1,3))
# # convert to np.float32
# Z = np.float32(Z)
# # define criteria, number of clusters(K) and apply kmeans()
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 2
# ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# # Now convert back into uint8, and make original image
# center = np.uint8(center)
# res = center[label.flatten()]
# res2 = res.reshape((img.shape))
# res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
# bright_count = np.sum(np.array(res2) <= 114)
# print(bright_count)
# bright_count = np.sum(np.array(res2) > 114)
# print(bright_count)
# print(res2)
# cv2.imshow('res2',res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# loop over the unique labels returned by the Watershed
# algorithm

from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
print('1test start')
image = cv2.imread("/Users/Danny/Desktop/GitHub/coding-academy-jioh/black.jpg")
image = cv2.resize(image, (0,0), fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
print('imshow...')
cv2.imshow("Input", image)
# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 24, 255, cv2.THRESH_BINARY)[1]
# thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh", thresh)

D = ndimage.distance_transform_edt(thresh)
# cv2.imshow("D",D)
image_max = ndimage.maximum_filter(gray, size=20, mode='constant')
cv2.imshow("image max", image_max)

localMax = peak_local_max(D, indices=False, min_distance=20,labels=thresh)
# perform a connected component analysis on the local peaks,
# using 8-connectivity, then appy the Watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))

i =0
for label in np.unique(labels):
	# if the label is zero, we are examining the 'background'
	# so simply ignore it
    print('Label:  ',label)
    if label == 0:
        continue
    mask = np.zeros(gray.shape, dtype="uint8")
    mask[labels == label] = 255
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    print(cnts)
    c = max(cnts, key=cv2.contourArea)
    print(c)

    #cropping countours
    if label ==6:
        crop = np.zeros((image.shape[0:2]), np.uint8)
        cv2.fillPoly(crop, [c], (255),8,0)
        # cv2.imshow('fillPoly', crop)
        out1 = cv2.bitwise_and(image, image, mask=crop)
        cv2.imshow('masked', out1)
        

    ((x, y), r) = cv2.minEnclosingCircle(c)
    # cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)

    cv2.drawContours(image, [c], -1, (0,255,0),2)
    cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
