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

def draw_obs(obstacles):
    for i in range(6):
        x = 100 + i * 120
        y = 75
        obstacle = Obstacle(x,y,sprites[2],3)
        obstacles.append(obstacle.obstacle)

    for i in range(6):
        x = 100 + i * 120
        y = 125
        obstacle = Obstacle(x,y,sprites[2],3)
        obstacles.append(obstacle.obstacle)

    for i in range(6):
        x = 100 + i * 120
        y = 175
        obstacle = Obstacle(x,y,sprites[1],2)
        obstacles.append(obstacle.obstacle)

    for i in range(6):
        x = 100 + i * 120
        y = 225
        obstacle = Obstacle(x,y,sprites[0],1)
        obstacles.append(obstacle.obstacle)

def draw():
    global game_status
    screen.blit("background.jpeg", (0,0))
    paddle.draw()
    ball.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for heart in hearts:
        heart.draw()


def update():
    global game_status,lives
    paddle.update()
    ball.update()

    if paddle.paddle.colliderect(ball.ball):
        ball.speed_y *= -1

    for obstacle in obstacles:
        if ball.ball.colliderect(obstacle):
            ball.speed_y *= -1
            obstacles.remove(obstacle)

    if ball.ball.y >= HEIGHT:
        lives -= 1
        ball.ball.x = 400
        ball.ball.y = 300
        ball.speed_x = 2
        ball.speed_y = -2
        hearts.pop()

    if lives == 0:
        game_status = 0
        obstacles.clear()
    if not obstacles and game_status != 0:
        game_status = 2

lives = 3
hearts = []
for i in range(lives):
    heart = Actor('heart.png')
    heart.x = 30 + i * 50
    heart.y = 25
    hearts.append(heart)

game_status = 1
paddle = Paddle(250, 450, 'paddle.png')
ball = Ball(300, 400, 'ball.png', 2, -2)
obstacles = []
sprites = ["greenwall.png","yellowwall.png","redwall.png"]
draw_obs(obstacles)

pgzrun.go()
