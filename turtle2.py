import turtle as tt
import random as r

tt.speed(10)
tt.color("red")
renkler = ["red","green","blue"]

for aa in range(10):
    tt.color(r.choice(renkler))
    tt.penup()
    tt.goto(r.randint(-200,200),r.randint(-100,300))
    tt.pendown()
    kenaru = r.randint(10,150)
    for a in range(4):
        tt.forward(50)
        tt.right(90)
