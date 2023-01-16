import pgzrun
import pygame as pg

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 500

class Paddle:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.paddle = Actor(sprite)
        self.paddle.x = x
        self.paddle.y = y

    def draw(self): self.paddle.draw()

    def update(self):
        if game_status == 1:
            self.paddle.x = pg.mouse.get_pos()[0]
        else:
            self.paddle.x = 1000

class Ball:
    def __init__(self, x, y, sprite, speed_x, speed_y):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.ball = Actor(sprite)
        self.ball.x = x
        self.ball.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self): self.ball.draw()

    def update(self):
        if game_status == 1:
            self.ball.x += self.speed_x * 2
            self.ball.y += self.speed_y * 2

            if self.ball.x <= 0 or self.ball.x >= WIDTH:
                self.speed_x *= -1
            if self.ball.y <= 0:
                self.speed_y *= -1
        else: self.ball.x = 1000

class Obstacle:
    def __init__(self, x, y, sprites ,hits_to_destroy):
        self.x = x
        self.y = y
        self.obstacle = Actor(sprites)
        self.obstacle.x = x
        self.obstacle.y = y
        self.obstacle.hitstodestroy = hits_to_destroy

    def draw(self):
        self.obstacle.draw()


def draw():
    global game_status
    screen.blit("background.jpeg", (0,0))
    paddle.draw()
    ball.draw()
#   for obstacle in obstacles:
#       obstacle.draw()

def update():
    paddle.update()
    ball.update()

game_status = 1
paddle = Paddle(250, 450, 'paddle.png')
ball = Ball(300, 400, 'ball.png', 2, -2)
obstacles = []
sprites = ["greenwall.png","yellowwall.png","redwall.png"]

pgzrun.go()
