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

    def printRoom(self):
        # prints all the information about the room!
        print(
            "RoomID: %s \n\nExits: \nNorth: %s\nSouth: %s\nEast: %s\nWest: %s\n"
            % (self.id, self.north, self.south, self.east, self.west)
        )
