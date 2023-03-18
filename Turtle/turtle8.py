import turtle as t


t.bgcolor("black")


t.speed(100)


for i in range(10):
    t.color("red")
    t.circle(100)
    t.left(36)

    for i in range(4):
        t.color("yellow")
        t.forward(50)
        t.left(90)


t.mainloop()