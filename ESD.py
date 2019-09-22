#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[77]:


img  = cv2.imread("C:/Users/Sahith/Desktop/ESD/IMG-0298.JPG",0)
h1,w1 = img.shape[:2]
h = int(0.2*h1)
w = int(0.2*w1)
img_res = cv2.resize(img,(w, h))#, interpolation = cv.INTER_CUBIC)
t = 250
kernel = np.ones((5,5),np.uint8)
cv2.imshow("rooda",img_res)
retval, th = cv2.threshold(img_res, t, 255, cv2.THRESH_BINARY)
erosion = cv2.erode(th,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
cv2.imshow("img",dilation)
cv2.imshow("threshold",th)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(dilation.any())

#mask = np.zeros(h,w)
if(dilation.any()==0 ):
    print("1")
    t1 = 235
    retval, th = cv2.threshold(img_res, t1, 255, cv2.THRESH_BINARY)
    erosion = cv2.erode(th,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    cv2.imshow("img1",dilation)
    cv2.imshow("threshold1",th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if(dilation.any()==0):
    print("2")
    t2 = 220
    retval, th = cv2.threshold(img_res, t2, 255, cv2.THRESH_BINARY)
    erosion = cv2.erode(th,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    cv2.imshow("img2",dilation)
    cv2.imshow("threshold2",th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
sumr = np.zeros((1,h))    
sumc = np.zeros((1,w))
print(sum(sumr.shape))
print(sum(sumc.shape))

for i in range(h):
    sumr[0,i] = sum(dilation[i ,: ])
    
for i in range(w):
    sumc[0,i] = sum(dilation[: ,i])    
    
print(sum1.shape)


# In[78]:


m=0;
i=0;
while(m==0):
    m=sumr[0,i]
    i=i+1  
rstart=i

while(m):
    m=sumr[0,i]
    i=i+1
rstop=i


# In[79]:


m=0;
i=0;
while(m==0):
    m=sumc[0,i]
    i=i+1  
cstart=i

while(m):
    m=sumc[0,i]
    i=i+1
cstop=i


# In[82]:


import math
print(rstart,rstop,cstart,cstop)
x = (cstart + cstop)/2
y = (rstart + rstop)/2
math.degrees(math.atan(y/x))


# In[ ]:




