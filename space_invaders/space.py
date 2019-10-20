import pygame as p
from random import randint

p.init()
p.mixer.init()
width=600
height=400
display=p.display.set_mode((width,height))
p.display.set_caption("Space Invaders")
clock = p.time.Clock()
white=(255,255,255)
black=(0,0,0)
font=p.font.SysFont(None, 30)
font_health=p.font.SysFont(None, 25)
display.fill(black)

invader_y=10
invader_x=0

player_x=4 
player_y=360

wallhit=0

score=0

run=True    

# player=p.Surface((15,15))
# player.fill((255,255,255))
player=p.image.load("Spaceship (4).png")

# invader = p.Surface((15,15))
# invader.fill((255,255,255))

list_bullet=[] 

bullet=p.Surface((2,5))
bullet.fill((255,255,255)) 

offsetx=50
offsety=20

invader_list=[]

number_of_invader=8

invader_sprite={1:"InvaderB_00.png",2:"InvaderB_01.png",3:"InvaderC_00.png",4:"InvaderC_01.png"}
inv=randint(1,4)
invader=p.image.load(invader_sprite[inv])

for i in range(number_of_invader):
    invader_list.append([invader_x,invader_y,invader])
    invader_x+=offsetx
    
invader_y=10
invader_x=-2

invadery_position=10

bullet_probability=0

bullet_count=1

invader_bullet_list=[]

def draw_player_healthbar(player_health1):

    player_health=player_health1
    player_life=p.Surface((40*player_health,15))
    player_life.fill((229,218,218,0.1))
    return player_life

def score_board(text,color,x,y):
    score1=font.render(text,True,color)
    display.blit(score1,(x,y))
    
def player_health_percentage(text,color,x,y):
    health=font_health.render(text,True,color)
    display.blit(health,(x,y))
    
player_health=7
original_health=player_health*40
while run:
    
    display.fill(black)
    
#------------------------Invaders respawning after some duration-----------------------------------

    if ((height//2-invadery_position)<=5  and (len(invader_list)+number_of_invader)<=18) or len(invader_list)==0:
        inv=randint(1,4)
        invader=p.image.load(invader_sprite[inv])
        for i in range(number_of_invader):
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
                p.mixer.music.load("ShipBullet.wav")
                p.mixer.music.play()
    
    keys=p.key.get_pressed()
            
    if keys[p.K_LEFT]:
        if player_x>=6:
            player_x-=4
    if keys[p.K_RIGHT]:
        if (player_x+50)<=width: #50 is player width
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
            p.mixer.music.load("InvaderBullet.wav")
            p.mixer.music.play()
            
    for k in invader_bullet_list:
        if k[1]>=height-20 :
            bullet_count=1
            invader_bullet_list.remove(k)
        elif abs(k[1]-player_y)<=5 and k[0]>=player_x and  k[0]<=(player_x+49):
            p.mixer.music.load("ShipHit.wav")
            p.mixer.music.play()
            player_health-=1
            invader_bullet_list.remove(k)
            bullet_count=1
            print("player heal  ",player_health)
            if player_health==0:
                run=False
                print("Game overrr",player_health)
                break
                
        else:
            k[1]+=5
            bullet_count+=1
        display.blit(bullet,(k[0],k[1])) 
    current_health=40*player_health
    text=(current_health*100)//original_health
    player_health_percentage(str(text)+" %", (229,218,218,0.1), 90, 20)
    display.blit(draw_player_healthbar(player_health),(150,20))
    
#---------------------------Draw Invader and remove invader when hit with bullet---------------------#
    
    for i in invader_list:
        if wallhit==0:
            i[0]+=2
            for i_ in list_bullet:
               
                if abs(i_[0]-i[0])<=10 and abs(i_[1]-i[1]<=10):
                    p.mixer.music.load("InvaderHit.wav")
                    p.mixer.music.pause()  
                    list_bullet.remove(i_)
                    invader_list.remove(i)
                    score+=1
                    break
            if i[0]>=width-20:
                for j in invader_list:
                    j[1]+=20
                wallhit=1
            
            if abs(i[0]-player_x)<=15 and abs(i[1]-player_y)<=20:
                player_health-=1
                invader_list.remove(i)
                if player_health==0:
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
                player_health-=1
                invader_list.remove(i)
                if player_health==0:
                    print("game over")
                    run=False
                
        if i[1]>=381:
            invader_list.remove(i)
        else:    
            invadery_position=i[1]
        display.blit(i[2],(i[0],i[1]))
        
        
#------------------------------Display Player Score-----------------------------------------------------------

    if run==False:
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
    score_board(text, (169 ,220 ,223), 20, 350)
    try:
        with open("highScore.txt","r+") as file:
            content=file.read()
        text="High Score : "+content
    except:
        file = open("highScore.txt", "w") 
        file.write("0") 
        file.close() 
        text="High Score : 0"
        
    score_board(text, (169 ,220 ,223), 410, 350)
    print(len(invader_list))
    p.display.flip()
    clock.tick(60)

            
    
