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
import hashlib

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# import list of modules in __modules__
from __modules__ import printHeader


# enables colored output on windows machines
init(convert=True)

printHeader.printHeader()
print(Fore.RED + Style.BRIGHT + "Use dungeon code? [y/n]" + Style.NORMAL + Fore.CYAN)
seedOrCustom = input()

if seedOrCustom != "y":
    # ask for basic userinputs
    print(Fore.RED + Style.BRIGHT + "Size:" + Style.NORMAL + Fore.CYAN)
    size = input()
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
        size + theme + setting + complexity + wealth + faction + story + difficulty
    )

    # TODO: Move seed generation into a module to keep things a little less messy
    # hash the result of the use selected inputs
    hashUserSelectedSeed = int(
        (hashlib.md5(userSelectedSeed.encode("utf-8"))).hexdigest(), 16
    )
    # generate a second seed
    randomSeed = int(random.random() * 100)

    unhashedSeed = str(hashUserSelectedSeed) + str(randomSeed)

    seed = (hashlib.md5(unhashedSeed.encode("utf-8"))).hexdigest()
    seed = int(seed, 16) % ((2 ^ 32) - 1)

# account for the fact that the user may want to use their own
else:
    print(Fore.RED + Style.BRIGHT + "Seed:" + Style.NORMAL + Fore.CYAN)
    seed = input()

numpy.random.seed(seed * 100000)
array = numpy.random.rand(10, 10)
for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        array[i][j] = int(array[i][j] * 100000000)
print(array)
