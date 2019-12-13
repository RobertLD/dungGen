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
            self.north.insert = Room(roomIds[c + 1][r])
        if self.south == True:
            self.south.insert = Room(roomIds[c - 1][r])
        if self.east == True:
            self.east.insert = Room(roomIds[c][r + 1])
        if self.west == True:
            self.west.insert = Room(roomIds[c][r - 1])


def generateMap(Head, RoomIds, c, r, size):
    print("Creating Node! Size @ " + str(size))
    if size <= 0:
        return Head
    Head = Room(RoomIds[c][r])
    if Head.north == True:
        tmp = Head.north
        return generateMap(tmp, RoomIds, c + 1, r, size - 1)
    if Head.south == True:
        tmp = Head.south
        return generateMap(tmp, RoomIds, c - 1, r, size - 1)
    if Head.east == True:
        tmp = Head.east
        return generateMap(tmp, RoomIds, c, r + 1, size - 1)
    if Head.west == True:
        tmp = Head.west
        return generateMap(tmp, RoomIds, c, r - 1, size - 1)

