import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 95))


class Car(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.speed = -10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= -10 or self.rect.right >= 600:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)


all_sprites = pygame.sprite.Group()

car_image_path = os.path.join('data', 'car2.png')
car = Car(car_image_path)
all_sprites.add(car)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill('white')
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
