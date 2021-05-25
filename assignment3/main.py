import os
import numpy as np
import ProcessFile
import math


# Separate the features set into a positive and negative class.
# Return each class with the class label stripped off
def separate_by_class(features):
    class1 = np.empty((0, features.shape[1]), int)
    class2 = np.empty((0, features.shape[1]), int)

    for line in features:
        if line[-1] == 1:
            class1 = np.append(class1, [line], axis=0)
        else:
            class2 = np.append(class2, [line], axis=0)

    return class1[:, :-1], class2[:, :-1]


# Separate the training data into a positive and negative class based on the label provided
# Create label sets for both the training data and testing data based on the label provided for each
# Sum the positive class down the rows to get the total number of times each word is present in each class
# Means for each class is the total number of reviews in each class over the total number of reviews
# Calculate the conditional probabilities p(y=1|x=1), p(y=1|x=0), p(y=0|x=1), p(y=0|x=0) for all words in
# the vocabulary. Implement Laplace Smoothing so there are no divide by zero errors.
# Take the log of these probabilities to prevent overflow later.
# Pass everything to make_prediction to calculate results
def train_classifiers(train_file, test_file):
    positive_class, negative_class = separate_by_class(train_file)

    train_length = len(train_file)

    train_labels = train_file[:, -1]
    test_labels = test_file[:, -1]

    positive_sum = np.sum(positive_class, axis=0)
    negative_sum = np.sum(negative_class, axis=0)

    py1_mean = len(positive_class) / train_length
    py0_mean = len(negative_class) / train_length

    py1_x1 = np.log(positive_sum + 1) - np.log(positive_class.shape[0] + 2)
    py1_x0 = np.log((positive_class.shape[0] - positive_sum) + 1) - np.log(positive_class.shape[0] + 2)

    py0_x1 = np.log(negative_sum + 1) - np.log(negative_class.shape[0] + 2)
    py0_x0 = np.log((negative_class.shape[0] - negative_sum) + 1) - np.log(negative_class.shape[0] + 2)

    print('Training Accuracy:',
          make_predictions([py1_x1, py1_x0, py0_x1, py0_x0, py1_mean, py0_mean], train_file, train_labels)
          )

    print('Test Accuracy:',
          make_predictions([py1_x1, py1_x0, py0_x1, py0_x0, py1_mean, py0_mean], test_file, test_labels)
          )

# Apply test feature to the probabilities measured earlier. Compare the results of that to the labels provided
# Sum up the comparison to get the total number of correct predictions
# Return total correct / number of features being predicted to get accuracy
def make_predictions(probabilities, test_data, labels):
    results = []
    for line in test_data:
        positive = math.log(probabilities[4])
        negative = math.log(probabilities[5])
        for j in range(test_data.shape[1] - 1):
            if line[j] == 1:
                positive += probabilities[0][j]
                negative += probabilities[2][j]
            else:
                positive += probabilities[1][j]
                negative += probabilities[3][j]

        results.append(np.greater_equal(positive, negative))

    correct = sum(np.logical_not(np.logical_xor(results, labels)))

    return correct / len(results)


def main():
    if not (os.path.exists("preprocessed_train.txt") or os.path.exists("preprocessed_test.txt")):
        test_file = open("testSet.txt", "rt", encoding='utf-8')
        training_file = open("trainingSet.txt", "rt", encoding='utf-8')

        training_lines = ProcessFile.parse_file(training_file)
        test_lines = ProcessFile.parse_file(test_file)

        training_vocab = ProcessFile.get_vocab(training_lines)

        training_features = ProcessFile.create_feature(training_vocab, training_lines)
        test_features = ProcessFile.create_feature(training_vocab, test_lines)

        ProcessFile.output_preprocessed(training_vocab, "preprocessed_train.txt", training_features)
        ProcessFile.output_preprocessed(training_vocab, "preprocessed_test.txt", test_features)
    else:
        training_features = np.genfromtxt('preprocessed_train.txt', skip_header=1, delimiter=',', encoding='utf-8')
        test_features = np.genfromtxt('preprocessed_test.txt', skip_header=1, delimiter=',', encoding='utf-8')

    train_classifiers(np.array(training_features), np.array(test_features))


if __name__ == "__main__":
    main()
