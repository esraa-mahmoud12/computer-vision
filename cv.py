import os
import io
import PIL.Image as Image
import numpy as np
from array import array




def imOpen(filename):
  img = Image.open(filename)
  pix = img.load()
  new = Image.new("L",img.size)
  w,h=img.size
  for i in range(0,img.size[0]-1):
    for j in range(0,img.size[1]-1):
      x  = pix[i,j] 
      rgb=x[0]+x[1]+x[2]
      grey_scale=rgb/3
      num = int( grey_scale)
      x=(num,num,num)
      new.putpixel((i,j),num)      

  new = new.save("grey.jpg") 
  return new


def toStrH(fname):
  img = Image.open(fname)
  pix = img.load()
  w,h=img.size
  a = "H"+ " "+str(w) + " "+str(h)+"\n"
  for i in range(0,img.size[0]-1):
    b=pix[i,0]
    t=b[0]
    a += str(t)
    for j in range(1,img.size[1]):
        x  = pix[i,j]
        y = x[0]
        if t==y:
          j=j+1 
        else:
          a =a+ str(i)+" "+str(j)+" "+str(i)+" "+str(j)
  a= a+"\n"      
  return a


def toStrV(fname):
  img = Image.open(fname)
  pix = img.load()
  w,h=img.size
  a = "H"+ " "+str(w) + " "+str(h)+"\n"
  for i in range(0,img.size[0]-1):
    b=pix[i,0]
    t=b[0]
    a += str(t)
    for j in range(1,img.size[1]):
        x  = pix[i,j]
        y = x[0]
        if t==y:
          j=j+1 
        else:
          a =a+ str(i)+" "+str(j)+" "+str(i)+" "+str(j)
  a= a+"\n"      
  return a

def toFile(fname,run_code):
  outF = open(fname, "a")
  outF.write(run_code)
  outF.close()

def toImg(fname):
  file1 = open(fname, 'r') 
  first_line = file1.readline()#take first line to determine if H orV & w,h
  size= first_line.split()
  w=int(size[1])
  h=int(size[2])
  new = Image.new("L",(w,h))
  next(file1)#to get second line
  for line in file1:
    count = 1
    if count == w-1 :
      break;
    else:
      count=count+1
      l = line.split()
      for i in range(0,len(l)-1):
        color=int(l[i])
        if i ==len(l)-2:
           break;
        elif l[i+1]==l[i+2]:
           new.putpixel((int(l[i+1]),count),color)
           i=i+3
        else:
           j=int(l[i+1])
           m=int(l[i+2])
           for k in range(j, m):
             new.putpixel((count,k),color)
  file1.close()
  new = new.save("geeks.jpg") 


c = "/content/Bars.bmp"
d = toStrH(c)
a = toFile("/content/file.txt",d)
