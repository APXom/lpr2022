import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (250, 150), 10)
circle(screen, (0, 0, 0), (150, 150), 5)
circle(screen, (0, 0, 0), (250, 150), 5)
polygon(screen, (0, 0, 0), [(175,150), (175,125), (100, 110), (100, 135)])
polygon(screen, (0, 0, 0), [(225,150), (225, 125), (300,110), (300, 135)])
rect(screen, (0, 0, 0), (160, 220, 80, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()