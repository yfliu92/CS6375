#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Information Gain'

from TreeNode import TreeNode
from Utilities import Utilities


class InformationGainHeuristicDT(object):
    def buildDT(self, data_set, labels):

        if len(data_set) == 0:
            return None

        # data_set contains only 'Class' values
        if len(data_set[0]) == 1 and labels[0] == 'Class':
            return TreeNode(is_leaf=True, val=Utilities.getMajorityValue(data_set))
        # all results from class
        class_list = [item[-1] for item in data_set]

        # If all the results in class list are '1' or '0', then just return
        if class_list.count(class_list[0]) == len(class_list):
            return TreeNode(is_leaf=True, val=class_list[0])

        best_classifier_index = Utilities.getBestClassifierByEntropy(data_set, labels)
        best_classifier = labels[best_classifier_index]

        labels.remove(best_classifier)

        map_after_split = Utilities.splitDataSet(data_set, best_classifier_index)

        left = self.buildDT(map_after_split.get('0'), labels.copy())

        right = self.buildDT(map_after_split.get('1'), labels.copy())

        return TreeNode(is_leaf=False, left=left, right=right, name=best_classifier)
