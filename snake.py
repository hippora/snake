'''
Created on 2009-4-12

@author: hippo
'''
from threading import *
from node import *
from properties import *

class SnakeException(Exception):
    def __init__(self, str):
        self._str = str
    def __str__(self):
        return repr(slef._str)

class Snake():
    '''
    snake's class
    
    x,y direct the position of the snake's head
    '''
    def __init__(self, x, y, length=3, speed=1):
        '''
        Constructor
        '''
        if length <= 0:
            self._length = 3
        self._length = length
        self._speed = speed
        self.body = list()
        # create the snake's body
        for i in range(self._length):
            self.body.append(Node(x, y + i, UP))
    def move(self):
        _t = self.body.pop()
        if self.body[0]._direct == UP:
            _t._x = self.body[0]._x
            _t._y = (self.body[0]._y - 1 + GRID_LEN) % GRID_LEN
        elif self.body[0]._direct == DOWN:
            _t._x = self.body[0]._x
            _t._y = (self.body[0]._y + 1 + GRID_LEN) % GRID_LEN
        elif self.body[0]._direct == LEFT:
            _t._x = (self.body[0]._x - 1 + GRID_LEN) % GRID_LEN
            _t._y = self.body[0]._y
        elif self.body[0]._direct == RIGHT:
            _t._x = (self.body[0]._x + 1 + GRID_LEN) % GRID_LEN
            _t._y = self.body[0]._y
        else:
            pass
        _t._direct = self.body[0]._direct
        self.body.insert(0, _t)
        self.display()
    def turn(self, direct):
        #print('snake turn to ' + direct)
        self.body[0]._changedirect(direct)
    def grow(self):
        ref = self.body[ - 1]
        _t = Node(0, 0, NONE)
        if ref._direct == UP:
            _t._x = ref._x
            _t._y = ref._y + 1
            _t._direct = DOWN
        elif ref._direct == DOWN:
            _t._x = ref._x
            _t._y = ref._y - 1
            _t._direct = UP
        elif ref._direct == LEFT:
            _t._x = ref._x + 1
            _t._y = ref._y
            _t._direct = RIGHT
        elif ref._direct == RIGHT:
            _t._x = ref._x - 1
            _t._y = ref._y
            _t._direct = LEFT
        else:
            pass
        self.body.append(_t)
    def display(self):
        print('-'*20)
        for i in self.body:
            print(i)