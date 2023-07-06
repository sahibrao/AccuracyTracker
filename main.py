import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 500
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BACKGROUND_COLOR = (0, 25, 40)

class Target: 
    MAXIMUM_SIZE = 25
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAXIMUM_SIZE:
            self.grow = False
        
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size*0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size*0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size*0.4)

def drawMain(win, targets):
    win.fill(BACKGROUND_COLOR)

    for target in targets:
        target.draw(win)

    pygame.display.update()

def main():
    run = True
    targets = []

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)
        
        for target in targets:
            target.update()


        draw(WIN, targets)
        
    pygame.quit()

if __name__ == "__main__":
    main()