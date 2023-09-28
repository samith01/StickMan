import numpy as np
import pygame
import random
import pandas as pd
import time


pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
brown = (150, 75, 0)
red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((800, 533))

font = pygame.font.Font('font.otf', 30)

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("background.jpg")

    def render(self):
        if self.x < 0:
            if self.x + 800 <= 0:
                self.x = 0
                screen.blit(self.image, (self.x, self.y))
            else:
                screen.blit(self.image, (self.x+800, self.y))
                screen.blit(self.image, (self.x, self.y))
            
        else:
            screen.blit(self.image, (self.x, self.y))
    
    def update(self,speed):
        self.x -= speed

class StickMan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.states = []
        self.state = 0

        for i in range(1,6):
            filename = 'Stickman/frame'+ str(i) + '.png'
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image,(150,150))
            self.states.append(image)

        self.image = self.states[self.state]

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.state += 1
        if self.state == 5:
            self.state = 0
        self.image = self.states[self.state]

    def jump(self, bg,block1):
  
        for i in range(100):
            self.y -= 1
            bg.render()
            bg.update(0.8)
            block1.update(bg,0.8)

            screen.blit(self.states[3], (self.x, self.y))
            pygame.display.flip()
            time.sleep(0.001)

        for i in range(100):
            self.y += 1
            # self.update()
            bg.render()
            bg.update(0.8)
            block1.update(bg,0.8)

            screen.blit(self.states[3], (self.x, self.y))


            pygame.display.update()

            time.sleep(0.001)
            

class Obstacles(pygame.sprite.Sprite):
    def __init__(self,color):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(800,1600)
        self.color = color
    
    def render(self):
        pygame.draw.rect(screen,(0,0,0),(self.x,360,70,100))
        if self.x <= 0:
            self.x = random.randint(800,1600)

    def update(self,bg,speed):
       bg.render()
       self.x -= speed
       pygame.draw.rect(screen,(0,0,0),(self.x,390,30,70))

def game_open():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stickman.jump(bg,block1)

    return True


bg = Background(0,0)
stickman = StickMan(100,335)

block1 = Obstacles((255,255,0))
block2 = Obstacles((0,225,0))


while game_open():

    bg.render() 
    bg.update(10)

    block1.render()
    block1.update(bg,10)
    # block2.render()
    # block2.update(bg,10)

    stickman.render()
    stickman.update()

    time.sleep(0.05)
    pygame.display.update()
