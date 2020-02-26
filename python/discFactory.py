import disc

referenceX = 25

class DiscFactory:

    def __init__(self, referenceX):
        self.referenceX = referenceX

    def getSmall(self):
        return disc.Disc(24, self.referenceX,'RED')
    
    def getMedium(self):
        return disc.Disc(36, self.referenceX,'GREEN')

    def getLarge(self):
        return disc.Disc(48, self.referenceX, 'BLUE')

    