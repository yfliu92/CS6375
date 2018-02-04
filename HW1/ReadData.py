#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Read data from CSV file'

import csv


class ReadData():
    def createDataSet(self, fileName):
        with open(fileName) as f:
            reader = csv.reader(f)
            data = list(reader)

            labels = data[0]
            ret = data[1:]
            return labels, ret
