import turtle
import time
turtle.setup(640,400)
text = turtle.Turtle()
text.hideturtle()
turtle.register_shape("boom.gif")
turtle.register_shape("pick.gif")
turtle.register_shape("pick1.gif")
turtle.register_shape("like.gif")
turtle.bgpic("pick.gif")
turtle.shape("like.gif")
turtle.hideturtle()
turtle.penup()
turtle.goto(200,50)
global go
go = ["pick.gif", "pick1.gif", "boom.gif"]
quests = ["quest","hi","boom"]
answer = ["true","true","true"]
global x
x = -1
global quest
quest = "false"
global y
y = -1
global z
z = -1
text.goto(-30,-50)



def background():
    global x
    global y
    global z
    global pic
    pic = "0"
    print(quest)
    
    if quest == "false":
        a=go[x+1]
        turtle.bgpic(a)
        x += 1
        text.clear()
        text.write(quests[z+1], move=False, align="left", font=("Arial",40,"normal"))
        z += 1
    if quest == "true":
        turtle.showturtle()
        time.sleep(2)
        turtle.hideturtle()
        text.clear()
        text.write(quests[z+1], move=False, align="left", font=("Arial",40,"normal"))
        z += 1

    pic = turtle.bgpic()
    if pic == "boom.gif":
        print("earth exploded")
        quit()

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
    quest = "true"
    background()

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()


def false():
    global quest
    quest = "false"
    background()


turtle.mainloop()
