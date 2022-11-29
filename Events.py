import pygame, sys
from bullet import Bullet
from inoplanet import Ino
import time
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
                bullets.add(newBullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bgColor, screen, gun, inos,  bullets):
    screen.fill(bgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.draw()
    inos.draw(screen)
    pygame.display.update()

def updateBullets(screen, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if len(inos) == 0:
        bullets.empty()
        createArmy(screen, inos)
def gunKill(stats, screen, gun, inos, bullets):  

    stats.gunsLive-=1
    inos.empty()
    bullets.empty()
    createArmy(screen, inos)
    gun.spawnGun()
    time.sleep(1)

def updateInos(stats, screen, gun, inos, bullets):

    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gunKill(stats, screen, gun, inos, bullets)
    inosCheck(stats, screen, gun, inos, bullets)

def inosCheck(stats, screen, gun, inos, bullets):

    screenRect = screen.get_rect()
    
    for ino in inos.sprites():
        if ino.rect.bottom >= screenRect.bottom:
            gunKill(stats, screen, gun, inos, bullets)
            break

def createArmy(screen, inos):

    ino = Ino(screen)
    inoWidth = ino.rect.width
    NumInoX = int((700 - 2 * inoWidth) / inoWidth)
    inoHeight = ino.rect.height
    NumInoY = int((800 - 100 - 2 * inoHeight) / inoHeight)

    for rowNum in range (NumInoY - 6):
        for inoNum in range(NumInoX - 6 ):
            ino = Ino(screen)
            ino.x = inoWidth + (1.8 * inoWidth * inoNum)
            ino.y = inoHeight + (inoHeight * rowNum)
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)