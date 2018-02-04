#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Information Gain'

from TreeNode import TreeNode
from Utilities import Utilities


class InformationGainHeuristicDT(object):
    def buildDT(self, data_set, labels, used_labels):
        # all results from class
        class_list = [item[-1] for item in data_set]

        # If all the results in class list are '1' or '0', then just return
        if class_list.count(class_list[0]) == len(class_list):
            return TreeNode(class_list[0])

        classifier = Utilities.getBestClassifier(data_set, labels, used_labels)

        used_labels.append(classifier)

        map_after_split = Utilities.splitDataSet(data_set, labels.index(classifier))

        new_labels = labels.copy()
        new_labels.remove(classifier)
        print(classifier)


