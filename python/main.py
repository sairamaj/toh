import toh
import ui
def showCongratulationsMessage(count):
    ui.printSuccess(f"Congratulations. Game is over. Number of stpes you took:{count}")

def showUsage():
    print('__________________________________________________')
    print("Game aim is to move all discs from first tower to any other towwer")
    print("Rules")
    print("   Only small dics can go on to the bigger disc")
    print('__________________________________________________')
    print()


toh = toh.Toh()
toh.start()

quit = False
showUsage()

while quit==False:
    fromTower = int(input("from:"))
    toTower = int(input("to:"))
    print("from", fromTower, "to", toTower)
    try:
        toh.move(fromTower, toTower)
        ui.printSuccess('successfully moved!')
    except Exception as e:
        ui.printError(str(e))

    # check whether game is over
    if toh.isGameOver() == True:
        showCongratulationsMessage(toh.getMoveCount())
        quit = True

