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

def draw():
    global game_status
    screen.blit("background.jpeg", (0,0))
    paddle.draw()

def update():
    paddle.update()


game_status = 1
paddle = Paddle(250, 450, 'paddle.png')

pgzrun.go()
