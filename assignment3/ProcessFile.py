import re
import os


def parse_file(file):
    lines = []

    for line in file:
        line = line.strip()
        line = line.split('\t')
        line[0] = line[0].strip()
        line[0] = re.sub(r'[^\w|\s]', '', line[0])
        line[0] = line[0].lower()
        line[0] = line[0].split()
        line[1] = line[1].strip()
        line[1] = int(line[1])
        lines.append(line)
    return lines


def get_vocab(lines):
    vocab = set()
    for line in lines:
        for word in line[0]:
            vocab.add(word)
    return sorted(vocab)


def create_feature(vocab, lines):
    m = len(vocab)
    features = []

    feature = [0] * (m + 1)
    for word in lines[0][0]:
        for i in range(len(vocab)):
            if word == vocab[i]:
                feature[i] = 1

    for line in lines:
        features.append([0] * (m + 1))
        for word in line[0]:
            for i in range(m):
                if word == vocab[i]:
                    features[-1][i] = 1
        if line[1] == 1:
            features[-1][-1] = 1

    return features


def output_preprocessed(vocab, filepath, features):
    if os.path.exists(filepath):
        os.remove(filepath)

    out = open(filepath, "w")

    for word in range(len(vocab) - 1):
        out.write(str(vocab[word]) + ',')
    out.write(str(vocab[-1]) + ',classpath\n')

    for feature in features:
        for word in range(len(feature) - 1):
            out.write(str(feature[word]) + ',')
        out.write(str(feature[-1]) + '\n')

    out.close()