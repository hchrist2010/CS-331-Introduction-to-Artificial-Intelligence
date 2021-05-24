import re
import os
import bisect

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
        # for word in line[0]:
        #     vocab.add(word)
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


# class feature:
#     def __init__(self, size):
#         self.size = size
#         self.feats = [0] * (size + 1)
#
#     def setFeatures(selfself, sentence):

def createFeature(vocab, lines):
    M = len(vocab)

    feature = [0] * (M + 1)
    for word in lines[0][0]:
        for i in range(len(vocab)):
            if word == vocab[i]:
                feature[i] = 1

    features = []
    featureLen = 0
    for line in lines:
        features.append([0] * (M + 1))
        for word in line[0]:
            for i in range(M):
                if(word == vocab[i]):
                    features[featureLen][i] = 1
        if line[1] == 1:
            features[featureLen][M] = 1
        featureLen += 1

    return features

def outputPreProcessed(vocab, filePath, features):
    if os.path.exists(filePath):
        os.remove(filePath)

    out = open(filePath, "w")

    for word in vocab:
        out.write('%s,'% word)
    out.write('classlabel')
    out.write('\n')

    for feature in features:
        for feat in feature:
            out.write('%d,' % feat)
        out.write('\n')


    # if os.path.exists("preprocessed_train.txt"):
    #     os.remove("preprocessed_train.txt")
    # if os.path.exists("preprocessed_test.txt"):
    #     os.remove("preprocessed_test.txt")

trainingLines = parseFile(trainingFile)
testLines = parseFile(testFile)

trainingVocab = getVocab(trainingLines)

trainingFeatures = createFeature(trainingVocab, trainingLines)
testFeatures = createFeature(trainingVocab, testLines)

outputPreProcessed(trainingVocab, "preprocessed_train.txt", trainingFeatures)
outputPreProcessed(trainingVocab, "preprocessed_test.txt", testFeatures)
