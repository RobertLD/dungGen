#!/usr/bin/env python3

# import modules
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib
import configparser
import numpy
import random

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# import list of modules in __modules__
from __modules__ import printHeader
from __modules__ import seedGen
from __modules__ import textureMod


# enables colored output on windows machines
init(convert=True)

printHeader.printHeader()
print(Fore.RED + Style.BRIGHT + "Use dungeon code? [y/n]" + Style.NORMAL + Fore.CYAN)
seedOrCustom = input()

settingsFile = open(parentDir + "\\dunggen\\resources\\settings.txt", "r")
themesFile = open(parentDir + "\\dunggen\\resources\\themes.txt", "r")
settingsText = str(settingsFile.read())
themesText = str(themesFile.read())

if seedOrCustom != "y":
    # ask for basic userinputs
    print(Fore.RED + Style.BRIGHT + "Size:" + Style.NORMAL + Fore.CYAN)
    size = int(input())
    print(Fore.RED + Style.BRIGHT + "Theme:\nInput 'ls' for a list of options." + Style.NORMAL + Fore.CYAN)
    theme = input()
    while theme == "ls":
        print(Fore.RED + Style.BRIGHT + themesText + "\nTheme:" + Style.NORMAL + Fore.CYAN)
        theme = input()
    print(Fore.RED + Style.BRIGHT + "Setting:\nInput 'ls' for a list of options." + Style.NORMAL + Fore.CYAN)
    setting = input()
    while setting == "ls":
        print(Fore.RED + Style.BRIGHT + settingsText + "\nSetting:" + Style.NORMAL + Fore.CYAN)
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

    # use above data to generate a seed
    userSelectedSeed = (
        str(size)
        + "|"
        + theme
        + "|"
        + setting
        + "|"
        + complexity
        + "|"
        + wealth
        + "|"
        + faction
        + "|"
        + story
        + "|"
        + difficulty
        + "|"
    )

    # generate the seed
    seed = seedGen.seedGen(userSelectedSeed, size)

    # seed the random number generator
    random.seed(seed)

    # generate size * size array of zeros
    roomIDs = [[0 for x in range(size)] for y in range(size)]

    # fill the generated array with random int of 20 digits
    for i in range(0, size):
        for j in range(0, len(roomIDs[i])):
            roomIDs[i][j] = random.randint(10 ** (20 - 1), (10 ** 20) - 1)

    userVariables = (
        str(size),
        theme,
        setting,
        complexity,
        wealth,
        faction,
        story,
        difficulty,
        seed,
    )

# account for the fact that the user may want to use their own
else:
    print(Fore.RED + Style.BRIGHT + "Seed:" + Style.NORMAL + Fore.CYAN)
    seed = input()

    random.seed(seed)

    # if the first character is not a number -- make it a number
    if seed[0].isalpha():
        size = ord(seed[0])
    else:
        size = int(seed[0])

    roomIDs = [[0 for x in range(size)] for y in range(size)]

    for i in range(0, size):
        for j in range(0, len(roomIDs[i])):
            roomIDs[i][j] = random.randint(10 ** (20 - 1), (10 ** 20) - 1)
    # seperate given key information to fill the user variables
    userVariables = seed.split("|")

# output the generated dungeon ID so that users can copy it if they like
dungeonID = seed
print("Youre DUNGEON ID is: " + str(dungeonID))
print(userVariables)


# TODO: Build map generation based roomIDS. Pass variable list to entrance gen
# generateMap(roomIDs, size)
print(roomIDs)

#run function that produces and prints entry location and description based on setting, theme, and dungeonID for random but consistent num
textureMod.initialPrint(setting,theme,dungeonID)
