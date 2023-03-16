# pip install pygame

import pygame

pygame.init()
width = 500; height = 500

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('게임 만들기')
icon = pygame.image.load('part1/pyGame/game.png')
pygame.display.set_icon(icon)

x, y = 250, 250
radius = 10
vel = 10
run = True 
jump = False
vel_y = 1


while run:
    win.fill((0,0,0))
    pygame.draw.circle(win, (255, 255, 255), (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 10:
        x -= vel 
    if userInput[pygame.K_RIGHT] and x < width -10:
        x += vel 
    if userInput[pygame.K_UP] and y > 10:
        y -= vel 
    if userInput[pygame.K_DOWN] and y < height -10:
        y += vel
    
    if jump == False and userInput[pygame.K_SPACE]:
        jump = True 
    if jump == True:
        y -= vel_y 
        vel_y -= 1
        if vel_y < -10:
            jump = False 
            vel_y = 10

    pygame.time.delay(10)
    pygame.display.update()