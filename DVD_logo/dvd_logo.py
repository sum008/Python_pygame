import pygame as p
import random
from pygame import gfxdraw

p.init()
p.mixer.init()
display=p.display.set_mode((800,600))
p.display.set_caption("DVD")

black=(0,0,0)
white=(255,255,255)

run=True
x=[1,739]
dx=random.choice(x)
dy=random.randint(0,549)


def logo_():

    logo=p.Surface((60,50))
    logo.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    return logo

def runn():
    run_=True
    for event in p.event.get():
        if event.type == p.QUIT:
            run_=False
            
    return run_

fps=180
px=0
py=0
while run:
    
#-------------------------------------------------------------------------------------------------------------------------------------------            
    if dx==1 and (dy-py)>0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=739 and dy!=549:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx+=1
            dy+=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dx==1 and (dy-py)<0:
        
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=739 and dy!=1:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx+=1
            dy-=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dx==739 and (dy-py)>0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=1 and dy!=549:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx-=1
            dy+=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dx==739 and (dy-py)<0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=1 and dy!=1:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx-=1
            dy-=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
            
    if dy==549 and (dx-px)>0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=739 and dy!=1:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx+=1
            dy-=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dy==549 and (dx-px)<0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=1 and dy!=1:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx-=1
            dy-=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dy==1 and (dx-px)>0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=739 and dy!=549:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx+=1
            dy+=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
            
    if dy==1 and (dx-px)<0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        logo=logo_()
        while dx!=1 and dy!=549:
            run=runn()
            if run==False:
                break
            px=dx
            py=dy
            display.fill(black)
            dx-=1
            dy+=1
            display.blit(logo,(dx,dy))
            p.display.flip()
            p.time.Clock().tick(fps)
#             print(dx,dy,px,py)
#     p.time.Clock().tick(fps)
#             p.display.flip()