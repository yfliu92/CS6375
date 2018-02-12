#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Build Tree Using Variance Impurity Gain'

from TreeNode import TreeNode
from Utilities import Utilities
import random
from collections import deque


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
            return TreeNode(is_leaf=True, val=class_list[0], size=len(class_list))

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

    def pruneTree(self, root, L, K, data, labels):
        best = self.copyTree(root)
        accuracy = self.calAccuracy(data, best, labels)
        for i in range(L):
            d_quotation = self.copyTree(root)
            M = random.randint(1, K)
            for j in range(M):
                N = self.calNonLeafCount(d_quotation)
                if N > 1:
                    P = random.randint(1, N)
                    self.replaceSubtree(d_quotation, P)

            accuracy_of_d_quotation = self.calAccuracy(data, d_quotation, labels)

            if accuracy < accuracy_of_d_quotation:
                best = d_quotation
                accuracy = accuracy_of_d_quotation
        return best

    def replaceSubtree(self, node, P):
        if not node.isLeaf():
            if node.getNo() == P:
                node.setLeaf(True)
                node.setVal(self.getMajorityClass(node))
                node.setLeft(None)
                node.setRight(None)
            else:
                self.replaceSubtree(node.getLeft(), P)
                self.replaceSubtree(node.getRight(), P)

    def getMajorityClass(self, root):
        size0 = 0
        size1 = 0
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node:
                if node.isLeaf():
                    if node.getVal() == '0':
                        size0 += node.getSize()
                    else:
                        size1 += node.getSize()
                else:
                    dq.append(node.getLeft())
                    dq.append(node.getRight())

        return '0' if size0 > size1 else '1'

    def copyTree(self, old):
        new = TreeNode()
        if old.isLeaf():
            new.setLeaf(True)
            new.setVal(old.getVal())
        else:
            new.setName(old.getName())
            if old.getLeft():
                new.setLeft(self.copyTree(old.getLeft()))

            if old.getRight():
                new.setRight(self.copyTree(old.getRight()))

        return new

    # use BFS to calculate the count of non-leaf node in tree
    def calNonLeafCount(self, root):
        count = 0
        dq = deque()
        dq.append(root)
        while dq:
            temp = dq.popleft()
            if not temp.isLeaf():
                count += 1
                temp.setNo(count)

                if temp.getLeft():
                    dq.append(temp.getLeft())

                if temp.getRight():
                    dq.append(temp.getRight())

        return count

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
