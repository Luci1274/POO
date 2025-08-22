import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.speed(0)
t.color("red")

t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(113)

for _ in range(200):
    t.right(1)
    t.forward(1)

t.left(120)

for _ in range(200):
    t.right(1)
    t.forward(1)

t.forward(112)

t.end_fill()
t.setpos(0, -22)
t.color("white")
t.hideturtle()
t.write("I Love You", align="center", font=("Arial", 20, "bold"))
input("Press Enter to exit")