#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Information Gain'

from TreeNode import TreeNode


class InformationGainHeuristicDT():
    def buildDT(self, data_set, labels):
        # all results from class
        class_list = [item[-1] for item in data_set]

        # If all the results in class list equal, then just return
        if class_list.count(class_list[0]) == len(class_list):
            return TreeNode(class_list[0])


