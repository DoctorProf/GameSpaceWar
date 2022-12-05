import pygame.font
from Gun import Gun
from pygame.sprite import Group

class Score():

    def __init__(self, screen, stats):

        self.screen = screen
        self.screenRect = screen.get_rect()
        self.stats = stats
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.ScoreImage()
        self.RecordImage()
        self.GunImage()
    
    def ScoreImage(self):

        self.ScoreImg = self.font.render(str(self.stats.score), True, self.textColor, (0,0,0))
        self.scoreRect = self.ScoreImg.get_rect()
        self.scoreRect.right = self.screenRect.right - 40
        self.scoreRect.top = 20

    def RecordImage(self):

        self.HighScoreImg = self.font.render(str(self.stats.HighScore), True, self.textColor, (0,0,0))
        self.HighScoreRect = self.HighScoreImg.get_rect()
        self.HighScoreRect.centerx = self.screenRect.centerx
        self.HighScoreRect.top = self.screenRect.top + 20
    
    def GunImage(self):
        self.guns = Group()
        for gunNum in range(self.stats.gunsLive):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gunNum * gun.rect.width
            gun.rect.y = 20
            self.guns.add_internal(gun)
    def showScore(self):

        self.screen.blit(self.ScoreImg, self.scoreRect)
        self.screen.blit(self.HighScoreImg, self.HighScoreRect)
        self.guns.draw(self.screen)