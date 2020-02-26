from colorama import init
from colorama import Fore, Back, Style


class Disc:
    def __init__(self, size, referenceX, color):
        self.size = size
        self.referenceX = referenceX
        self.color = color

    def getSize(self):
        return self.size

    def draw(self):
        n = 0
        startPos = int(self.referenceX - (self.size/2))
        # print(''.rjust(startPos), end='')
        print(' '*startPos, end='')
        while n < self.size:
            #print('_', end='')
            print(getattr(Fore, self.color) + '_' + Fore.WHITE, end='')
            n = n+1
        print()
