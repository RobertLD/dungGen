#!/usr/bin/env python3
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# used to color console output


def printHeader():
    headerFile = open(fileDir + "\\header", "r")
    print(Fore.RED + headerFile.read() + Style.RESET_ALL)

