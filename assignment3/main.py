import re
import os
import sys
import numpy as numpy
numpy.set_printoptions(threshold=sys.maxsize)

testFile = open("testSet.txt", "rt")
trainingFile = open("trainingSet.txt", "rt")

def parseFile(file):
    lines = []
    vocab = set()

    for line in file:
        line = line.strip()
        line = line.split('\t')
        line[0] = line[0].strip()
        line[0] = re.sub(r'[^\w | \s]', '', line[0])
        line[0] = line[0].lower()
        line[0] = line[0].split()
        line[1] = line[1].strip()
        line[1] = int(line[1])
        lines.append(line)
    return lines

def getVocab(lines):
    vocab = set()
    for line in lines:
        for word in line[0]:
            vocab.add(word)
    return sorted(vocab)


def createFeature(vocab, lines):
    M = len(vocab)
    features = []

    feature = [0] * (M + 1)
    for word in lines[0][0]:
        for i in range(len(vocab)):
            if word == vocab[i]:
                feature[i] = 1

    for line in lines:
        features.append([0] * (M + 1))
        for word in line[0]:
            for i in range(M):
                if(word == vocab[i]):
                    features[-1][i] = 1
        if line[1] == 1:
            features[-1][-1] = 1

    return features


def outputPreProcessed(vocab, filePath, features):
    if os.path.exists(filePath):
        os.remove(filePath)

    out = open(filePath, "w")

    for word in range(len(vocab) - 1):
        out.write(str(vocab[word]) + ',')
    out.write(str(vocab[-1]) + ',classpath\n')

    for feature in features:
        for word in range(len(feature) - 1):
            out.write(str(feature[word]) + ',')
        out.write(str(feature[-1]) + '\n')

    out.close()

def printSentence(vocab, feature):
    for i in range(len(feature) - 1):
        if feature[i] == 1:
            print(vocab[i], end=" ")
    print()

def trainClassifiers(vocab):
    train = numpy.genfromtxt('preprocessed_train.txt', skip_header=1, delimiter=',')

    class1 = numpy.empty((0,train.shape[1]), int)
    class2 = numpy.empty((0,train.shape[1]), int)

    for line in train:
        if line[-1] == 1:
            class1 = numpy.append(class1, [line], axis=0)
        else:
            class2 = numpy.append(class2, [line], axis=0)





def main():
    trainingLines = parseFile(trainingFile)
    testLines = parseFile(testFile)

    trainingVocab = getVocab(trainingLines)

    trainingFeatures = createFeature(trainingVocab, trainingLines)
    testFeatures = createFeature(trainingVocab, testLines)

    outputPreProcessed(trainingVocab, "preprocessed_train.txt", trainingFeatures)
    outputPreProcessed(trainingVocab, "preprocessed_test.txt", testFeatures)

    trainClassifiers(trainingVocab)

if __name__ == "__main__":
    main()