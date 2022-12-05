class Stats():

    def __init__(self):

        self.resetStats()
        self.runGame = True
        with open('Record.txt','r') as f:
            self.HighScore = int(f.readline())

    def resetStats(self):
        
        self.gunsLive = 2
        self.score = 0