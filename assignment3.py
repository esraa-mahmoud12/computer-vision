import PIL.Image as Image
from PIL import Image, ImageFilter 
import numpy as np
from array import array
from statistics import median
import matplotlib.pyplot as plt



def multiply(x,y):
  v=[]
  for i in range (0,y):
    v.append(x)
  return v

def median_filter(img):
   gray = img.convert('L')
   image_array = np.array(gray, dtype='int64')
   height = image_array.shape[0]
   width = image_array.shape[1]
   kernal=[[1,3,1],
          [3,5,3],
          [1,3,1]]
   start=len(kernal)//2  
   #print(image_array)  
   for i in range(start,height-start):

     if (len(kernal) % 2)==0:

       backIRange = i-start
       forwordIRange = i+(start)
     else:

       backIRange = i-start
       forwordIRange = i+(start+1)

     for j in range (start,width-start):

       if (len(kernal) % 2)==0:

         backJRange = j-start
         forwordJRange = j+(start)
       else:

         backJRange = j-start
         forwordJRange = j+(start+1)
       v=[]
       
       imgPart = image_array[backIRange:forwordIRange,backJRange:forwordJRange]
       #get the image part that would be using with kernal
       #print(imgPart)
       for k in range(0,imgPart.shape[0]):
         for l in range(0,imgPart.shape[1]):
#use the method multiply to append in the list the list of image pixel with the kernal limit 
           x=multiply(imgPart[k][l],kernal[k][l])
           v.append(x)
       array=[]
       for o in range(0,len(v)):
         element=v[o]
         for t in range(0,len(element)):
           array.append(element[t])
## to arrange the list to have all integers in integer form not list
       array.sort()#sort the array
       n = len(array) 
       image_array[i][j]= array[n//2] #to get the median element  

   return image_array






img = Image.open('/content/BarCode2.jpg')

 
filterResult = median_filter(img)
plt.imshow(filterResult, cmap="gray")
plt.imsave("Camera_Filt_3.jpg", filterResult, cmap="gray")
plt.show()                  
   
   




