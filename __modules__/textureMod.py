#!/usr/bin/env python3
import sys
import os
import pandas as pd
from colorama import init
from colorama import Fore, Back, Style
import importlib
import configparser
import numpy 
import csv

# gets the current path of installation to assist with opening/reading files
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

#custom function to open .csv and save to an array
def readcsv(filename):
	with open(filename, newline='') as csvfile:
		data = list(csv.reader(csvfile))
	return(data)

#generate room texture data based on roomID and  cardinal data
def textureGen():#(roomKey, nE, sE, eE, wE):
	#breaks down room id into room texture values to generate components from .csv
	roomKey = 28443015103400553158
	roomString = str(roomKey)
	roomWeights = [roomString[i:i+2] for i in range(0, len(roomString), 2)]
	setting = "castle"
	theme = "lair"
	nE = 1
	sE = 0
	eE = 1
	wE = 0
	#extract texture values from roomID
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

#generate initial dungeon entrance and location description seperate to the rooms
def initialPrint (setting, theme, dungeonID):
	dungeonID = dungeonID[len(dungeonID)-6:len(dungeonID)]
	dungeonID = int(dungeonID,16)
	dungeonID = str(dungeonID)
	location = int(dungeonID[len(dungeonID)-2:len(dungeonID)])
	entrance = int(dungeonID[len(dungeonID)-4:len(dungeonID)-2])
	locationArray = readcsv(parentDir + "\\resources\\location\\" + setting + ".csv")
	entranceArray = readcsv(parentDir + "\\resources\\entrance\\" + theme + ".csv")
	for x in range(0,len(locationArray)):
		if int(location) <= int(locationArray[x][0]):
			locationString = locationArray[x][1]
			break
	for x in range(0,len(entranceArray)):
		if int(entrance) <= int(entranceArray[x][0]):
			entranceString = entranceArray[x][1]
			break
	initialString = locationString + entranceString
	initialString = initialString.replace('","',',')
	print("\n\n" + initialString)
