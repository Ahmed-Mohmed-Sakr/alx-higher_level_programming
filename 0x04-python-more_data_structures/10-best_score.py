#!/usr/bin/python3

def best_score(a_dictionary):

    if (not a_dictionary):
        return (None)

    bestk = ""
    bestS = 0

    for a, v in a_dictionary.items():
        if(v >= bestS):
            bestK = a

    return bestK
