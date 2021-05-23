import re
import bisect

testSet = open("testSet.txt", "rt")
trainingSet = open("trainingSet.txt", "rt")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def getVocab(set):
    lines = []
    vocabulary = []

    for line in set:
        line = line.strip()
        line = line.split('\t')
        line[0] = line[0].strip()
        line[0] = re.sub(r'[^\w | \s]', '', line[0])
        line[0] = line[0].lower()
        line[0] = line[0].split()
        for word in line[0]:
            bisect.insort(vocabulary, word)
        line[1] = line[1].strip()
        line[1] = int(line[1])

        lines.append(line)

    # vocabulary = list(set(vocabulary))

    # print(lines)
    return vocabulary

print(list(set(getVocab(trainingSet))))

# vocabulary = list(set(getVocab(trainingSet)))
# vocabulary.sort()
