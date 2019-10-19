import pygame as p
from random import randint

p.init()
display=p.display.set_mode((400,400))
p.display.set_caption("Space Invaders")
clock = p.time.Clock()
white=(255,255,255)
black=(0,0,0)
font=p.font.SysFont(None, 30)
display.fill(black)

invader_y=10
invader_x=0

player_x=4 
player_y=380

wallhit=0

score=0

run=True    

# player=p.Surface((15,15))
# player.fill((255,255,255))
player=p.image.load("Ship.png")

# invader = p.Surface((15,15))
# invader.fill((255,255,255))

list_bullet=[] 

bullet=p.Surface((2,5))
bullet.fill((255,255,255)) 

offsetx=50
offsety=20

invader_list=[]

invader_sprite={1:"InvaderB_00.png",2:"InvaderB_01.png",3:"InvaderC_00.png",4:"InvaderC_01.png"}
inv=randint(1,4)
invader=p.image.load(invader_sprite[inv])

for i in range(6):
    invader_list.append([invader_x,invader_y,invader])
    invader_x+=offsetx
    
invader_y=10
invader_x=-2

invadery_position=10

bullet_probability=1

bullet_count=1

invader_bullet_list=[]


def score_board(text,color,x,y):
    score1=font.render(text,True,color)
    display.blit(score1,(x,y))

while run:
    
    display.fill(black)
    
#------------------------Invaders respawning after some duration-----------------------------------

    if ((400//2-invadery_position)<=5  and (len(invader_list)+6)<=18) or len(invader_list)==0:
        inv=randint(1,4)
        invader=p.image.load(invader_sprite[inv])
        for i in range(6):
            invader_list.append([invader_x,invader_y,invader])
            invader_x+=offsetx
        invader_y=10
        invader_x=-2
        invadery_position=0
        
        
    for event in p.event.get(eventtype=None):
        if event.type==p.QUIT:
            run=False
            
        if event.type==p.KEYDOWN:
            if event.key==32:
                list_bullet.append([player_x+5,player_y])
    
    keys=p.key.get_pressed()
            
    if keys[p.K_LEFT]:
        if player_x>=6:
            player_x-=4
    if keys[p.K_RIGHT]:
        if player_x<=365:
            player_x+=4
        
#     if keys[p.K_SPACE]:
#         list_bullet.append([player_x+10,player_y])

#------------------------------Player Bullets-----------------------------------------------------------------------------------
        
    if len(list_bullet)>=1:
        for i in list_bullet:
            if i[1]<=10:
                list_bullet.remove(i)              
            else:
                i[1]-=20
            display.blit(bullet,(i[0],i[1]))        
    
    display.blit(player,(player_x,player_y))
    
#---------------------------------------Invader Bullets-------------------------------------------------
    
    if len(invader_list)>0 and bullet_count<=bullet_probability:
        
        for k in range(bullet_probability):
            b=randint(0,len(invader_list)-1)
            print(b,len(invader_list))
            bx=invader_list[b][0]
            by=invader_list[b][1]
            invader_bullet_list.append([bx,by])
            
    for k in invader_bullet_list:
        if k[1]>=390 :
            bullet_count=1
            invader_bullet_list.remove(k)
        elif (abs(k[1]-player_y)<=10 and abs(k[0]-player_x)<=10):
            run=False
            print("Game overrr")
            break
        else:
            k[1]+=5
            bullet_count+=1
        display.blit(bullet,(k[0],k[1])) 
    
#---------------------------Draw Invader and remove invader when hit with bullet---------------------#
    
    for i in invader_list:
        if wallhit==0:
            i[0]+=2
            for i_ in list_bullet:
               
                if abs(i_[0]-i[0])<=10 and abs(i_[1]-i[1]<=10):   
                    list_bullet.remove(i_)
                    invader_list.remove(i)
                    score+=1
                    break
            if i[0]>=380:
                for j in invader_list:
                    j[1]+=20
                wallhit=1
            
            if abs(i[0]-player_x)<=15 and abs(i[1]-player_y)<=20:
                print("game over")
                run=False
                
        elif wallhit==1:
            i[0]-=2
            for i_ in list_bullet:
                
                if abs(i_[0]-i[0])<=10 and abs(i_[1]-i[1]<=10):
                    list_bullet.remove(i_)
                    invader_list.remove(i)
                    score+=1
                    break
            if i[0]<=-2:
                for j in invader_list:
                    j[1]+=20
                wallhit=0
                
            if abs(i[0]-player_x)<=15 and abs(i[1]-player_y)<=20:
                print("game over")
                run=False
                
        if i[1]>=381:
            invader_list.remove(i)
        else:    
            invadery_position=i[1]
        display.blit(i[2],(i[0],i[1]))
        
        
#------------------------------Display Player Score-----------------------------------------------------------

    if run==False:
        print("falseeeeeee")
        try:
            with open("highScore.txt","r+") as file:
                content=file.read()
                file.seek(0)
                if score>int(content):
                    file.write(str(score))
                    file.truncate()
        except:
            file = open("highScore.txt", "w") 
            file.write("0") 
            file.close() 

    text="Current Score : "+str(score)
    score_board(text, (169 ,220 ,223), 100, 350)
    try:
        with open("highScore.txt","r+") as file:
            content=file.read()
        text="High Score : "+content
    except:
        file = open("highScore.txt", "w") 
        file.write("0") 
        file.close() 
        text="High Score : 0"
        
    score_board(text, (169 ,220 ,223), 100, 20)
    print(len(invader_list))
    p.display.flip()
    clock.tick(60)

            
    