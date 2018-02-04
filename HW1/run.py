#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'run decision tree'

import sys

from ReadData import ReadData
from InformationGainHeuristicDT import InformationGainHeuristicDT

# data_set name
data_set = 'data_sets1'


def main(args):
    # judge input arguments length
    if (len(args) != 6):
        print('Should Have Six Input Arguments')
        exit(0)

    # input parameters
    L = int(args[0])
    K = int(args[1])
    training_set_file_name = args[2]
    validation_set_file_name = args[3]
    test_set_file_name = args[4]
    to_print = True if args[5].lower() == 'true' else False

    path = './' + data_set + '/'

    # read data from training set, test set, and validation set
    rd = ReadData()
    labels, training_set = rd.createDataSet(path + training_set_file_name)
    labels, validation_set = rd.createDataSet(path + validation_set_file_name)
    lables, test_set = rd.createDataSet(path + test_set_file_name)

    # build tree
    information_gain_tree = InformationGainHeuristicDT()
    information_gain_tree.buildDT(training_set, labels)


if __name__ == "__main__":
    main(sys.argv[1:])
