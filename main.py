import pygame, Events
from Gun import Gun
from pygame.sprite import Group
def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('SpaceWar')
    bgColor = (0,0,0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        Events.event(screen, gun, bullets)
        gun.updateGun()
        bullets.update()
        Events.update(bgColor, screen, gun, bullets)

run()