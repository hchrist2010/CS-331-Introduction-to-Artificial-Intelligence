import sys
import numpy as np
import ProcessFile

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


def train_classifiers(vocab):
    train = np.genfromtxt('preprocessed_train.txt', skip_header=1, delimiter=',')
    positive_class, negative_class = separate_by_class(train)


def main():
    training_lines = ProcessFile.parse_file(trainingFile)
    test_lines = ProcessFile.parse_file(testFile)

    training_vocab = ProcessFile.get_vocab(training_lines)

    training_features = ProcessFile.create_feature(training_vocab, training_lines)
    test_features = ProcessFile.create_feature(training_vocab, test_lines)

    ProcessFile.output_preprocessed(training_vocab, "preprocessed_train.txt", training_features)
    ProcessFile.output_preprocessed(training_vocab, "preprocessed_test.txt", test_features)

    train_classifiers(training_vocab)


if __name__ == "__main__":
    main()
