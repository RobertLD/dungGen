#!/usr/bin/env python3
import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib
import configparser

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)
# open the header text file
headerFile = open(fileDir + "\\resources\\header", "r", encoding="utf8")
headerText = str(headerFile.read())
headerFile.close()

# open the config file
config = configparser.ConfigParser()
config.read(parentDir + "\\config\\mainConfig.ini")

# loadvalues from config file
versionNumber = config.get("default", "version")

# replace version number from config file
headerText = headerText.replace("[x.x.x]", versionNumber)

# print header funciton
def printHeader():
    print(Fore.RED + Back.WHITE + headerText + Style.RESET_ALL)

