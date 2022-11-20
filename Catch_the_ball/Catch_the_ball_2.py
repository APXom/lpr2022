import pygame
from pygame.draw import *
from random import randint, choice
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

def new_ball(x, y, r):
    '''рисует новый шарик '''
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)



#def click(event):
#    return pygame.mouse.get_pos()[1] pygame.mouse.get_pos()[1]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        X = []
        Y = []
        R = []
        Vx = []
        Vy = []
        k = randint(1, 5)
        for i in range(k-1):
            X.append(randint(100, 1100))
            Y.append(randint(100, 900))
            R.append(randint(10, 100))
            Vx.append(randint(100, 1100))
            Vy.append(randint(100, 900))
        for j in range(k-1):
            new_ball(X[j], Y[j], R[j])
            '''
        for j in range(k-1):
            if (X[j] + R[j] + Vx[j] >= 1200) or (X[j] - R[j] + Vx[j] <= 0):
                Vx[j] = -Vx[j]
            if (Y[j] + R[j] + Vy[j] >= 700) or (Y[j] - R[j] + Vy[j] <= 0):
                Vy[j] = -Vy[j]
            X[j] += Vx[j]
            Y[j] += Vy[j]'''
        #rect(screen, choice(COLORS), (X[k], Y[k], R[k], R[k]))
        '''if (X[k] + R[k] + Vx[k] >= 1200) or (X[k] + Vx[k] <= 0):
            Vy[k] = Vy[k]*choice([-1, 1])
            Vx[k] = -Vx[k]
        if (Y[k] + R[k] + Vy[k] >= 700) or (Y[k] + Vy[k] <= 0):
            Vx[k] = Vx[k]*choice([-1, 1])
            Vy[k] = -Vy[k]
        X[k] += Vx[k]
        Y[k] += Vy[k]'''
        pygame.display.update()
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        '''
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            pos = list(pygame.mouse.get_pos())
            #print(pos)
            #circlepos = list(click(event))
            #print(click(event))
            for i in range(k - 1):
                print('Дошло')
                print(pos[0], X[i], pos[1], Y[i], R[i])
                print(((pos[0] - X[i]) ** 2 + (pos[1] - Y[i]) ** 2) <= R[i] ** 2)
                if ((pos[0] - X[i]) ** 2 + (pos[1] - Y[i]) ** 2) <= R[i] ** 2:
                    print('Дошло')
                    count += 1
                    print("Есть пробитие!")
                    print("Ваш счет:", count)
                    break
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()