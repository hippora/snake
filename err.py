"""
Created on 2021-2-4

@author: hippo
"""


class SnakeException(Exception):
    def __init__(self, errmsg):
        self._str = errmsg

    def __str__(self):
        return repr(self._str)
