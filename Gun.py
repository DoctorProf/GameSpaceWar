import pygame

class Gun():

    def __init__ (self, screen):
        self.screen = screen
        self.image = pygame.image.load("image/Gun.png")
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        self.mright = False
        self.mleft = False


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def updateGun(self):
        if self.mright and self.rect.right < self.screenRect.right:
            self.rect.centerx +=1
        if self.mleft and self.rect.left > self.screenRect.left:
            self.rect.centerx -=1