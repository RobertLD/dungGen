#!/usr/bin/env python3
import sys
import os
import importlib
import random


class Room:
    def __init__(self, val):
        self.roomID = val
        self.north = None  # the pointer initially points to nothing
        self.south = None  # the pointer initially points to nothing
        self.east = None  # the pointer initially points to nothing
        self.west = None  # the pointer initially points to nothing


class Hallway:
    def __init__(self, hallID):
        self.val = hallID
        self.start = None  # the pointer initially points to nothing
        self.end = None  # the pointer initially points to nothing


def roomInit(roomIDs, c, r):

    # the initial room @ c/r with seed roomIDs [c][r]
    random.seed(roomIDs[c][r])
    start = Room(roomIDs[c][r])

    # the value of the room is equal to the seed that generated it
    start.val = roomIDs[c][r]

    # use the seed to determine if it has rooms attached
    start.north = bool(random.getrandbits(1))
    start.south = bool(random.getrandbits(1))
    start.east = bool(random.getrandbits(1))
    start.west = bool(random.getrandbits(1))

    return start


# define starting size variable
def __init__(self,userVariables, roomIDs):
    size = int(userVariables[0])
    head = roomInit(roomIDs, 4, 4)
    print(5)
    size = userVariables[0]
    mapGen(self,roomIDs, size, head, 4, 4)
    return head


def mapGen(self, roomIDs, internalSize, Room, c, r):
    # if this is the first room, init the head of the list

    # base case
    if internalSize == 0:
        return mapGen(self, roomIDs, internalSize - 1, Room.west, c, r - 1)
    if Room.north == True:
        Room.north = roomInit(roomIDs, c + 1, r)
        return mapGen(self, roomIDs, internalSize - 1, Room.north, c, r - 1)
    if Room.south == True:
        Room.south = roomInit(roomIDs, c - 1, r)
        return mapGen(self, roomIDs, internalSize - 1, Room.south, c, r - 1)
    if Room.east == True:
        Room.east = roomInit(roomIDs, c, r + 1)
        return mapGen(self, roomIDs, internalSize - 1, Room.east, c, r - 1)
    if Room.west == True:
        Room.west = roomInit(roomIDs, c, r - 1)
        return mapGen(self, roomIDs, internalSize - 1, Room.west, c, r - 1)
    
roomIDs = [[0 for x in range(100)] for y in range(100)]
for i in range(0, 100):
        for j in range(0, len(roomIDs[i])):
            roomIDs[i][j] = random.randint(10 ** (20 - 1), (10 ** 20) - 1)


head = mapGen.__init__((5, 1), roomIDs)

