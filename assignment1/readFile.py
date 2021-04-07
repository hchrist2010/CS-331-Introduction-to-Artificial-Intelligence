import csv
from dispatch import dispatch

def readFiles(startFile, goalFile, mode, outputFile):
    start = readFile(startFile)
    goal = readFile(goalFile)
    dispatch(start, goal, mode, outputFile)

def readFile(file):
    currentline = []
    with open(file, "r") as startCSV:
        for line in startCSV:
            line = line.rstrip('\n')
            line = line.split(',')
            line = [int(i) for i in line]
            currentline.append(line)
        return currentline
