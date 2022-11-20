import pygame
from pygame.draw import *
from random import randint
pygame.init()
count = 0
FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    return x, y, r

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            pos = list(pygame.mouse.get_pos())
            #print(pos)
            circlepos = list(click(event))
            #print(click(event))
            if ((pos[0] - circlepos[0]) ** 2 + (pos[1] - circlepos[1]) ** 2) <= circlepos[2] ** 2:
                count += 1
                print("Есть пробитие!")
                print("Ваш счет:", count)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()