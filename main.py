from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time
import numpy as np

gameoverposition=1000 # ei variable diye game over lekhar position control hobe. car crash korle etar value 0 hoye jabe ar game over lekha show korbe
slowness=.08
crash=False # For detecting car crashed or not
middleline_y=300 # ei variable diyei road er midlle line gula control hobe. Basically eta middle line er bottom point.
centerx=247 # center of car
#Round object parameters
objx=[] # object gular center x
objy=[600,750,750,900,1050,1050,1200,1200,1500,1650,1650,1800]
objradius=[]


for x in range(12): # randomly object er lane assign kortesi. Apatoto 12 ta object nicchi at a time.
     objx.append(random.choice([247-65,247,247+65]))
     objradius.append(12) #initial radius 12 set kortesi
# Square object paramater
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

#for drawing circle objects
def objcirc():
 global objy
 global objx
 global objradius

 i=0
 for x in range(len(objx)):
     cinc(objx[i], objy[i], objradius[i])
     i+=1

#For drawing square object
def objsquare():
 global x1,y1,x2,y2,x3,y3,x4,y4
 mqda(x1,y1,x2,y2,x3,y3,x4,y4)

#square er point gula ke given degree angle e rotate kore dibe
def rotatedeg(degree): # quad er 4 ta point ke given degree angle e rotate kore dibe
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

#For Drawing middle lines of the road
def middlelines(y): # y er moddhe middleline_y pass hocche.
# proti column e middleilne_y er sapekkhe 3 ta line separet line thakbe.
 glColor3f(1, 1, 1)
 mldamedium(215, y, 215, y+200)
 mldamedium(215, y-100, 215, y-300 )
 mldamedium(215, y+300, 215, y+500)
 mldamedium(280, y, 280, y + 200)
 mldamedium(280, y - 100, 280, y - 300)
 mldamedium(280, y + 300, 280, y + 500)

#Drawing point 2
def draw_points(x, y):
 glPointSize(2) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#Drawing point 10
def draw_pointsmedium(x, y):
 glPointSize(10) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#Drawing point 30
def draw_pointsbig(x, y):
 glPointSize(30) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#MLDA (Line) 2
def FindZoneAndCvtTo0(x1,y1,x2,y2): #Algoritm=> diff>0 hole x,y swap. ar x,y er modhe je je  negative tader -1 diye multiply
 res=[] # x1,y1,x2,y2,zone eita return korbe
 dx = x2 - x1
 dy = y2 - y1
 diff=abs(dx)-abs(dy)
 if diff>=0: #No Swap
     if (dx>=0): #dx positive
         #Zone 0
         if dy>=0: #dy positive
             res.append(x1)
             res.append(y1)
             res.append(x2)
             res.append(y2)
             res.append(0)
         # Zone 7
         else: #dy negative
             res.append(x1)
             res.append(y1*(-1))
             res.append(x2)
             res.append(y2*(-1))
             res.append(7)
     else: #dx negative
         # Zone 3
         if dy >= 0:  # dy positive
             res.append(x1*(-1))
             res.append(y1)
             res.append(x2*(-1))
             res.append(y2)
             res.append(3)
         # Zone 4
         else:  # dy negative
             res.append(x1*(-1))
             res.append(y1*(-1))
             res.append(x2*(-1))
             res.append(y2*(-1))
             res.append(4)
 else: #diff<0 #Swap lagbe
     if (dx >= 0):  # dx positive
         # Zone 1
         if dy >= 0:  # dy positive
             res.append(y1)
             res.append(x1)
             res.append(y2)
             res.append(x2)
             res.append(1)
         # Zone 6
         else:  # dy negative
             res.append(y1*(-1))
             res.append(x1)
             res.append(y2*(-1))
             res.append(x2)
             res.append(6)
     else:  # dx negative
         # Zone 2
         if dy >= 0:  # dy positive
             res.append(y1)
             res.append(x1*(-1))
             res.append(y2)
             res.append(x2*(-1))
             res.append(2)
        # Zone 5
         else:  # dy negative
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
 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 #Applying Mlda
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
     #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_points(tp[0],tp[1])
     #Updating pixel
     if(d>0):#choose NE
         x+=1
         y+=1
         d=d+dNE  #updating d
     else: # choose E
         x+=1
         d=d+dE # updating d

#MLDA (Line) 10
def mldamedium(x1,y1,x2,y2):
 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 #Applying Mlda
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
    #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsmedium(tp[0],tp[1])
     #Updating pixel
     if(d>0):#choose NE
         x+=1
         y+=1
         d=d+dNE  #updating d
     else: # choose E
         x+=1
         d=d+dE # updating d
#MLDA (Line) 30
def mldabig(x1,y1,x2,y2):
 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)
 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]
 #Applying Mlda
 dx=x2-x1
 dy=y2-y1
 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx
 d=dint
 x=x1
 y=y1
 while(x<x2):
     #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsbig(tp[0],tp[1])
 #Updating pixel
     if(d>0):#choose NE
         x+=1
         y+=1
         d=d+dNE  #updating d
     else: # choose E
         x+=1
         d=d+dE # updating d

#MCDA (Circle)
def mcda(centerX,centerY,r):
 #print(centerX)
 d=1-r # d initialize

 # initially x =0 ar y =radius
 x=0
 y=r
 while(y>=x): # jotokhon zone 1 e thakbe
     draw_circle_points(x,y,centerX,centerY) #point ta sob zone e draw korbe.
   #Updating pixel
     if(d>=0):#choose SE
         d=d+2*x-2*y+5
         x += 1
         y -= 1
     else: # choose E
         d=d+2*x+3
         x += 1
def draw_circle_points(x,y,centerX,centerY):
 for i in range(8): # i mean zone 0 to 7

     temp=Cvt1ToX(x,y,i) #i th zone er jonno 8 way sym diye point ber kore temp e store kortesi. temp[0]=>x ,temp[1]=>y
     draw_points(temp[0]+centerX,temp[1]+centerY) # point er sathe center jog kore draw kore dicchi.
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
 else: # zone==7:
     res.append(y)
     res.append(x*(-1))
 return res
#MQDA (Quad)
def mqda(x1,y1,x2,y2,x3,y3,x4,y4):
 mldamedium(x1,y1,x2,y2)
 mldamedium(x2, y2, x3, y3)
 mldamedium(x3, y3, x4, y4)
 mldamedium(x4, y4, x1, y1)

#MQDA filled (filled Quad)
def mqdafilled(x1,y1,x2,y2,x3,y3,x4,y4):
 # mlda(x1,y1,x2,y2)
 # mlda(x2, y2, x3, y3)
 # mlda(x3, y3, x4, y4)
 # mlda(x4, y4, x1, y1)
 for x in range(x1,x2+1,25): #optimize er jonno skip kortesi.
     mldabig(x,y1,x,y4)
 # for y in range(y1,y4+1):
 #     mlda(x1,y,x2,y)

#MQDA filled (filled Quad)
def mqdafilledSmall(x1,y1,x2,y2,x3,y3,x4,y4):
 # mlda(x1,y1,x2,y2)
 # mlda(x2, y2, x3, y3)
 # mlda(x3, y3, x4, y4)
 # mlda(x4, y4, x1, y1)

 for x in range(x1,x2+1): #optimize er jonno skip kortesi.
     mlda(x,y1,x,y4)

 # for y in range(y1,y4+1): #eta use korle slow hoye jay. so alternatively drawpoint er size baraye diyechi.
 #     mlda(x1,y,x2,y)
