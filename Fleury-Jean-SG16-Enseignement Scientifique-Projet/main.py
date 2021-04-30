#                                              PONG: By Jean Fleury
#                                            Touche: Haut = E, Bas = C
#                                              C'est un Jeu sans fin


import turtle
import os

# Fenetre
wn = turtle.Screen()
wn.title("Pong by Jean Fleury")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Reset Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.2
ball.dy = 1.2

# Score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Fonction de mouvement vers le haut du Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


# Fonction de mouvement vers le bas du Paddle A
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


# Fonction de mouvement vers le haut du Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)


# Fonction de mouvement vers le bas du Paddle B
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)


# Detection des touches pressees
wn.listen()
wn.onkeypress(paddle_a_up, "e")
wn.onkeypress(paddle_a_down, "c")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Mise a jour continue de la Fenetre
while True:
    wn.update()

    # Mouvement de la Balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Rebond sur les bordures
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay BouncePaddle.wav&")

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        os.system("afplay BouncePaddle.wav&")

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        os.system("afplay LoseALife.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        os.system("afplay LoseALife.wav&")

    # Rebond sur les Paddles
    if 330 < ball.xcor() < 340 and (paddle_b.ycor() + 63 > ball.ycor() > paddle_b.ycor() - 63):
        ball.setx(330)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if -340 > ball.xcor() > -350 and (paddle_a.ycor() + 63 > ball.ycor() > paddle_a.ycor() - 63):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # IA
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 85:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 85:
        paddle_b_down()
