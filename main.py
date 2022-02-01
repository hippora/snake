"""
Created on 2009-4-13

@author: hippo
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from control import *


class Game:
    def __init__(self):
        self.strike_enable = 1
        self._speed = 1
        self._root = Tk()
        self._root.title('Python Snake')
        self.ctrler = Controller()
        frm = ttk.Frame(self._root)
        frm.grid(row=0, column=1)
        self._cv = Canvas(self._root, width=AREA_X, height=AREA_X, bg=BKCOLOR)
        self._cv.grid(row=0, column=0)
        self._scale = Scale(frm, to=10, label='Speed', command=self._set_speed)
        self._scale.grid(row=0, column=0)
        #        self._button = tkinter.Button(frame, text='Suspend')
        #        self._button.grid(row=1, column=0)
        self._root.bind('<Key>', self._turn_snake)
        self._setmenu()
        self._drawgrid()
        self._root.mainloop()

    def _turn_snake(self, event):
        if not self.strike_enable:
            return
        if event.char.upper() == 'W':
            self.ctrler.snake_up()
        elif event.char.upper() == 'S':
            self.ctrler.snake_down()
        elif event.char.upper() == 'A':
            self.ctrler.snake_left()
        elif event.char.upper() == 'D':
            self.ctrler.snake_right()
        else:
            pass
        self.strike_enable = 0

    def _setmenu(self):
        menu_root = Menu(self._root)
        menu_game = Menu(menu_root, tearoff=NO)
        menu_game.add_command(label='New Game', command=self.start)
        menu_game.add_command(label='Suspend/Resume', command=self.suspend_resume)
        menu_game.add_separator()
        menu_game.add_command(label='Exit', command=self._root.destroy)
        menu_root.add_cascade(label='Game', menu=menu_game)
        menu_root.add_command(label='About', command=self.about)
        self._root.config(menu=menu_root)

    def _draw_static_node(self, node_list):
        bookmark = 'static'
        self._cv.delete(bookmark)
        for i in node_list:
            self._drawnode(i, bookmark)

    def _drawgrid(self):
        self._cv.create_rectangle(GRID_X * OFFSET, GRID_X * OFFSET,
                                  GRID_X * (GRID_LEN + OFFSET), GRID_X * (GRID_LEN + OFFSET))
        if DISPLAY_GRID:
            for i in range(OFFSET + 1, GRID_LEN + OFFSET):
                self._cv.create_line(GRID_X * OFFSET, GRID_X * i, GRID_X * (GRID_LEN + OFFSET), i * GRID_X,
                                     fill='#b0b0b0')
                self._cv.create_line(GRID_X * i, GRID_X * OFFSET, GRID_X * i, GRID_X * (GRID_LEN + OFFSET),
                                     fill='#b0b0b0')

    def _drawnode(self, node, bookmark):
        if not isinstance(node, Node):
            raise SnakeException('What''s this?')
        pos = (GRID_X * (node._x + OFFSET), GRID_X * (node._y + OFFSET),
               GRID_X * (node._x + OFFSET + 1), GRID_X * (node._y + OFFSET + 1))
        if isinstance(node, Food):
            self._cv.create_oval(pos, outline=node.edgecolor, fill=node.color, tags=bookmark)
        else:
            self._cv.create_rectangle(pos, outline=node.edgecolor, fill=node.color, tags=bookmark)

    def _drawall(self):
        bookmark = 'dynamic'
        self._cv.delete(bookmark)
        # draw the snake
        for i in self.ctrler.snake.body:
            self._drawnode(i, bookmark)
        # draw the food
        self._drawnode(self.ctrler.food, bookmark)
        # draw the rock

    def _set_speed(self, x):
        self._speed = x

    def _loop(self):
        self.ctrler.snake_move()
        self._drawall()
        self.strike_enable = 1
        self._cv.after(220 - 10 * int(self._speed), self._loop)
        print("speed=" + str(self._speed))

    def start(self):
        self._speed = self._scale.get()
        #   self._scale.set(0)
        self._draw_static_node(self.ctrler.rocks)
        self.strike_enable = 1
        self._loop()

    def suspend_resume(self):
        self.ctrler.game_suspend_resume()

    @staticmethod
    def about():
        messagebox.showwarning('About Python Snake', 'Powered by Hippo!')


if __name__ == '__main__':
    Game()
