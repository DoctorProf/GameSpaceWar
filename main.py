import pygame, Events
from Gun import Gun
from pygame.sprite import Group
from stats import Stats
def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('SpaceWar')
    bgColor = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    Events.createArmy(screen, inos)
    stats = Stats()

    while True:
        Events.event(screen, gun, bullets)
        gun.updateGun()
        Events.update(bgColor, screen, gun, inos, bullets)
        Events.updateBullets(screen, inos, bullets)
        Events.updateInos(stats, screen, gun, inos, bullets)

run()