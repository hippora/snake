'''
Created on 2009-4-15

@author: hippo
'''
from node import *

class Rock(Node):
    def __init__(self, x=None, y=None):
        if x is None or y is None:
            self.reset()
        else:
            self._x = x
            self._y = y
        self.color = '#101010'
        self.edgecolor = 'black'
    def reset(self):
        self._x = randint(0, GRID_LEN - 1)
        self._y = randint(0, GRID_LEN - 1)
        
    def __str__(self):
        return 'x=' + repr(self._x) + ',y=' + repr(self._y)
