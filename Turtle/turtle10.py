import turtle as t


t.speed(100)


for i in range(12):
    t.left(30)
    t.begin_fill()
    t.fillcolor("indigo")

    for i in range(4):
        t.forward(100)
        t.left(90)

    t.end_fill()

t.mainloop()