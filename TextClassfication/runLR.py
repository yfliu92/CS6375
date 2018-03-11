#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Description'

__author__ = 'LIU'

import sys
from LogisticRegression import LogisticRegression


def main(_lambda, iterations, use_stop_words):
    lr = LogisticRegression(_lambda, iterations, use_stop_words)
    lr.train()

    spam_success_ratio, ham_success_ratio, total_success_ratio = lr.classify()

    print('Success Ratio For Spam Emails: %.4f%%' % (spam_success_ratio * 100))
    print('Success Ratio For Ham Emails: %.4f%%' % (ham_success_ratio * 100))
    print('Success Ratio For All Emails: %.4f%%' % (total_success_ratio * 100))

if __name__ == "__main__":
    use_stop_words = True if sys.argv[3].lower() == 'true' else False
    _lambda = sys.argv[1]
    iterations = sys.argv[2]
    main(float(_lambda), int(iterations), use_stop_words)
