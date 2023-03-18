import turtle as t


t.bgcolor("black")


t.speed(100)


for i in range(10):
    t.color("red")
    t.forward(100)
    t.left(36)

    for i in range(3):
        t.color("yellow")
        t.forward(50)
        t.left(120)


t.mainloop()