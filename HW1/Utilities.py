#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Utilities Module'

import math
import operator


class Utilities(object):
    @staticmethod
    def getBestClassifier(data_set, labels, used_labels):

        bestClassifier = None

        # get data map, key: attribute, value: list contains all corresponding values
        data_map = Utilities.getDataMap(data_set, labels, used_labels)
        # get all values of 'Class'
        class_values = data_map['Class']

        total = [class_values.count('0'), class_values.count('1')]
        # map to store information gain for every attribute
        info_gain_map = {}

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
            info_gain_map[labels[i]] = info_gain

        # sort map with values in descending order
        sorted_info_gain_map = sorted(info_gain_map.items(), key=operator.itemgetter(1), reverse=True)

        return sorted_info_gain_map[0][0]

    @staticmethod
    def getDataMap(data_set, labels, used_labels):
        map = {}
        for i, label in enumerate(labels):

            if label in used_labels: continue

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
        ret = {}
        for row in data_set:
            if row[index] == '1':
                if '1' in ret:
                    ret['1'].append(row)
                else:
                    ret['1'] = [row]

            else:
                if '0' in ret:
                    ret['0'].append(row)
                else:
                    ret['0'] = [row]

        return ret
