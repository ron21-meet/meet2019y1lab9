import turtle
import time
text = turtle.Turtle()
turtle.shape("arrow")
turtle.hideturtle()
turtle.penup()
turtle.goto(150,100)
go = ["blue", "green", "red", "yellow", "orange"]
quests = ["quest"]
answer = ["true"]
turtle.bgcolor("blue")
global x
x = 0
global quest
quest = "38"
global y
y = -1
text.write(quests[0])

def background():
    global x
    global y
    if quest == "false":
        a=go[x+1]
        turtle.bgcolor(a)
        x += 1
    if quest == "true":
        turtle.showturtle()
        time.sleep(3)
        turtle.hideturtle()
        
def right():
    global y
    quest = "true"
    if quest == answer[y+1]:
        y += 1
        background()
    else:
        y += 1
        background()


def left():
    global y
    quest = "false"
    if quest == answer[y+1]:
        y += 1
        background()
    else:
        y += 1
        background()

def true():
    global quest
    quest = "true"
    background()

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()


def false():
    global quest
    quest = "0"
    background()


turtle.done()
