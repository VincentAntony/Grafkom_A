from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time
import numpy as np

gameoverposition=1000 
slowness=.01
crash=False 
middleline_y=300 
centerx=247 
objx=[]
objy=[600,750,750,900,1050,1050,1200,1200,1500,1650,1650,1800]
objradius=[]

for x in range(12): 
     objx.append(random.choice([247-65,247,247+65]))
     objradius.append(12)

temp=random.choice([247-65,247,247+65])
sqcenterx=temp
sqcentery=975
x1=sqcenterx-15
x2=sqcenterx+15
x3=sqcenterx+15
x4=sqcenterx-15
y1=sqcentery-15
y2=sqcentery-15
y3=sqcentery+15
y4=sqcentery+15

score=0

def objcirc():
 global objy
 global objx
 global objradius
 i=0
 for x in range(len(objx)):
     cinc(objx[i], objy[i], objradius[i])
     i+=1

def objsquare():
 global x1,y1,x2,y2,x3,y3,x4,y4
 mqda(x1,y1,x2,y2,x3,y3,x4,y4)

def rotatedeg(degree): 
 global x1,y1,x2,y2,x3,y3,x4,y4,sqcentery,sqcenterx
 a = math.cos(math.radians(degree))
 b = math.sin(math.radians(degree))
 r = np.array([[a, -b, 0],
               [b, a, 0],
               [0, 0, 1]])
 negtrans = np.array([[1, 0, (-1) * sqcenterx],
                      [0, 1, (-1) * sqcentery],
                      [0, 0, 1]])
 transback = np.array([[1, 0, sqcenterx],
                       [0, 1, sqcentery],
                       [0, 0, 1]])
 temp = np.matmul(transback, r)
 compmat = np.matmul(temp, negtrans)

 v1 = np.array([[x1],
                [y1],
                [1]])
 v2 = np.array([[x2],
                [y2],
                [1]])
 v3 = np.array([[x3],
                [y3],
                [1]])
 v4 = np.array([[x4],
                [y4],
                [1]])

 temp=np.matmul(compmat,v1)
 x1=temp[0][0]
 y1=temp[1][0]

 temp = np.matmul(compmat, v2)
 x2 = temp[0][0]
 y2 = temp[1][0]

 temp = np.matmul(compmat, v3)
 x3 = temp[0][0]
 y3 = temp[1][0]

 temp = np.matmul(compmat, v4)
 x4 = temp[0][0]
 y4 = temp[1][0]

def middlelines(y): 
 glColor3f(1, 1, 1)
 mldamedium(215, y, 215, y+200)
 mldamedium(215, y-100, 215, y-300 )
 mldamedium(215, y+300, 215, y+500)
 mldamedium(280, y, 280, y + 200)
 mldamedium(280, y - 100, 280, y - 300)
 mldamedium(280, y + 300, 280, y + 500)

def draw_points(x, y):
 glPointSize(2) 
 glBegin(GL_POINTS)
 glVertex2f(x,y) 
 glEnd()

def draw_pointsmedium(x, y):
 glPointSize(10) 
 glBegin(GL_POINTS)
 glVertex2f(x,y) 
 glEnd()

def draw_pointsbig(x, y):
 glPointSize(30)
 glBegin(GL_POINTS)
 glVertex2f(x,y) #
 glEnd()

def FindZoneAndCvtTo0(x1,y1,x2,y2): 
 res=[] 
 dx = x2 - x1
 dy = y2 - y1
 diff=abs(dx)-abs(dy)
 if diff>=0: 
     if (dx>=0): 
         if dy>=0: 
             res.append(x1)
             res.append(y1)
             res.append(x2)
             res.append(y2)
             res.append(0)
         else:
             res.append(x1)
             res.append(y1*(-1))
             res.append(x2)
             res.append(y2*(-1))
             res.append(7)
     else:
         if dy >= 0: 
             res.append(x1*(-1))
             res.append(y1)
             res.append(x2*(-1))
             res.append(y2)
             res.append(3)
         else:
             res.append(x1*(-1))
             res.append(y1*(-1))
             res.append(x2*(-1))
             res.append(y2*(-1))
             res.append(4)
 else: 
     if (dx >= 0):
         if dy >= 0: 
             res.append(y1)
             res.append(x1)
             res.append(y2)
             res.append(x2)
             res.append(1)
         else: 
             res.append(y1*(-1))
             res.append(x1)
             res.append(y2*(-1))
             res.append(x2)
             res.append(6)
     else:
         if dy >= 0:
             res.append(y1)
             res.append(x1*(-1))
             res.append(y2)
             res.append(x2*(-1))
             res.append(2)
         else:
             res.append(y1*(-1))
             res.append(x1*(-1))
             res.append(y2*(-1))
             res.append(x2*(-1))
             res.append(5)
 return res
     
