import turtle
import random
import emojis
from turtle import *

#----------------- Functions ----------------------
def square(y_axis):  #function for a square
    middleLine = turtle.Turtle()
    middleLine.penup()
    middleLine.goto(0, y_axis)
    middleLine.shape("square")
    middleLine.shapesize(stretch_wid=0.50, stretch_len=0.50)


def result_box():  #function for a rectangle
    result.shape("square")
    result.color("yellow")
    result.shapesize(stretch_wid=3, stretch_len=6)


#-------------- Global Variables--------------------

SCREEN_HEIGHT = 127  #starting height of the screen
player1_score = 0  #starting score of player1
player2_score = 0  #starting score of player2

#--------------------- Setup------------------------
#Screen Size
screen = turtle.Screen()
screen.setup(width=540, height=350)  #screen size
screen.colormode(255)
screen.bgcolor(227, 238, 250)  #color for background

# Welcome Message 
welcome_message = emojis.encode(
    "Welcome to the Pong Game by Team Chillcoders! :ping_pong: :smile: :heart:"
)
print(welcome_message)

title("Pong!")
#Border
border = turtle.Turtle()
border.penup()
border.goto(235, 150)
border.shape("square")
border.shapesize(stretch_wid=1, stretch_len=60)

border2 = turtle.Turtle()
border2.penup()
border2.goto(235, -150)
border2.shape("square")
border2.shapesize(stretch_wid=1, stretch_len=60)

#Scores
scores = turtle.Turtle()
scores.color("black")
scores.penup()
scores.goto(0, 115)
scores.write("Player1:  0 \t\t Player2:  0", align="center")

#Middleline
for i in range(12):  #to have 8 squares
    square(SCREEN_HEIGHT)
    SCREEN_HEIGHT -= 25

# Paddle Base
paddle1 = turtle.Turtle()
paddle2 = turtle.Turtle()

#Result of the Winner
result = turtle.Turtle()  #Box
result_text = turtle.Turtle()  #Text

# Paddle 1
paddle1.penup()
paddle1.shape("square")
paddle1.color("pink")
paddle1.setpos(-200, 0)
paddle1.shapesize(stretch_wid=None, stretch_len=None, outline=None)
paddle1.shapesize(stretch_wid=0.68, stretch_len=3.5)

# Paddle 2
paddle2.penup()
paddle2.setpos(200, 0)
paddle2.shape("square")
paddle2.color("pink")
paddle2.shapesize(stretch_wid=None, stretch_len=None, outline=None)
paddle2.shapesize(stretch_wid=0.68, stretch_len=3.5)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.penup()
ball.dx = 3
ball.dy = -3

#Moving Paddles
def k1():
    paddle1.forward (45)

def k2():
    paddle1.back(45)

def k3():
    paddle2.forward (45)

def k4():
    paddle2.back(45)

paddle1.left(90)
paddle2.right(90)

onkeypress(k1, "w")
onkeypress(k2, "s")
onkeypress(k3, "Down")
onkeypress(k4, "Up")

listen()

#Moving the Ball 

while player1_score < 10 and player2_score < 10:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking borders 
    if ball.ycor() > 120:
        ball.sety(90)
        ball.dy *= -1

    if ball.ycor() < -120:
        ball.sety(-90)
        ball.dy *= -1

    if ball.xcor() > 230:
        ball.goto(0, 0)
        ball.dx *= -1

        player1_score += 1  #Adding point for player1
        scores.clear()
        scores.write("Player1:  {} \t\t Player2:  {}".format(
            str(player1_score), str(player2_score)),
                     align="center")

    if ball.xcor() < -230:
        ball.goto(0, 0)
        ball.dx *= -1

        player2_score += 1  #Adding point for player2
        scores.clear()
        scores.write("Player1:  {} \t\t Player2:  {}".format(
            str(player1_score), str(player2_score)),
                     align="center")

# Ball color change 
    randomR = random.randint(0, 255)
    randomG = random.randint(0, 255)
    randomB = random.randint(0, 255)

    # Paddle and Ball Collisions - 
    if (ball.xcor() > 170 and ball.ycor() < 180) and (ball).ycor(
    ) < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40:
        ball.setx(170)
        ball.dx *= -1
        ball.color(randomR, randomG, randomB)

    if (ball.xcor() < -170 and ball.ycor() > -180) and (ball).ycor(
    ) < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40:
        ball.setx(-170)
        ball.dx *= -1
        ball.color(randomR, randomG, randomB)

#Displays the Winner
if player1_score > player2_score:
    result_box()
    result_text.write("Player1 Win", align="center")
else:
    result_box()
    result_te
