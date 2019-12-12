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
from __modules__ import mapGen


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

    # TODO: Edit the roomID creater to only create  # size IDs
    for i in range(0, size):
        for j in range(0, len(roomIDs[i])):
            roomIDs[i][j] = random.randint(10 ** (20 - 1), (10 ** 20) - 1)
    # seperate given key information to fill the user variables
    print(roomIDs)
    userVariables = seed.split("|")
# output the generated dungeon ID so that users can copy it if they like
dungeonID = seed
print("Youre DUNGEON ID is: " + str(dungeonID))


# TODO: Build map generation based roomIDS. Pass variable list to entrance gen
# generateMap(roomIDs, size)
# head = mapGen(userVariables, roomIDs,)
head = mapGen.Room(roomID=roomIDs[5][5])
rooms = mapGen.generateMap(head, roomIDs, 5, 5, size)


def printInorder(root, i):

    if root:

        # First recur on left child
        try:
            printInorder(root.north, i + 1)
        except:
            pass
        # First recur on left child
        try:
            printInorder(root.south, i + 1)
        except:
            pass
        # First recur on left child
        try:
            printInorder(root.east, i + 1)
        except:
            pass
        # First recur on left child
        try:
            printInorder(root.west, i + 1)
        except:
            pass

        # then print the data of node
        print("Room: @ " + str(i) + " is " + str(root.id))


printInorder(head, 0)

