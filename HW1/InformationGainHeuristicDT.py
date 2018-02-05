#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Information Gain'

from TreeNode import TreeNode
from Utilities import Utilities


class InformationGainHeuristicDT(object):
    def buildDT(self, data_set, labels):

        if len(data_set) == 0:
            return None
        # all results from class
        class_list = [item[-1] for item in data_set]

        # If all the results in class list are '1' or '0', then just return
        if class_list.count(class_list[0]) == len(class_list):
            # return TreeNode(isLeaf=True, val=class_list[0])
            return class_list[0]

        best_classifier_index = Utilities.getBestClassifier(data_set, labels)
        best_classifier = labels[best_classifier_index]

        labels.remove(best_classifier)

        map_after_split = Utilities.splitDataSet(data_set, best_classifier_index)

        left = self.buildDT(map_after_split.get('0'), labels.copy())

        right = self.buildDT(map_after_split.get('1'), labels.copy())

        return TreeNode(isLeaf=False, left=left, right=right, name=best_classifier)





