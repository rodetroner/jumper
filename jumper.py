import pygame, sys

size = width, height = 320, 240

class Jumper(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('jumper.png')
        self.rect = self.image.get_rect()

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.rect.move_ip(x, y)


screen = pygame.display.set_mode(size)
jumper = Jumper(screen)
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    jumper.move(20, 0)
    jumper.blit()
    pygame.display.flip()

pygame.quit()
