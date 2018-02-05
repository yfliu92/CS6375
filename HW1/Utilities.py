#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Utilities Module'

import math
import operator


class Utilities(object):
    @staticmethod
    def getBestClassifier(data_set, labels):

        # get data map, key: attribute, value: list contains all corresponding values
        data_map = Utilities.getDataMap(data_set, labels)
        # get all values of 'Class'
        class_values = data_map['Class']

        total = [class_values.count('0'), class_values.count('1')]

        max_info_gain = 0.0
        best_classifier_index = -1

        for i in range(len(labels) - 1):

            values = data_map[labels[i]]
            one = [0, 0]
            zero = [0, 0]
            for index, val in enumerate(values):
                if val == '1':
                    if class_values[index] == '1':
                        one[1] += 1
                    else:
                        one[0] += 1
                else:
                    if class_values[index] == '1':
                        zero[1] += 1
                    else:
                        zero[0] += 1

            info_gain = Utilities.calEntropyGain(total, zero, one)

            if info_gain > max_info_gain:
                max_info_gain = info_gain
                best_classifier_index = i

        return best_classifier_index

    @staticmethod
    def getDataMap(data_set, labels):
        map = {}
        for i, label in enumerate(labels):
            for row in data_set:
                if label in map:
                    map[label].append(row[i])
                else:
                    map[label] = [row[i]]

        return map

    @staticmethod
    def calEntropy(negative, positive):
        total = positive + negative
        if positive == negative:
            return 1
        if positive == 0 or negative == 0:
            return 0
        entropy = -(positive / total) * math.log2(positive / total) - (negative / total) * math.log2(negative / total)
        return entropy

    @staticmethod
    def calEntropyGain(total, zero, one):
        total_count = total[0] + total[1]
        total_entropy = Utilities.calEntropy(total[0], total[1])

        one_count = one[0] + one[1]
        one_entropy = Utilities.calEntropy(one[0], one[1])

        zero_count = zero[0] + zero[1]
        zero_entropy = Utilities.calEntropy(zero[0], zero[1])

        info_gain = total_entropy - (one_count / total_count) * one_entropy - (zero_count / total_count) * zero_entropy
        return info_gain

    @staticmethod
    def splitDataSet(data_set, index):
        ret = {
            '0': [],
            '1': []
        }
        for row in data_set:
            reduced_row = row[:index]
            reduced_row.extend(row[index + 1:])
            ret[row[index]].append(reduced_row)
        return ret
