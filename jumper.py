import sys, pygame
pygame.init()

size = width, height = 320, 240

screen = pygame.display.set_mode(size)

class Jumper(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('jumper.png')
        self.rect = self.image.get_rect()

    def blit(self):
        self.screen.blit(self.image, self.rect)

jumper = Jumper(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        jumper.blit()

        pygame.display.flip()
