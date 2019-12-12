#!/usr/bin/env python3
import sys
import os
import importlib
import random

# creates the default Room class (essentially a node in a linked list with four children)
class Room:
    def __init__(self, roomID):

        # the initial room @ c/r with seed roomIDs [c][r]
        random.seed(roomID)

        # the value of the room is equal to the seed that generated it
        self.id = roomID

        # use the seed to determine if it has rooms attached
        self.north = bool(random.getrandbits(1))
        self.south = bool(random.getrandbits(1))
        self.east = bool(random.getrandbits(1))
        self.west = bool(random.getrandbits(1))

    def insert(self, roomIds, c, r):
        # Compare the new value with the parent node
        if self.north == True:
            self.north.insert = Room(roomIds[c][r + 1])
        if self.south == True:
            self.south.insert = Room(roomIds[c][r - 1])
        if self.east == True:
            self.east.insert = Room(roomIds[c + 1][r])
        if self.west == True:
            self.west.insert = Room(roomIds[c - 1][r])


def generateMap(Head, RoomIds, c, r, size):
    if size <= 0:
        return

    if Head.north == True:
        try:
            Head.north = Room(roomID=RoomIds[c + 1][r])
        except:
            pass
        tmp = Head.north
        return generateMap(tmp, RoomIds, c + 1, r, size - 1)
    if Head.south == True:
        try:
            Head.north = Room(roomID=RoomIds[c - 1][r])
        except:
            pass
        tmp = Head.north
        return generateMap(tmp, RoomIds, c - 1, r, size - 1)
    if Head.east == True:
        try:
            Head.north = Room(roomID=RoomIds[c][r + 1])
        except:
            pass
        tmp = Head.north
        return generateMap(tmp, RoomIds, c, r + 1, size - 1)
    if Head.west == True:
        try:
            Head.north = Room(roomID=RoomIds[c][r - 1])
        except:
            pass
        tmp = Head.north
        return generateMap(tmp, RoomIds, c, r - 1, size - 1)

