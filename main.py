import pgzrun
import pygame as pg

# Window options
TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 500


# Add Paddle class
class Paddle:
    def __init__(self, x, y, sprite):
        self.sprite = sprite
        self.paddle = Actor(sprite, anchor=(50, 0))
        self.paddle.x = x
        self.paddle.y = y

    def draw(self):
        self.paddle.draw()

    def update(self):
        # Check game status and hold position by cursor
        if game_status == 1:
            self.paddle.x = pg.mouse.get_pos()[0]
        elif game_status != 1:
            self.paddle.x = 0
        # Bouncing the ball from the collider
        if self.paddle.colliderect(ball.ball):
            ball.speed_y *= -1


class Ball:
    def __init__(self, x, y, sprite, speed_x, speed_y, speed):
        self.sprite = sprite
        self.ball = Actor(sprite)
        self.ball.x = x
        self.ball.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed = speed

    def draw(self):
        self.ball.draw()

    def update(self):
        global score_to_speed_up
        if game_status == 1:
            # Ball movement
            self.ball.x += self.speed_x * self.speed
            self.ball.y += self.speed_y * self.speed
            # Ball speed up every 300 points
            if self.speed <= 5:
                if score == score_to_speed_up:
                    self.speed = self.speed + 1
                    score_to_speed_up += 300
            # Bouncing off the borders
            if self.ball.x <= 0 or self.ball.x >= WIDTH:
                self.speed_x *= -1
            if self.ball.y <= 0:
                self.speed_y *= -1
        else:
            self.ball.x = 0


class Obstacle:
    def __init__(self, x, y, spritess, hits_to_destroy):
        self.obstacle = Actor(spritess)
        self.obstacle.x = x
        self.obstacle.y = y
        self.obstacle.hits_to_destroy = hits_to_destroy

    def draw(self):
        self.obstacle.draw()


# Function to create obstacles
def draw_obs():
    global obstacles, i
    for i in range(7):
        x = 70 + i * 110
        y = 75
        obstacle = Obstacle(x, y, sprites[2], 3)
        obstacles.append(obstacle)

    for i in range(7):
        x = 70 + i * 110
        y = 115
        obstacle = Obstacle(x, y, sprites[2], 3)
        obstacles.append(obstacle)

    for i in range(7):
        x = 70 + i * 110
        y = 155
        obstacle = Obstacle(x, y, sprites[1], 2)
        obstacles.append(obstacle)

    for i in range(7):
        x = 70 + i * 110
        y = 225
        obstacle = Obstacle(x, y, sprites[0], 1)
        obstacles.append(obstacle)

    for i in range(4):
        x = 70 + i * 220
        y = 265
        obstacle = Obstacle(x, y, sprites[1], 2)
        obstacles.append(obstacle)


def draw():
    global game_status, heart, score
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    screen.draw.text(f"Score: {score}", (700, 15), color=(255, 255, 255))
    screen.draw.text(f"Speed: {ball.speed}", (700, 30), color=(255, 255, 255))

    for obstacle in obstacles:
        obstacle.draw()
    for heart in hearts:
        heart.draw()

    if game_status == 0:
        screen.blit('gameover.png', (0, 0))

    if game_status == 2:
        screen.blit('win.png', (0, 0))


def update():
    global lives, game_status, score, score_to_speed_up
    paddle.update()
    ball.update()
    # Check hits to destroy obstacle and bouncing the ball
    for obstacle in obstacles:
        if ball.ball.colliderect(obstacle.obstacle):
            ball.speed_y *= -1
            obstacle.obstacle.hits_to_destroy -= 1
            if obstacle.obstacle.hits_to_destroy == 0:
                score += 50
                obstacles.remove(obstacle)
    # Loss of life in case of a miss
    if ball.ball.y >= HEIGHT:
        lives -= 1
        ball.ball.x = 400
        ball.ball.y = 300
        ball.speed_x = 2
        ball.speed_y = -2
        ball.speed = 2
        hearts.pop()

    if lives == 0:
        game_status = 0
        obstacles.clear()
    if not obstacles and game_status != 0:
        game_status = 2

    print(ball.speed)


# Creating lives
lives = 3
hearts = []
for i in range(lives):
    heart = Actor('heart.png')
    heart.x = 30 + i * 55
    heart.y = 35
    hearts.append(heart)

# Variables and initialization
game_status = 1
paddle = Paddle(250, 450, 'paddle.png')
ball = Ball(300, 400, 'ball.png', 2, -2, 5)
obstacles = []
sprites = ["greenwall.png", "yellowwall.png", "redwall.png"]
draw_obs()
score = 0
score_to_speed_up = 300

pgzrun.go()
