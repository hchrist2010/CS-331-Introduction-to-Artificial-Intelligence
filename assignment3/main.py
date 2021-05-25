import sys
import numpy as np
import ProcessFile
from math import pi
from math import exp
from math import log

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

    return class1, class2


def train_feature_probabilities(data, feature_label, class_label):
    features = data[:,:-1].T    # store feature vectors without class labels, transpose so each row is all instances of a single feature
    labels = data[:,-1]         # store class labels in their own vector
    probabilities = np.zeros(features.shape[0])

    denominator = labels.shape[0]
    for i in range(labels.shape[0]):
        if labels[i] == class_label:
            denominator += 1

    for i in range(features.shape[0]):
        numerator = 1
        for j in range(features.shape[1]):
            if features[i][j] == feature_label and labels[j] == class_label:
                numerator += 1
        probabilities[i] = log(numerator / denominator)

    return probabilities


def get_class_probabilities(data):
    labels = data[:,-1]
    numerator = 0
    for label in labels:
        if label == 1:
            numerator += 1
    return numerator / labels.shape[0]


def train_classifiers(vocab):
    train = np.genfromtxt('preprocessed_train.txt', skip_header=1, delimiter=',')
    # positive_class, negative_class = separate_by_class(train)
    p_x0_y0 = train_feature_probabilities(train, 0, 0)
    p_x0_y1 = train_feature_probabilities(train, 0, 1)
    p_x1_y0 = train_feature_probabilities(train, 1, 0)
    p_x1_y1 = train_feature_probabilities(train, 1, 1)
    p_y0 = get_class_probabilities(train)
    p_y1 = get_class_probabilities(train)
    return train, p_x0_y0, p_x0_y1, p_x1_y0, p_x1_y1, p_y0, p_y1


def predict_class(features):
    print('hi')


def main():
    training_lines = ProcessFile.parse_file(trainingFile)
    test_lines = ProcessFile.parse_file(testFile)

    training_vocab = ProcessFile.get_vocab(training_lines)

    training_features = ProcessFile.create_feature(training_vocab, training_lines)
    test_features = ProcessFile.create_feature(training_vocab, test_lines)

    ProcessFile.output_preprocessed(training_vocab, "preprocessed_train.txt", training_features)
    ProcessFile.output_preprocessed(training_vocab, "preprocessed_test.txt", test_features)

    train, p_x0_y0, p_x0_y1, p_x1_y0, p_x1_y1, p_y0, p_y1 = train_classifiers(training_vocab)
    # print(p_x0_y0)
    # print(p_x0_y1)
    # print(p_x1_y0)
    # print(p_x1_y1)
    feature_vector = train[3][:-1]
    class_label = train[3][-1]

    acc = 0.0

    for j in range(train.shape[0]):
        feature_vector = train[j][:-1]
        class_label = train[3][-1]
        y0 = p_y0
        y1 = p_y1
        for i in range(feature_vector.shape[0]):
            if feature_vector[i] == 0:
                y0 += p_x0_y0[i]
                y1 += p_x0_y1[i]
            else:
                y0 += p_x1_y0[i]
                y1 += p_x1_y1[i]
        if (y0 >= y1 and class_label == 0) or (y1 > y0 and class_label == 1):
            acc += 1.0

    print(acc / float(train.shape[0]))



if __name__ == "__main__":
    main()
