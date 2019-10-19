import pygame as p
from pygame import gfxdraw
from random import randint

width=600
height=600
x=200
y=50
a=200
b=200
count=0

points=[(600,200),(300,0),(0,200),(150,600),(450,600)]

number_of_points=5
div=3


# for i in range(0,number_of_points):
#     ax=randint(0,width)
#     ay=randint(0,height)
#     points.append((ax,ay))

dx=randint(0,width)
dy=randint(0,height)

px=dx
py=dy
pt=0
def main():
    global count,px,py,number_of_points,div,pt
    Color_line=(randint(0,255),randint(0,255),randint(0,255))
    vertex=[]
    cnt=0
    screen=p.display.set_mode((width,height))
    p.display.set_caption("pentagon")
    while True:
        
        for events in p.event.get():
            if events.type == p.QUIT:

                p.quit()
                
        gfxdraw.pixel(screen, px, py, Color_line)
        p.display.flip()
        
        t=randint(0,number_of_points-1)
#         while pt==t:
#             t=randint(0,number_of_points-1)
#         px=(px+points[t][0])//div
#         py=(py+points[t][1])//div
#         pt=t
#         p.time.Clock().tick(50000)
        
        #---------------------------------PATTERN 2(Little complex)------------------------------------------------------
        if len(vertex)==0:
            vertex.append(t)
            cnt+=1
        if len(vertex)==1:
            vertex.append(t)
            cnt+=1
        if len(vertex)>=2 and vertex[0]==vertex[1]:
             
            while abs(pt-t)==1 or abs(pt-t)==4:
                t=randint(0,number_of_points-1)
            vertex.pop(0)
            vertex.append(t)
        elif cnt==2:
            vertex.pop(0)
            vertex.append(t)
        px=(px+points[t][0])//div
        py=(py+points[t][1])//div
        pt=t
        p.time.Clock().tick(500000)
main()