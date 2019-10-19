import pygame as p
import random

p.init()
p.mixer.init()
display=p.display.set_mode((300,400))
clock = p.time.Clock()
white=(255,255,255)
pipe_green=(61,175,80)
almost_white=(73,107,66)
display.fill(white)
font=p.font.SysFont(None, 30)
score=0

background_image = p.image.load("flappy.png")
bird_img = p.image.load("bird.png")

bird_x=10
bird_y=100

run=True
offset=120
pipe_lengthup=random.randint(3,21)
pipe_yd=pipe_lengthup*10+offset

pipe_yup=0
pipe_xup=100

u=450
d=450

pipe_xd=100
pipe_lengthlow=400

bird = p.Surface((10, 10))
bird.fill((255, 0, 0))

pipe_length_list=[]
for i in range(0,3):
    pipe_lengthup=random.randint(3,20)
    pipe_lengthlow=400
    pipe_length_list.append((pipe_lengthup*10,pipe_lengthlow,))
pipe_list=[]
for x,y in pipe_length_list:
    
    pipeup = p.Surface((20, x))
    pipeup.fill(pipe_green)
    
    piped = p.Surface((20, y))
    piped.fill(pipe_green)
    pipe_list.append((pipeup,piped,x+offset))
    
    
    
def score_board(text,color,x,y):
    score1=font.render(text,True,color)
    display.blit(score1,(x,y))
            
    
while run:
    
    for event in p.event.get(eventtype=None):
        if event.type==p.QUIT:
            run=False
    
    if u<=-280 and d<=--280:
        pipe_length_list=[]
        for i in range(0,3):
            pipe_lengthup=random.randint(3,20)
            pipe_lengthlow=400
            pipe_length_list.append((pipe_lengthup*10,pipe_lengthlow))
        pipe_list=[]
        for x,y in pipe_length_list:
             
            pipeup = p.Surface((20, x))
            pipeup.fill(pipe_green)
             
            piped = p.Surface((20, y))
            piped.fill(pipe_green)
            pipe_list.append((pipeup,piped,x+offset))
        u=450
        d=450
        
            
    keys=p.key.get_pressed()
    if keys[p.K_SPACE]:
        p.mixer.music.load("sfx_wing.wav")
        p.mixer.music.play()
        bird_y-=25
        
        
    display.blit(background_image, [0, 0])
    display.blit(bird,(20,bird_y))
    count=0
    pipe_xd=d
    pipe_yup=0
    pipe_xup=u
    for x,y,a in pipe_list:
        
        display.blit(x,(pipe_xup ,0))
        display.blit (y,(pipe_xd ,a))
        pipe_xd+=130 
        pipe_xup+=130
        
        if (((u+count*130)-bird_x)<=10 and (u+count*130)-bird_x >=0) and (bird_y-10<=(a-offset)) or ((((u+count*130)-bird_x)<=10 and (u+count*130)-bird_x >=0) and bird_y+10>=a):
                p.mixer.music.load("sfx_hit.wav")
                p.mixer.music.play()
                run=False 
                print((u+count*130)-bird_x,bird_y,a-offset,a,u,count*130)
                
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
                    text="High Score : 0"
                
        if bird_x-(u+count*130)==-20:
            score+=1
                     
#         elif (u+count*130)-bird_x==0 and bird_y+10>=a:
#             p.mixer.music.load("sfx_hit.wav")
#             p.mixer.music.play()
#             run=False
#             print("down",(u+count*130)-bird_x,bird_y,a,u,count*130)
              
        #print("downnnnnn",(u+count*130)-bird_x,bird_y,a,u,count*130,score)
        count+=1
        
    bird_y+=10    
    pipe_xd=d
    pipe_yup=0
    pipe_xup=u
    
    text="Current Score : "+str(score)
    score_board(text, (99 ,50 ,88), 50, 350)
    try:
        with open("highScore.txt","r+") as file:
            content=file.read()
        text="High Score : "+content
    except:
        file = open("highScore.txt", "w") 
        file.write("0") 
        file.close() 
        text="High Score : 0"
        
    score_board(text, (99 ,50 ,88), 50, 20)
    
    p.display.update()
    u-=5
    d-=5
    clock.tick(20)
    