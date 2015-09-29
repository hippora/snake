<<<<<<< HEAD
'''
Created on 2009-4-13

@author: hippo
'''
from node import *
from properties import *
from random import randint
from snake import Snake

class Food(Node):
    def __init__(self):
        self.reset() 
        self.color = 'red'
        self.edgecolor = 'black'
    def __str__(self):
        return 'x=' + repr(self._x) + ',y=' + repr(self._y)
=======
'''
Created on 2009-4-13

@author: hippo
'''
from node import *
from properties import *
from random import randint
from snake import Snake

class Food(Node):
    def __init__(self):
        self.reset() 
        self.color = 'red'
        self.edgecolor = 'black'
    def __str__(self):
        return 'x=' + repr(self._x) + ',y=' + repr(self._y)
>>>>>>> f142e28e7d811fcb550dd728c31323dc931357dd
