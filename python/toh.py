import tower
import disc
import discFactory

referenceX = 45

class Toh():
    def __init__(self):
        print("in toh.init")
        towerA = tower.Tower("1", referenceX,'YELLOW')
        towerA.addDisc(discFactory.DiscFactory(referenceX).getLarge())
        towerA.addDisc(discFactory.DiscFactory(referenceX).getMedium())
        towerA.addDisc(discFactory.DiscFactory(referenceX).getSmall())
        self.towers = [towerA, tower.Tower("2", referenceX,'MAGENTA'), tower.Tower("3", referenceX,'CYAN')]
        self.moveCount = 0

    def start(self):
        self.draw()

    def move(self, fromTower, toTower):
        realFrom = fromTower-1
        realTo = toTower-1
        topDisc = self.towers[realFrom].removeTopDisc()
        if topDisc == None:
            raise Exception(f"Tower {fromTower} does not have any discs.")

        try:
            self.towers[realTo].addDisc(topDisc)
        except:
            # add disc back in case of errors
            self.towers[realFrom].addDisc(topDisc)
            raise
        self.moveCount = self.moveCount +1
        self.draw()

    def draw(self):
        for tower in self.towers:
            tower.draw()
            print()

    def isGameOver(self):
        # check whether any tower other than first one has 3 discs
        for tower in self.towers[1:]:
            if tower.getDiscCount() == 3:
                return True
        return False
    def getMoveCount(self):
        return self.moveCount