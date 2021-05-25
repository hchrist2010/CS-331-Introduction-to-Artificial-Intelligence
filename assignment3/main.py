import sys
import numpy as np
import ProcessFile
from math import pi
from math import exp

import math

np.set_printoptions(threshold=sys.maxsize)

testFile = open("testSet.txt", "rt")
trainingFile = open("trainingSet.txt", "rt")


def print_sentence(feature, vocab):
    for i in range(len(feature) - 1):
        if feature[i] == 1:
            print(vocab[i], end=" ")
    print()


def separate_by_class(features):
    class1 = np.empty((0, features.shape[1]), int)
    class2 = np.empty((0, features.shape[1]), int)

    for line in features:
        if line[-1] == 1:
            class1 = np.append(class1, [line], axis=0)
        else:
            class2 = np.append(class2, [line], axis=0)

    return class1[:,:-1], class2[:,:-1]


def train_classifiers(trainifile, testfile):
    train = np.genfromtxt(trainifile, skip_header=1, delimiter=',')
    test = np.genfromtxt(testfile, skip_header=1, delimiter=',')
    positive_class, negative_class = separate_by_class(train)
    positive_class_mean = np.mean(positive_class, axis=0)
    positive_class_stdev = np.std(positive_class, axis=0)
    negative_class_mean = np.mean(negative_class, axis=0)
    negative_class_stdev = np.std(negative_class, axis=0)

    labels = train[:,-1]

    positive_sum = np.sum(positive_class, axis=0)
    negative_sum = np.sum(negative_class, axis=0)
    total_sum = (positive_sum + negative_sum)

    py1_mean = len(positive_class) / len(train)
    py0_mean = len(negative_class) / len(train)

    py1_x1 = np.log(positive_sum + 1) - np.log(positive_class.shape[0] + 2)
    py1_x0 = np.log((positive_class.shape[0] - positive_sum) + 1) - np.log(positive_class.shape[0] + 2)

    py0_x1 = np.log(negative_sum + 1) - np.log(negative_class.shape[0] + 2)
    py0_x0 = np.log((negative_class.shape[0] - negative_sum) + 1) - np.log(negative_class.shape[0] + 2)

    results = []


    for line in test:
        positive = 0
        negative = 0
        for j in range(test.shape[1] - 1):
            if line[j] == 1:
                positive += py1_x1[j]
                negative += py0_x1[j]
            else:
                positive += py1_x0[j]
                negative += py0_x0[j]

        positive += math.log(py1_mean)
        negative += math.log(py0_mean)

        if positive >= negative:
            results.append(1)
        else:
            results.append(0)

    correct = 0
    incorrect = 0

    for i in range(len(results)):
        if(labels[i] == results[i]):
            correct += 1
        else:
            incorrect += 1

    print(correct, incorrect)
    print(correct / (correct + incorrect))
    print()

def main():
    training_lines = ProcessFile.parse_file(trainingFile)
    test_lines = ProcessFile.parse_file(testFile)

    training_vocab = ProcessFile.get_vocab(training_lines)

    training_features = ProcessFile.create_feature(training_vocab, training_lines)
    test_features = ProcessFile.create_feature(training_vocab, test_lines)

    train_classifiers('preprocessed_train.txt', 'preprocessed_train.txt')
    train_classifiers('preprocessed_train.txt', 'preprocessed_test.txt')

    # ProcessFile.output_preprocessed(training_vocab, "preprocessed_train.txt", training_features)
    # ProcessFile.output_preprocessed(training_vocab, "preprocessed_test.txt", test_features)


if __name__ == "__main__":
    main()
