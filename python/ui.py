from colorama import init
from colorama import Fore, Back, Style

init()

def printError(str1):
    print(getattr(Fore, 'RED') + str1 + Fore.WHITE)

def printSuccess(str1):
    print(getattr(Fore, 'GREEN') + str1 + Fore.WHITE)

