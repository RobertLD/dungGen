#!/usr/bin/env python3

# import modules
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib
import configparser

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# import list of modules in __modules__
from __modules__ import printHeader


# enables colored output on windows machines
init(convert=True)

printHeader.printHeader()

print(
	Fore.RED
    + Style.BRIGHT
    + "Input theme. For theme options type -ls"
    + Style.NORMAL
    + Fore.CYAN
)
theme = input()
