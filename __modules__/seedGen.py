#!/usr/bin/env python3
import numpy
import random
import hashlib


def seedGen(userSelectedSeed, size):

    # Hash the result of the user selected options
    hashUserSelectedSeed = int(
        (hashlib.md5(userSelectedSeed.encode("utf-8"))).hexdigest(), 16
    )
    # generate a randomn salt to shift the hash of the final seed
    salt = random.randint(0, 99)

    # this is the intermediate seed before it is hashed a second time with the salt value
    unhashedSeed = str(hashUserSelectedSeed) + str(salt)
    seed = (hashlib.md5(unhashedSeed.encode("utf-8"))).hexdigest()

    # ensure that the given seed is not out of bounds for the numpy function
    # whose maximum value is 2^32
    seed = int(seed, 16) % ((2 ^ 32) - 1)
    numpy.random.seed(seed)
    array = numpy.random.rand(size * 2, size * 2)
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            # take each element in the array and salt it
            array[i][j] = int(
                int(array[i][j] * (10 ** 8))
            )  # adjust values to fit the integer range we need
    return array
