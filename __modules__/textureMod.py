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

def readcsv(filename):
	with open(filename, newline='') as csvfile:
		data = list(csv.reader(csvfile))
	return(data)

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

def initialPrint (setting, theme, dungeonID):
	#print(ord(dungeonID))
	dungeonID = dungeonID[len(dungeonID)-4:len(dungeonID)]
	print(dungeonID)
	dungeonID = int(dungeonID,16)
	print(dungeonID)
	print("location seed?")
	location = input()
	print("entrance seed?")
	entrance = input()
	#print("setting?")
	#setting = input()
	#print("theme?")
	#theme = input()
	locationArray = readcsv(parentDir + "\\resources\\location\\" + setting + ".csv")
	entranceArray = readcsv(parentDir + "\\resources\\entrance\\" + theme + ".csv")
	locationString = "k"
	entranceString = "l"
	#print(locationArray)
	#print(len(locationArray))
	for x in range(0,len(locationArray)):
		if int(location) <= int(locationArray[x][0]):
			locationString = locationArray[x][1]
			break
	#print(locationString)
	for x in range(0,len(entranceArray)):
		if int(entrance) <= int(entranceArray[x][0]):
			entranceString = entranceArray[x][1]
			break
		#print("oooof")
	initialString = locationString + entranceString
	initialString = initialString.replace('","',',')
	print(initialString)
#initialPrint()
