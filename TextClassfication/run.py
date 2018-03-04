#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'LIU'

from NaiveBayesClassifier import NaiveBayesClassifier


def main():
    bc = NaiveBayesClassifier()
    spam_total_count, ham_total_count = bc.train()

    spam_success_ratio, ham_success_ratio = bc.classify(spam_total_count, ham_total_count)
    print(spam_success_ratio)
    print(ham_success_ratio)


if __name__ == "__main__":
    main()