def Cvt0ToX(x,y,zone):
 res=[]
 if(zone==0):
     res.append(x)
     res.append(y)
 elif zone==1:
     res.append(y)
     res.append(x)
 elif zone==2:
     res.append(y*(-1))
     res.append(x)
 elif zone==3:
     res.append(x*(-1))
     res.append(y)
 elif zone==4:
     res.append(x*(-1))
     res.append(y*(-1))
 elif zone==5:
     res.append(y*(-1))
     res.append(x*(-1))
 elif zone==6:
     res.append(y)
     res.append(x*(-1))
 else: # zone==7:
     res.append(x)
     res.append(y*(-1))
 return res
def mlda(x1,y1,x2,y2):
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
     tp=Cvt0ToX(x,y,prezone)
     draw_points(tp[0],tp[1])
     if(d>0):
         x+=1
         y+=1
         d=d+dNE 
     else:
         x+=1
         d=d+dE 
#------------------------------------
def mldamedium(x1,y1,x2,y2):
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsmedium(tp[0],tp[1])
     #Updating pixel
     if(d>0):
         x+=1
         y+=1
         d=d+dNE  
     else:
         x+=1
         d=d+dE 
def mldabig(x1,y1,x2,y2):
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsbig(tp[0],tp[1])
     if(d>0):
         x+=1
         y+=1
         d=d+dNE  
     else: 
         x+=1
         d=d+dE 

def mcda(centerX,centerY,r):
 
 d=1-r 
 x=0
 y=r
 while(y>=x): 
     draw_circle_points(x,y,centerX,centerY)
     if(d>=0):
         d=d+2*x-2*y+5
         x += 1
         y -= 1
     else: 
         d=d+2*x+3
         x += 1
def draw_circle_points(x,y,centerX,centerY):
 for i in range(8):

     temp=Cvt1ToX(x,y,i) 
     draw_points(temp[0]+centerX,temp[1]+centerY)
def Cvt1ToX(x,y,zone):
 res=[]
 if(zone==0):
     res.append(y)
     res.append(x)
 elif zone==1:
     res.append(x)
     res.append(y)
 elif zone==2:
     res.append(x*(-1))
     res.append(y)
 elif zone==3:
     res.append(y*(-1))
     res.append(x)
 elif zone==4:
     res.append(y*(-1))
     res.append(x*(-1))
 elif zone==5:
     res.append(x*(-1))
     res.append(y*(-1))
 elif zone==6:
     res.append(x)
     res.append(y*(-1))
 else: 
     res.append(y)
     res.append(x*(-1))
 return res
def mqda(x1,y1,x2,y2,x3,y3,x4,y4):
 mldamedium(x1,y1,x2,y2)
 mldamedium(x2, y2, x3, y3)
 mldamedium(x3, y3, x4, y4)
 mldamedium(x4, y4, x1, y1)

def mqdafilled(x1,y1,x2,y2,x3,y3,x4,y4):
 for x in range(x1,x2+1,25): 
     mldabig(x,y1,x,y4)


def mqdafilledSmall(x1,y1,x2,y2,x3,y3,x4,y4):

 for x in range(x1,x2+1): 
     mlda(x,y1,x,y4)
