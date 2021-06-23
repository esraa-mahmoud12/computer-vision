import PIL.Image as Image
from numpy import*
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

image = Image.open('/content/L4.jpg')
pix = image .load()
x  = pix[0,0] 
print(x)
temp=asarray(image) 
temp2=asarray(image)
x=temp.shape[0] 
y=temp.shape[1]*temp.shape[2] 
temp.resize((x,y)) # a 2D array 
print(x,y)
print(temp) 



def CalculateIntegral(array2D,array1D,x,y):
 
  w=len(array1D)

  test=np.zeros(w)
  test.resize(x,y)

  testii=np.zeros(w)
  testii.resize(x,y)
  
  for i in range(x):
   test[i,0]=array2D[i,0]#to copy the first column

  for j in range(x): 
    for k in range(y):
      test[j,k]=test[j,k-1]+array2D[j,k]

  for m in range(x): 
    for n in range(y):
      testii[m,n]=testii[m-1,n]+test[m,n]
  return testii

def CalculateLocalSum(fname,x1,y1,x2,y2):
  img = Image.open(fname)
  pix = img.load()
  if(x1 < x2 and y1 < y2):
    x= pix[x1,y1] 
    sum=0
    sum+=x[0]+x[1]+x[2]
  return sum(sum , CalculateLocalSum(fname,x1+1,y1+1,x2,y2))

z=CalculateIntegral(temp,temp2,x,y)
