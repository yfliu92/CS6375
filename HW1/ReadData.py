#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Read data from CSV file'

import csv


class ReadData(object):

    def createDataSet(self, file_name):
        """Read data from CSV file.

        Args:
            file_name: the name of file needed to be load

        Returns:
            labels: a list contains all the attributes names.
            ret: a list contains all the values

        """

        with open(file_name) as f:
            reader = csv.reader(f)
            data = list(reader)

            labels = data[0]
            ret = data[1:]
            return labels, ret
