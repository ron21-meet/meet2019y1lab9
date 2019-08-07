import turtle
import time
from pygame import mixer
turtle.setup(640,400)
mixer.init()
mixer.music.load("bob.mp3")
mixer.music.play()
text = turtle.Turtle()
text_box = turtle.Turtle()
text.hideturtle()
texxt = turtle.Turtle()
sccore = turtle.Turtle()
texxt.hideturtle()
turtle.register_shape("rec.gif")
text_box.shape("rec.gif")
text_box.penup()
text_box.hideturtle()
text_box.goto(0,190)
text_box.showturtle()
turtle.register_shape("pick.gif")
turtle.register_shape("pick1.gif")
turtle.register_shape("like.gif")
turtle.register_shape("pick2.gif")
turtle.register_shape("pick3.gif")
turtle.register_shape("pick4.gif")
turtle.register_shape("pick5.gif")
turtle.register_shape("win.gif")
turtle.bgpic("pick.gif")
turtle.shape("like.gif")
turtle.hideturtle()
turtle.penup()
sccore.penup()
sccore.hideturtle()
turtle.goto(180,30)
sccore.goto(170,50)
text.penup()
text.goto(-310,179)
text.speed(0)
texxt.speed(0)
texxt.penup()
text.color("sienna")
texxt.color("gold")
texxt.goto(-80,-179)
texxt.write("Left button = False and Right button = True.", move = False, align = "left", font=("arial",15,"normal"))
global go
go = ["pick.gif", "pick1.gif", "pick5.gif", "pick2.gif",  "pick3.gif" ,  "pick4.gif"]
quests = ["coal energy is a type of renewable energy?","LED lights are more energy efficient than incandescent light bulbs?",\
          "Combustion engines are more efficient than electric motors?", "Wind energy is the most reliable type of energy?"\
          , "A quarter of all the world’s energy comes from renewable energy?", "Global warming is just a part of earth’s 'homeostasis'"\
          ,"Climate change leads to habitat loss for many animals?", "There are no countries that run on more than 95% renewable energy?"\
          ,"Climate change has lead to the destruction of most coral reefs?", "Glass bottles take thousands of years to decompose?"\
          ,"Humans use 1 trillion plastic bags a year!?", "America produces 15% of the world’s carbon emissions?"\
          ,"Going on public transport is bad for the environment?", "Climate change is irreversible?", "Climate change will not be a problem until 2060?"
          ,"Water is an element?"\
          , "Americans recycle 50% of their paper waste products?", "Deforestation contributes positively to Climate change?"\
          ,"The Atlantic ocean is the biggest ocean?", "You can’t do much to reduce the amount of trash you make?"]
answer = ["false","true","false","false", "true", "false", "true", "false", "true","true", "true", "false", "false", "false"\
          , "false", "false", "true", "false", "false", "false"]
global x
x = -1
global quest
quest = "false"
global y
y = -1
global z
z = -1


score = 0

def background():
    global x
    global y
    global z
    global pic
    pic = "0"
    
    if quest == "false":
        a=go[x+1]
        turtle.bgpic(a)
        x += 1
        text.clear()
        text.write(quests[z+1], move=False, align="left", font=("Arial",15,"normal"))
        z += 1
        if z >= 1 and z < 6:
            mixer.init()
            mixer.music.load("oof.mp3")
            mixer.music.play()
            time.sleep(1)
            mixer.init()
            mixer.music.load("bob.mp3")
            mixer.music.play()


    if quest == "true":
        turtle.showturtle()
        time.sleep(1.5)
        turtle.hideturtle()
        text.clear()
        text.write(quests[z+1], move=False, align="left", font=("Arial",15,"normal"))
        z += 1

    pic = turtle.bgpic()
    if pic == "pick4.gif":
        mixer.init()
        mixer.music.load("bomb.mp3")
        mixer.music.play()
        text.clear()
        print("earth exploded")
        quit()
    if score >= 16:
        mixer.init()
        mixer.music.load("victory.mp3")
        mixer.music.play()
        text.clear()
        sccore.clear()
        texxt.clear()
        text_box.hideturtle()
        turtle.clear()
        turtle.bgpic("win.gif")
        

background()
def right():
    global y
    quest = "true"
    if quest == answer[y+1]:
        y += 1
        true()
    else:
        y += 1
        false()

def left():
    global y
    quest = "false"
    if quest == answer[y+1]:
        y += 1
        true()
    else:
        y += 1
        false()

def true():
    global quest
    global score
    quest = "true"
    score += 1
    sccore.clear()
    sccore.write("SCORE: " + str(score), move = False, align = "left", font=("Arial", 20, "normal"))
    background()

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()


def false():
    global quest
    quest = "false"
    background()


turtle.mainloop()
