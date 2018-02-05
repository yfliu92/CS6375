#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    """Build tree node
    """

    def __init__(self, isLeaf=False, left=None, right=None, val=None, name=None):
        self.__isLeaf = isLeaf
        self.__left = left
        self.__right = right
        self.__val = val
        self.__name = name

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getName(self):
        return self.__name

    def isLeaf(self):
        return self.__isLeaf

    def getVal(self):
        return self.__val
