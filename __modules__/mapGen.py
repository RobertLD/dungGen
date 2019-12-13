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
        if self == True:
            self = Room(roomIds[c][r])


def generateMap(Head, RoomIds, c, r, size):
    print("Creating Node! Size @ " + str(size))
    if size == 0:
        return
    if Head.north == True:
        Head.north = Room(RoomIds[c + 1][r])
        return generateMap(Head.north, RoomIds, c + 1, r, size - 1)
    if Head.south == True:
        Head.south = Room(RoomIds[c - 1][r])
        return generateMap(Head.south, RoomIds, c - 1, r, size - 1)
    if Head.east == True:
        Head.east = Room(RoomIds[c][r + 1])
        return generateMap(Head.east, RoomIds, c, r + 1, size - 1)
    if Head.west == True:
        Head.west = Room(RoomIds[c][r - 1])
        return generateMap(Head.west, RoomIds, c, r - 1, size - 1)

