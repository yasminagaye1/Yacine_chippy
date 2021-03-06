import pygame
import random
import os

pygame.init()

display_width = 535
display_height = 540

box_width = 50
box_height = 50
margin = 3
locations = []
black = (0,0,0)
white = (255,255,255)
darkgreen = (0,80,0)
green = (0,100,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
goo_image = pygame.image.load('1600.png')
goo_image = pygame.transform.scale( goo_image , (45,50))
reward_image = pygame.image.load('Acorn_Body.png')
reward_image = pygame.transform.scale(reward_image, (45,50))
chippyImg = pygame.image.load('unnamed.png')
chippyImg = pygame.transform.scale( chippyImg, (45,50))
for row in range (10):
    for column in range (10):
        locations.append((margin + row * 53 ,margin + column * 53))
def goo(x,y):
    gameDisplay.blit(goo_image, (x,y) )
def chippy(x,y):
    gameDisplay.blit(chippyImg, (x,y) )
def reward(x,y):
    gameDisplay.blit(reward_image, (x,y) )
def game_loop():
    reward_loc = locations[random.randint(0,100)]
    chippy_loc = locations[random.randint(0,100)]
    goo_loc = locations[random.randint(0,100)]
    x = chippy_loc[0]
    y = chippy_loc[1]
    x_change = 0
    y_change = 0
    delay = 150
    pygame.display.set_caption('Chippy on a Grid')
    clock = pygame.time.Clock()
    playon = True
    while playon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playon = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 3:
                    x_change = -53
                    pygame.time.wait(delay)
                elif event.key == pygame.K_RIGHT and x < 480:
                    x_change = 53
                    pygame.time.wait(delay)
                elif event.key == pygame.K_UP and y > 3:
                    y_change = -53
                    pygame.time.wait(delay)
                elif event.key == pygame.K_DOWN and y < 480:
                    y_change = 53
                    pygame.time.wait(delay)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0;
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        filenames = next(os.walk("Users/chrisbanks/Desktop/WORKFILES/chippy"))[2]
        for file in filenames:
            directory = open(file,"r")
            if directory.read() is 0 and y > 3:
                y_change = -53
                pygame.time.wait(delay)
            elif directory.read() is 1 and y < 480:
                y_change = 53
                pygame.time.wait(delay)
            elif directory.read() is 2 and x > 3:
                x_change = -53
                pygame.time.wait(delay)
            elif directory.read() is 3 and x < 480:
                x_change = 53
                pygame.time.wait(delay)
        x += x_change
        y += y_change
        gameDisplay.fill(darkgreen)
        for row in range(10):
            for column in range(10):
                color = green
                pygame.draw.rect(gameDisplay, color, [(margin + box_width) * column + margin,
                                                      (margin + box_height) * row + margin,
                                                      box_width, box_height])
        chippy(x,y)
        goo(goo_loc[0], goo_loc[1])
        reward(reward_loc[0],reward_loc[1])
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()

