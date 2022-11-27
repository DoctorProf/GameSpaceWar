import pygame, sys
from bullet import Bullet

def event(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                newBullet = Bullet(screen, gun)
                bullets.add()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bgColor, screen, gun, bullets):
    screen.fill(bgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.draw()
    pygame.display.update()