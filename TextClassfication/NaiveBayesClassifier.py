#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math


class NaiveBayesClassifier:
    TRAIN_PATH = 'train'
    TEST_PATH = 'test'

    def __init__(self, use_stop_words):
        self.ham_words_map = {}
        self.spam_words_map = {}
        self.words_space_set = None
        self.ham_count = 0
        self.spam_count = 0
        self.stop_words = []
        self.use_stop_words = use_stop_words

    def train(self):
        self.spam_count, spam_list = self.initList(self.TRAIN_PATH + '/spam')
        self.ham_count, ham_list = self.initList(self.TRAIN_PATH + '/ham')

        # delete empty string
        if '' in spam_list:
            spam_list.remove('')

        if '' in ham_list:
            ham_list.remove('')

        if self.use_stop_words:
            self.stop_words = self.readStopWords()
            for word in self.stop_words:
                if word in spam_list:
                    spam_list.remove(word)
                if word in ham_list:
                    ham_list.remove(word)

        spam_words_len = len(spam_list)
        ham_words_len = len(ham_list)

        self.words_space_set = set(spam_list + ham_list)
        words_space_len = len(self.words_space_set)

        self.ham_words_map = self.initMap(ham_list)
        self.spam_words_map = self.initMap(spam_list)

        spam_total_count = spam_words_len + words_space_len
        ham_total_count = ham_words_len + words_space_len

        # p_ham = self.ham_count * 1.0 / (self.ham_count + self.spam_count)
        # p_spam = self.spam_count * 1.0 / (self.ham_count + self.spam_count)

        for word in self.ham_words_map.keys():
            self.ham_words_map[word] = math.log2((self.ham_words_map[word] + 1) * 1.0 / ham_total_count)

        for word in self.spam_words_map.keys():
            self.spam_words_map[word] = math.log2((self.spam_words_map[word] + 1) * 1.0 / spam_total_count)

        return spam_total_count, ham_total_count

    def classify(self, spam_total_count, ham_total_count):

        # spam
        file_content = os.listdir(self.TEST_PATH + '/spam')

        if not file_content:
            return

        test_spam_count = len(file_content)
        after_classify_spam = 0

        for file_name in file_content:
            with open(self.TEST_PATH + '/spam' + '/' + file_name, 'r', encoding='utf-8', errors='ignore') as f:
                temp = f.read().lower().replace('\n', ' ').split(' ')

            ham_prop = math.log2(self.ham_count * 1.0 / (self.ham_count + self.spam_count))
            spam_prop = math.log2(self.spam_count * 1.0 / (self.ham_count + self.spam_count))

            # delete empty string
            if '' in temp:
                temp.remove('')
            # delete stop_words from list
            if self.use_stop_words:
                for word in self.stop_words:
                    if word in temp:
                        temp.remove(word)

            for word in temp:
                if word in self.spam_words_map:
                    spam_prop += self.spam_words_map[word]
                else:
                    spam_prop += math.log2(1 / spam_total_count)

                if word in self.ham_words_map:
                    ham_prop += self.ham_words_map[word]
                else:
                    ham_prop += math.log2(1 / ham_total_count)

            if spam_prop >= ham_prop:
                after_classify_spam += 1

        spam_success_ratio = after_classify_spam * 1.0 / test_spam_count

        # ham
        file_content = os.listdir(self.TEST_PATH + '/ham')

        if not file_content:
            return

        test_ham_count = len(file_content)
        after_classify_ham = 0

        for file_name in file_content:
            with open(self.TEST_PATH + '/ham' + '/' + file_name, 'r', encoding='utf-8', errors='ignore') as f:
                temp = f.read().lower().replace('\n', ' ').split(' ')

            # delete empty string
            if '' in temp:
                temp.remove('')

            ham_prop = math.log2(self.ham_count * 1.0 / (self.ham_count + self.spam_count))
            spam_prop = math.log2(self.spam_count * 1.0 / (self.ham_count + self.spam_count))

            # delete stop_words from list
            if self.use_stop_words:
                for word in self.stop_words:
                    if word in temp:
                        temp.remove(word)

            for word in temp:
                if word in self.spam_words_map:
                    spam_prop += self.spam_words_map[word]
                else:
                    spam_prop += math.log2(1 / spam_total_count)

                if word in self.ham_words_map:
                    ham_prop += self.ham_words_map[word]
                else:
                    ham_prop += math.log2(1 / ham_total_count)

            if spam_prop <= ham_prop:
                after_classify_ham += 1

        ham_success_ratio = after_classify_ham * 1.0 / test_ham_count

        total_success_ratio = (after_classify_spam + after_classify_ham) * 1.0 / (test_spam_count + test_ham_count)

        return spam_success_ratio, ham_success_ratio, total_success_ratio


    def initMap(self, words_list):
        temp = {}
        for word in words_list:
            if word in temp:
                temp[word] += 1
            else:
                temp[word] = 0

        return temp

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

    def readStopWords(self):
        with open('stop_words.txt') as f:
            temp = f.read().lower().replace('\n', ' ').split(' ')

        return temp
