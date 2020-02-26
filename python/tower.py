from colorama import init
from colorama import Fore, Back, Style
import disc


class Tower():
    def __init__(self, name, referenceX, color):
        self.name = name
        self.color = color
        self.referenceX = referenceX
        self.discs = []

    def __str__(self):
        return "Tower"

    def draw(self):
        self.drawPole()
        for disc in self.discs[::-1]:
            disc.draw()
        title = f"Tower-{self.name}"
        pos = int(self.referenceX - (len(title)/2))
        print(' ' *pos, end='')
        print(title)

    def addDisc(self, disc):
        self.validateForAdd(disc)
        self.discs.append(disc)

    def drawPole(self):
        line = "|"
        n = 0
        while n < 4:
            print(' ' *self.referenceX, end='')
            print(Style.BRIGHT + getattr(Fore, self.color) + line + Fore.WHITE)
            # print(line)
            n = n+1

    def removeTopDisc(self):
        if len(self.discs) == 0:
            return None
        return self.discs.pop()

    def getDiscCount(self):
        return len(self.discs)

    def validateForAdd(self, disc):
        if len(self.discs) == 0:
            return  # no disc means disc can be added

        topDisc = self.discs[-1]
        if topDisc.getSize() > disc.getSize():
            return  # coming disc is smaller than top of the disc

        raise Exception(
            f"Disc {disc.getSize()} is not allowed on disc:{topDisc.getSize()}")
