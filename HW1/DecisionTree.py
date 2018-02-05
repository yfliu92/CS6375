#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Variance Impurity Gain'

from TreeNode import TreeNode
from Utilities import Utilities


class DecisionTree(object):
    def buildDT(self, data_set, labels, method):

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

        if method == 'information_gain':
            best_classifier_index = Utilities.getBestClassifierByEntropy(data_set, labels)
        else:
            best_classifier_index = Utilities.getBestClassifierByVariance(data_set, labels)
        best_classifier = labels[best_classifier_index]

        labels.remove(best_classifier)

        map_after_split = Utilities.splitDataSet(data_set, best_classifier_index)

        left = self.buildDT(map_after_split.get('0'), labels.copy(), method)

        right = self.buildDT(map_after_split.get('1'), labels.copy(), method)

        return TreeNode(is_leaf=False, left=left, right=right, name=best_classifier)


    def calAccuracy(self, data_set, node, labels):
        count = 0
        for row in data_set:
            if self.checkOutput(row, node, labels):
                count += 1

        return count / len(data_set) * 100


    def checkOutput(self, row, node, labels):
        result = row[-1]
        head = node
        while (True):
            if head.isLeaf():
                if head.getVal() == result:
                    return True
                else:
                    return False
            else:
                idx = labels.index(head.getName())
                if row[idx] == '0':
                    head = head.getLeft()
                else:
                    head = head.getRight()
