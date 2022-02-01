"""
Created on 2009-4-13

@author: hippo
"""
from random import randint
from properties import *
from err import SnakeException

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
NONE = 'none'

def _setcolor():
    if COLORFUL:
        return '#%02x%02x%02x' % (randint(0, 255), randint(0, 255), randint(0, 255))
    return BODY_COLOR

class Node:
    def __init__(self, x, y, direct=None):
        if direct is not None:
            if direct not in (UP, DOWN, LEFT, RIGHT, NONE):
                raise SnakeException('The snake don''t know how to move!')
        self._direct = direct
        self._x = x
        self._y = y
        self.color = _setcolor()
        self.edgecolor = 'black'

    def reset(self):
        self._x = randint(0, GRID_LEN - 1)
        self._y = randint(0, GRID_LEN - 1)

    def _changedirect(self, direct):
        _map = {UP: -1, DOWN: 1, LEFT: -2, RIGHT: 2, NONE: 0}
        if _map[self._direct] + _map[direct]:
            self._direct = direct

    def __str__(self):
        return 'x=' + repr(self._x) + ',y=' + repr(self._y) + ',direct=' + repr(self._direct)
