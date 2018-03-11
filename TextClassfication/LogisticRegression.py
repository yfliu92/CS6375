#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Description'

__author__ = 'LIU'

import os
import math


class LogisticRegression:
    TRAIN_PATH = 'train'
    TEST_PATH = 'test'
    learning_rate = 0.001
    WEIGHTS = {}

    def __init__(self, _lambda, iterations, use_stop_words):
        self.ham_words_map = {}
        self.spam_words_map = {}
        self.map_list = []
        self.class_list = []
        self.words_space_set = None
        self.stop_words = []
        self.use_stop_words = bool(use_stop_words)

        self._lambda = _lambda
        self.iterations = iterations

    def train(self):
        spam_count, spam_list = self.initList(self.TRAIN_PATH + '/spam')
        ham_count, ham_list = self.initList(self.TRAIN_PATH + '/ham')

        self.words_space_set = set(spam_list + ham_list)

        # delete empty string
        if '' in self.words_space_set:
            self.words_space_set.remove('')

        # use stop_words
        if self.use_stop_words:
            self.stop_words = self.readStopWords()
            for word in self.stop_words:
                if word in self.words_space_set:
                    self.words_space_set.remove(word)

        self.WEIGHTS['zero'] = 0.0
        for i in self.words_space_set:
            self.WEIGHTS[i] = 0.0

        self.initMapList(self.TRAIN_PATH + '/spam', 'spam')
        self.initMapList(self.TRAIN_PATH + '/ham', 'ham')

        for ite in range(self.iterations):
            print('iteration %d' % (ite))
            for word in self.WEIGHTS:
                sum = 0.0
                for i in range(len(self.class_list)):
                    instance = self.map_list[i]

                    if word in instance:
                        class_name = self.class_list[i]
                        y_val = 1 if class_name == 'spam' else 0
                        prob = self.cal(instance, 'spam')
                        sum += float(instance[word] * (y_val - prob))

                self.WEIGHTS[word] += (
                        self.learning_rate * sum - float(self._lambda) * self.learning_rate * self.WEIGHTS[word])

    def classify(self):

        spam_count, spam_list = self.initList(self.TEST_PATH + '/spam')
        ham_count, ham_list = self.initList(self.TEST_PATH + '/ham')

        # clear train data
        self.class_list = []
        self.map_list = []
        self.words_space_set = None

        self.words_space_set = set(spam_list + ham_list)

        # delete empty string
        if '' in self.words_space_set:
            self.words_space_set.remove('')

        # use stop_words
        if self.use_stop_words:
            self.stop_words = self.readStopWords()
            for word in self.stop_words:
                if word in self.words_space_set:
                    self.words_space_set.remove(word)

        self.initMapList(self.TEST_PATH + '/spam', 'spam')
        self.initMapList(self.TEST_PATH + '/ham', 'ham')

        spam_success = 0
        ham_success = 0
        total_success = 0

        for i in range(len(self.class_list)):
            instance = self.map_list[i]
            class_name = self.class_list[i]
            return_type = self.judgeMailType(instance)
            if return_type == class_name:
                total_success += 1
                if class_name == 'spam':
                    spam_success += 1
                else:
                    ham_success += 1

        spam_success_ratio = spam_success * 1.0 / spam_count
        ham_success_ratio = ham_success * 1.0 / ham_count
        total_success_ratio = total_success * 1.0 / (spam_count + ham_count)

        return spam_success_ratio, ham_success_ratio, total_success_ratio

    def judgeMailType(self, instance):
        spam_prop = self.cal(instance, 'spam')
        ham_prop = 1 - spam_prop
        if spam_prop > ham_prop:
            return 'spam'
        else:
            return 'ham'

    # calculate weight
    def cal(self, instance, class_name):
        weight = self.WEIGHTS['zero']

        for word in instance:
            if word not in self.WEIGHTS:
                self.WEIGHTS[word] = 0.0
            weight += self.WEIGHTS[word] * float(instance[word])

        exp_weight = math.exp(float(weight))

        sigmoid = exp_weight / (1 + exp_weight)

        return sigmoid if class_name == 'spam' else (1 - sigmoid)

    def initList(self, folder):
        file_content = os.listdir(folder)

        if not file_content:
            return

        msg = []
        for file_name in file_content:
            with open(folder + '/' + file_name, 'r', encoding='utf-8', errors='ignore') as f:
                temp = f.read().lower().replace('\n', ' ').split(' ')
                msg = msg + temp

        return len(file_content), msg

    def initMapList(self, folder, class_type):
        file_content = os.listdir(folder)

        if not file_content:
            return

        for file_name in file_content:
            tempMap = {}
            with open(folder + '/' + file_name, 'r', encoding='utf-8', errors='ignore') as f:
                temp = f.read().lower().replace('\n', ' ').split(' ')
                for word in temp:
                    if word in self.words_space_set:
                        if word not in tempMap:
                            tempMap[word] = 0
                        tempMap[word] += 1

            self.map_list.append(tempMap)
            self.class_list.append(class_type)

    def readStopWords(self):
        with open('stop_words.txt') as f:
            temp = f.read().lower().replace('\n', ' ').split(' ')

        return temp
