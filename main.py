import pygame, Events
from Gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Score
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
    sc = Score(screen, stats)

    while True:
        Events.event(screen, gun, bullets)

        if stats.runGame == True:

            gun.updateGun()
            Events.update(bgColor, screen, stats, sc, gun, inos, bullets)
            Events.updateBullets(screen,stats, sc, inos, bullets)
            Events.updateInos(stats, screen, sc, gun, inos, bullets)

run()