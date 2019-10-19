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

points=[(500,50),(100,50),(100,500),(500,500)]

number_of_points=4
div=2


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
    
    screen=p.display.set_mode((width,height))
    
    while True:
        
        for events in p.event.get():
            if events.type == p.QUIT:

                p.quit()
                
        gfxdraw.pixel(screen, px, py, Color_line)
        p.display.flip()
        
        t=randint(0,number_of_points-1)
        while pt==t:
            t=randint(0,number_of_points-1)
        px=(px+points[t][0])//div
        py=(py+points[t][1])//div
        pt=t
        p.time.Clock().tick(50000)
main()