#!/usr/bin/env python3
import sys
import os
import importlib
import random

# creates the default Room class (essentially a node in a linked list with four children)
class Room:
    def __init__(self, roomID, previousConnection, previousConnectionPointer):

        # the initial room @ c/r with seed roomIDs [c][r]
        random.seed(roomID)

        # the value of the room is equal to the seed that generated it
        self.id = roomID

        # use previous connection and the previousConnectionPointer to determine the linkage between rooms
        # use the seed to determine if it has rooms attached
        if previousConnection == "north":
            # set the previous connection to the connecting rooms pointer
            self.south = previousConnectionPointer
            self.north = bool(random.getrandbits(1))
            self.east = bool(random.getrandbits(1))
            self.west = bool(random.getrandbits(1))
            return
        elif previousConnection == "south":
            # set the previous connection to the connecting rooms pointer
            self.north = previousConnectionPointer
            self.south = bool(random.getrandbits(1))
            self.east = bool(random.getrandbits(1))
            self.west = bool(random.getrandbits(1))
            return
        elif previousConnection == "east":
            # set the previous connection to the connecting rooms pointer
            self.west = previousConnectionPointer
            self.north = bool(random.getrandbits(1))
            self.south = bool(random.getrandbits(1))
            self.east = bool(random.getrandbits(1))
            return
        elif previousConnection == "west":
            # set the previous connection to the connecting rooms pointer
            self.east = previousConnectionPointer
            self.north = bool(random.getrandbits(1))
            self.south = bool(random.getrandbits(1))
            self.west = bool(random.getrandbits(1))
            return

        # base case no pointers passed
        self.west = bool(random.getrandbits(1))
        self.north = bool(random.getrandbits(1))
        self.south = bool(random.getrandbits(1))


def generateMap(Head, RoomIds, c, r, size):
    print("Creating Node! Size @ " + str(size))
    if size == 0:
        return
    if Head.north == True:
        Head.north = Room(RoomIds[c + 1][r], "south", Head)
        return generateMap(Head.north, RoomIds, c + 1, r, size - 1)
    if Head.south == True:
        Head.south = Room(RoomIds[c - 1][r], "north", Head)
        return generateMap(Head.south, RoomIds, c - 1, r, size - 1)
    if Head.east == True:
        Head.east = Room(RoomIds[c][r + 1], "west", Head)
        return generateMap(Head.east, RoomIds, c, r + 1, size - 1)
    if Head.west == True:
        Head.west = Room(RoomIds[c][r - 1], "east", Head)
        return generateMap(Head.west, RoomIds, c, r - 1, size - 1)

