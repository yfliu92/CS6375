#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'LIU'

from NaiveBayesClassifier import NaiveBayesClassifier
import sys

def main(use_stop_words):
    bc = NaiveBayesClassifier(use_stop_words)
    spam_total_count, ham_total_count = bc.train()

    spam_success_ratio, ham_success_ratio, total_success_ratio = bc.classify(spam_total_count, ham_total_count)
    print('Success Ratio For Spam Emails: %.4f%%' %(spam_success_ratio*100))
    print('Success Ratio For Ham Emails: %.4f%%' %(ham_success_ratio*100))
    print('Success Ratio For All Emails: %.4f%%' %(total_success_ratio*100))


if __name__ == "__main__":
    use_stop_words = True if sys.argv[1].lower() == 'true' else False
    main(use_stop_words)
