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
headerFile = open(fileDir + "\\resources\\header", "r")

# open the config file
config = configparser.ConfigParser()
configFile = config.read("..\\mainConfig.ini")

for line in headerFile:
    fout.write(line.replace("[VERSION]", "Orange"))

# print header funciton
def printHeader():
    print(Fore.RED + headerFile.read() + Style.RESET_ALL)

