#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:54:44 2021

@author: marla
"""


import matplotlib.pyplot as plt
import numpy as np
import cv2

image_name = 'wanda.jpeg'
background_name = 'city.jpeg'



def processImages(img, background_image):
    #convert to rgb
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb_background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
    
    img_shape = rgb_image.shape
    background_shape = rgb_background_image.shape
    print('image shape ', img_shape)
    print('background_shape ', background_shape)
    #resize
    if img_shape[0]<background_shape[0]:
        #crop background
        rgb_background_image = rgb_background_image[0:img_shape[0],:]
    else:
        rgb_image = rgb_image[0:background_shape[0],:]
      
    if img_shape[1]<background_shape[1]:
        rgb_background_image = rgb_background_image[:,0:img_shape[1]]
    else:
        rgb_image = rgb_image[:,0:background_shape[1]]
    print('after image shape ', rgb_image.shape)
    print('after background_shape ', rgb_background_image.shape)    
    return rgb_image, rgb_background_image


img = cv2.imread(image_name)
img_copy = np.copy(img)
plt.imshow(img)
background_img = cv2.imread(background_name)
background_copy = np.copy(background_img)

rgb_image, rgb_background_image = processImages(img_copy, background_copy)
#plt.imshow(rgb_image)
#plt.imshow(rgb_background_image)
lower_blue = np.array([0,50,150])
upper_blue = np.array([220,200,255])
mask = cv2.inRange(rgb_image, lower_blue, upper_blue)
#plt.imshow(mask, cmap = 'gray')

masked_img = rgb_image.copy()
masked_img[mask!=0]=[0,0,0]
#plt.imshow(masked_img)

#cut out shape from background
masked_background = rgb_background_image.copy()
masked_background[mask==0]=[0,0,0]
#plt.imshow(masked_background)

#final image
final_image = masked_img + masked_background
plt.imshow(final_image)

'''


img = cv2.imread(image_name)
img_copy = np.copy(img)
rgb_image = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
rgb_image = rgb_image[:,200:1600]

lower_blue = np.array([0,0,160])
upper_blue = np.array([20,190,255])
mask = cv2.inRange(rgb_image, lower_blue, upper_blue)

plt.imshow(mask, cmap = 'gray')

masked_img = rgb_image.copy()
masked_img[mask!=0]=[0,0,0]
plt.imshow(masked_img)
print('image size', masked_img.shape)

#get the new background
background_image = cv2.imread(background_name)
print(background_image.shape)
#convert to rgb
rgb_background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
img_height = masked_img.shape[0]
img_width = masked_img.shape[1]
#crop to size
rgb_background_image = rgb_background_image[0:img_height, 0:img_width]

#cut out shape from background
masked_background = rgb_background_image.copy()
masked_background[mask==0]=[0,0,0]
plt.imshow(masked_background)

#final image
final_image = masked_img + masked_background
plt.imshow(final_image)
'''