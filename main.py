#!/usr/bin/env python3

import sys
import os
from colorama import init
from colorama import Fore, Back, Style
import importlib

# import modules
import printHeader

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# enables colored output on windows machines
init(convert=True)

printHeader.printHeader()
