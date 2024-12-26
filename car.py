import pygame
import os
import sys

pygame.init()
screen = pygame.display.set_mode((600, 95))

car = pygame.image.load(os.path.join('data', 'car2.png'))
car = pygame.transform.flip(car, True, False)

x = 0
speed = -10

while True:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x >= 450 or x <= 0:
        speed = -speed
        car = pygame.transform.flip(car, True, False)

    x += speed

    screen.fill('white')
    screen.blit(car, (x, 0))
    pygame.display.flip()
