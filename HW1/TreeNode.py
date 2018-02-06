#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode(object):
    """Build tree node
    """
    depth = -1

    def __init__(self, is_leaf=False, left=None, right=None, val=None, name=None, size=0):
        self.__isLeaf = is_leaf
        self.__left = left
        self.__right = right
        self.__val = val
        self.__name = name
        self.__no = -1
        self.__size = size


    def getLeft(self):
        return self.__left

    def setLeft(self, left):
        self.__left = left

    def getRight(self):
        return self.__right

    def setRight(self, right):
        self.__right = right

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def isLeaf(self):
        return self.__isLeaf

    def setLeaf(self, isLeaf):
        self.__isLeaf = isLeaf

    def getVal(self):
        return self.__val

    def setVal(self, val):
        self.__val = val

    def setNo(self, no):
        self.__no = no

    def getNo(self):
        return self.__no

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def printTree(self):
        TreeNode.depth += 1
        if (not self.isLeaf()):
            print('\n', end='')
            for i in range(TreeNode.depth):
                print('| ', end='')
            print('%s = 0 :' % self.getName(), end='')
        else:
            print(' %s' % self.getVal(), end='')

        if (self.getLeft()):
            self.getLeft().printTree()
            if self.isLeaf():
                print(' %s' % self.getVal(), end='')
            else:
                print('\n', end='')
                for i in range(TreeNode.depth):
                    print('| ', end='')
                print("%s = 1 :" % self.getName(), end='')

            self.getRight().printTree()

        TreeNode.depth -= 1