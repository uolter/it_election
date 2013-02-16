__author__ = 'uolter'

import random


def divide_data(data, test=0.05):
    # divide the training set for Cross Validation
    trainset = []
    testset = []

    for row in data:
        if random.random() < test:
            testset.append(row)
        else:
            trainset.append(row)

    return trainset, testset
