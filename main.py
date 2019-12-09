#!/usr/bin/env python3

# import modules
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib
import configparser
import numpy

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# import list of modules in __modules__
from __modules__ import printHeader
from __modules__ import seedGen


# enables colored output on windows machines
init(convert=True)

printHeader.printHeader()
print(Fore.RED + Style.BRIGHT + "Use dungeon code? [y/n]" + Style.NORMAL + Fore.CYAN)
seedOrCustom = input()

if seedOrCustom != "y":
    # ask for basic userinputs
    print(Fore.RED + Style.BRIGHT + "Size:" + Style.NORMAL + Fore.CYAN)
    size = int(input())
    print(Fore.RED + Style.BRIGHT + "Theme:" + Style.NORMAL + Fore.CYAN)
    theme = input()
    print(Fore.RED + Style.BRIGHT + "Setting" + Style.NORMAL + Fore.CYAN)
    setting = input()
    print(Fore.RED + Style.BRIGHT + "Wealth:" + Style.NORMAL + Fore.CYAN)
    wealth = input()
    print(Fore.RED + Style.BRIGHT + "Faction:" + Style.NORMAL + Fore.CYAN)
    faction = input()
    print(Fore.RED + Style.BRIGHT + "Complexity:" + Style.NORMAL + Fore.CYAN)
    complexity = input()
    print(Fore.RED + Style.BRIGHT + "Story:" + Style.NORMAL + Fore.CYAN)
    story = input()
    print(Fore.RED + Style.BRIGHT + "Difficulty" + Style.NORMAL + Fore.CYAN)
    difficulty = input()

    # use above data to generate a seed of format ###.##.#
    userSelectedSeed = (
        str(size) + theme + setting + complexity + wealth + faction + story + difficulty
    )
    seed = seedGen.seedGen(userSelectedSeed, size)
# account for the fact that the user may want to use their own
else:
    print(Fore.RED + Style.BRIGHT + "Seed:" + Style.NORMAL + Fore.CYAN)
    seed = input()

# seed numpy with our generated seed
# and generete the random room-seeds

print(array)
