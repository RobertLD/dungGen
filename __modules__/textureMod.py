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

def textureGen():#(roomKey, nE, sE, eE, wE):
	roomKey = 28443015103400553158
	roomString = str(roomKey)	
	roomWeights = [roomString[i:i+2] for i in range(0, len(roomString), 2)]
	setting = "castle"
	theme = "lair"
	nE = 1
	sE = 0
	eE = 1
	wE = 0
	size = roomWeights[0]
	floor = roomWeights[1]
	walls = roomWeights[2]
	ceiling = roomWeights[3]
	lighting = roomWeights[4]
	furniture = roomWeights[5]
	detail = roomWeights[6]
	loot = roomWeights[7]
	doorway = roomWeights[8]
	npc = roomWeights[9]	
textureGen()