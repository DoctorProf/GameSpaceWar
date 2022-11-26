import pygame, Events
from Gun import Gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Kosmo')
    bgColor = (0,0,0)
    gun = Gun(screen)

    while True:
        Events.event(gun)
        gun.updateGun()
        screen.fill(bgColor)
        gun.draw()
        pygame.display.update()

run()