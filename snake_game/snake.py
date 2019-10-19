import pygame as p
from random import randint

p.init()
p.mixer.init()
display = p.display.set_mode((400,400))
p.display.set_caption("Snake")
font=p.font.SysFont(None, 30)
font_gameover=p.font.SysFont(None,30)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
display.fill(white)
run=True
clock = p.time.Clock()
snake_x=10
snake_y=50
gameover=False
size=15
lensnk=size
snake_width=size
snake_height=size
velocity=size

food_x=0
food_y=0
food_width=size
food_height=size
food=False
direction="right"
snk=[]
count=0
home_Screen=True
def draw_snake(food1,snk,lensnk):
    global food_x,food_y,food_width,food_height,food,snake_x,snake_y
    display.fill(white) 
    
    if food1==False:
        food_x=randint(1,37)
        food_y=randint(1,37)
        food=True
        
    p.draw.rect(display, (255,0,0), (food_x*10,food_y*10,food_width,food_height)) 
    
    if len(snk)*10 > lensnk:
        snk.pop(0) 
        
    for x,y in snk:
        p.draw.rect(display, black, (x, y,snake_width,snake_height))
    snake_x=snake_x%400
    snake_y=snake_y%400
    text="Current Score : "+str(count)
    score_board(text, (15 ,157 ,88), 10, 10)
    try:
        with open("highScore.txt","r+") as file:
            content=file.read()
        text="High Score : "+content
    except:
        file = open("highScore.txt", "w") 
        file.write("0") 
        file.close() 
        text="High Score : 0"
    score_board(text, (15 ,157 ,88), 210, 10)
    p.display.update()
    

def score_board(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))
    
def game_over(text,color,x,y):
    score=font_gameover.render(text,True,color)
    display.blit(score,(x,y))


def game_loop():
    global run,count,snk,lensnk ,gameover,food,direction,velocity,snake_x,snake_y,home_Screen
    snk=[]
    direction="right"
    snake_x=10
    snake_y=50
    lensnk=10
    count=0
    fps=15
    print(home_Screen)
    while run:
        
        
    
        if home_Screen:
            display.fill(white)
            game_over("Press space to start the game", (15 ,157 ,88), 70, 200)
            p.display.update()
            for event in p.event.get():
                if event.type==p.QUIT:
                    home_Screen=False
                    run=False
                if event.type==p.KEYDOWN:
                    if event.key==32:
                        home_Screen=False
                        game_loop()

        
        elif gameover:
            display.fill(white)
            text="Game Over"
            text2="Press enter to play again"
            game_over(text, (15 ,157 ,88), 140, 150)
            game_over(text2, (15 ,157 ,88), 70, 200)
            p.display.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    run=False
                if event.type==p.KEYDOWN:
                    print(event.key,p.KEYDOWN)
                    if event.key==13:
                        gameover=False
                        home_Screen=True
        else:
            
            for event in p.event.get():
                if event.type == p.QUIT:
                    run=False
                    
            draw_snake(food,snk,lensnk)
            keys=p.key.get_pressed()
            
            if keys[p.K_LEFT]:
                direction="left"
            elif keys[p.K_RIGHT]:
                direction="right"
            elif keys[p.K_UP]:
                direction="up"
            elif keys[p.K_DOWN]:
                direction="down"
            
               
            if direction=="left":
                snake_x-=velocity
                draw_snake(food,snk,lensnk)
                        
            if direction=="right":
                snake_x+=velocity
                draw_snake(food,snk,lensnk)
            
            if direction=="up" :
                snake_y-=velocity
                draw_snake(food,snk,lensnk)
                
            if direction=="down":
                snake_y+=velocity
                draw_snake(food,snk,lensnk)
                
            if (abs(snake_x-food_x*10)<7)  and (abs(snake_y-food_y*10)<7):
                lensnk+=size
                food=False
                count+=10
                p.mixer.music.load("eat.wav")
                p.mixer.music.play()
                if count==50 or count==100 or count==200 or count==250:
                    fps+=5
                
            snake_x_y=[]
            snake_x_y.append(snake_x)
            snake_x_y.append(snake_y)
            
            if snake_x_y in snk:
                p.mixer.music.load("gameover.wav")
                p.mixer.music.play()
                p.time.delay(1000)
                try:
                    with open("highScore.txt","r+") as file:
                        content=file.read()
                        file.seek(0)
                        if count>int(content):
                            file.write(str(count))
                            file.truncate()
                    p.display.update()
                except:
                    pass
                gameover=True
            snk.append(snake_x_y)
            clock.tick(fps)
    
game_loop()