def drawnum(x,y,num,width, height):
 if num=='0':
     mlda(x-width,y-height,x-width,y+height) 
     mlda(x + width, y - height, x + width, y + height)  
     mlda(x - width, y + height, x + width, y + height) 
     mlda(x - width, y - height, x + width, y - height) 
 elif num=='1':
     mlda(x + width, y - height, x + width, y + height)
 elif num=='2':
     mlda(x + width, y , x + width, y + height)  
     mlda(x - width, y + height, x + width, y + height)  
     mlda(x - width, y - height, x + width, y - height)  
     mlda(x - width, y - height, x - width, y )  
     mlda(x - width, y , x + width, y )  
 elif num=='3':
     mlda(x - width, y + height, x + width, y + height)  
     mlda(x - width, y - height, x + width, y - height)  
     mlda(x - width, y, x + width, y) 
     mlda(x + width, y - height, x + width, y + height)  
 elif num=='4':
     mlda(x - width, y, x + width, y) 
     mlda(x + width, y - height, x + width, y + height)  
     mlda(x - width, y + height, x - width, y)  
 elif num=='5':
     mlda(x - width, y + height, x + width, y + height)  
     mlda(x - width, y - height, x + width, y - height)  
     mlda(x - width, y, x + width, y)  
     mlda(x - width, y + height, x - width, y)  
     mlda(x + width, y, x + width, y - height)  
 elif num=='6':
     mlda(x - width, y, x + width, y)  
     mlda(x - width, y - height, x - width, y + height)  
     mlda(x - width, y - height, x + width, y - height) 
     mlda(x + width, y, x + width, y - height)  
     mlda(x - width, y + height, x + width, y + height)  
 elif num=='7':
     mlda(x - width, y - height, x + width, y + height)  
     mlda(x - width, y + height, x + width, y + height)  
 elif num=='8':
     mlda(x - width, y + height, x + width, y + height)  
     mlda(x - width, y - height, x + width, y - height)  
     mlda(x - width, y, x + width, y)  
     mlda(x + width, y - height, x + width, y + height)  
     mlda(x - width, y - height, x - width, y + height)
 elif num=='9':
     mlda(x - width, y, x + width, y)  
     mlda(x + width, y - height, x + width, y + height)  
     mlda(x - width, y + height, x - width, y)  
     mlda(x - width, y + height, x + width, y + height)
     mlda(x - width, y - height, x + width, y - height) 

def cinc(x,y,r):
     centerX = x
     centerY = y
     radius = r

     mcda(centerX, centerY, radius) 

     mcda(centerX + radius / 2, centerY, radius / 2)  
     mcda(centerX - radius / 2, centerY, radius / 2)  
     mcda(centerX, centerY + radius / 2, radius / 2) 
     mcda(centerX, centerY - radius / 2, radius / 2)  

     crossX = (math.sin(math.radians(45))) * radius / 2
     crossY = crossX

     mcda(centerX + crossX, centerY + crossY, radius / 2)  
     mcda(centerX - crossX, centerY + crossY, radius / 2)  
     mcda(centerX + crossX, centerY - crossY, radius / 2) 
     mcda(centerX - crossX, centerY - crossY, radius / 2)  

def car(centerx):
 glColor3f(0.9, 0.49, 0.494)
 mqdafilledSmall(centerx-17,30,centerx+17,30,centerx+17,100,centerx-17,100)
 glColor3f(0, 0, 0)
 mqdafilledSmall(centerx - 10, 50, centerx + 10, 50, centerx + 10, 80, centerx - 10, 80)

def scoredisplay(b=0):
    glColor3f(.1, .1,.8)

    x, y = 10, 100+350
    for i in range(5):
        mlda(x, y, x+25, y)
        mlda(x+25, y, x + 25, y + 12)
        mlda(x + 25, y + 12, x , y+12)
        mlda(x , y+12, x, y+25)
        mlda(x,y+25,x+25,y+25)
        x += 1
        y += 1

    x, y = 50, 100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x + 25, y, x, y)
        x += 1
        y += 1
 
    x, y = 90, 100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x + 25, y + 25, x + 25, y)
        mlda(x + 25, y, x, y)
        x += 1
        y += 1
    
    x, y = 130,100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x + 25, y + 25, x + 25, y + 12)
        mlda(x, y + 12, x + 25, y + 12)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x, y + 12, x + 25, y)
        x += 1
        y += 1
    
    x, y = 170,100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y, x + 25, y)
        mlda(x, y + 12, x + 25, y + 12)
        mlda(x, y + 25, x + 25, y + 25)
        x += 1
        y += 1

    x,y=210,120+350
    for i in range(5):
        mlda(x,y+i,x+5,y+i)
        mlda(x,y+i-10,x+5,y+i-10)

    x,y=250,115+350
    for i in str(b):
        drawnum(x,y,i,10,10)
        x+=30

