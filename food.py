"""
Created on 2009-4-13

@author: hippo
"""

from node import *


class Food(Node):
    def __init__(self):
        super(Food, self).__init__(0,0)
        self.reset()
        self.color = 'red'
        self.edgecolor = 'black'

    def __str__(self):
        return 'x=' + repr(self._x) + ',y=' + repr(self._y)
