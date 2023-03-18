import turtle as t



t.pen(speed=100)

for i in range(4):
    t.color("black")
    t.pensize(3)
    t.forward(100)
    t.left(95)

    for i in range(36):
        t.pensize(0.5)
        t.color("red")
        t.circle(50)
        t.left(10)







t.mainloop()