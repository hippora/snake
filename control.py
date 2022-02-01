"""
Created on 2009-4-13

@author: hippo
"""
from food import *
from rock import Rock
from snake import Snake

RUNNING = 'run'
DEAD = 'dead'
SUSPEND = 'suspend'


class Controller:
    """
    control snake's behaves,
    such as turn left,turn right etc.
    """

    def __init__(self):
        """
        init the controller,pass the snake to me!
        """
        # self.draw_screen = func_draw
        self.snake = Snake(GRID_LEN // 2, GRID_LEN // 2, 6)
        self.rocks = self._gen_rocks(ROCK_NUM)
        self.food = self._gen_food()
        self.status = RUNNING

    def _gen_rock(self):
        r = Rock()
        self._node_reset(r, self.snake.body)
        return r

    def _gen_rocks(self, num):
        rocks = []
        for i in range(num):
            rocks.append(self._gen_rock())
        return rocks

    def _gen_food(self):
        f = Food()
        self._node_reset(f, self.snake.body)
        self._node_reset(f, self.rocks)
        return f

    def _node_reset(self, node, ref_list):
        flag = False
        for i in ref_list:
            if node._x == i._x and node._y == i._y:
                flag = True
                break
        if flag:
            node.reset()
            self._node_reset(node, ref_list)

    #    def game_start(self):
    #        self.status = RUNNING
    #        if self.snake._speed > 0:
    #            self.snake_timer = SnakeTimer(0.1, self.snake_move)
    #            self.snake_timer.daemon = True
    #            self.snake_timer.start()

    def snake_up(self):
        self.snake.turn(UP)

    def snake_down(self):
        self.snake.turn(DOWN)

    def snake_left(self):
        self.snake.turn(LEFT)

    def snake_right(self):
        self.snake.turn(RIGHT)

    def snake_move(self):
        if self.status == DEAD:
            for i in self.snake.body:
                i.color = None
            return
        if self.status == SUSPEND:
            return

        self.snake.move()
        #       print('snake_move_start')
        #       the snake eat then food
        if self.food._x == self.snake.body[0]._x and self.food._y == self.snake.body[0]._y:
            self.snake.grow()
            self._node_reset(self.food, self.snake.body)
            self._node_reset(self.food, self.rocks)
        # detect the snake if touch itself
        for i in self.snake.body[1:]:
            if self.snake.body[0]._x == i._x and self.snake.body[0]._y == i._y:
                self.status = DEAD
                break
        # detect the snake if touch the rocks
        for i in self.rocks:
            if self.snake.body[0]._x == i._x and self.snake.body[0]._y == i._y:
                self.status = DEAD
                break
        # print('snake_move_stop')
        # draw the screen
        # self.draw_screen()

    def game_suspend_resume(self):
        if self.status == DEAD:
            return
        if self.status == RUNNING:
            self.status = SUSPEND
            return
        if self.status == SUSPEND:
            self.status = RUNNING
