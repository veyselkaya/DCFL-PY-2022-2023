import turtle as t




t.speed(100)

for i in range(8):
    for i in range(2):
        for colors in ["red", "lime", "yellow", "white", "indigo", "magenta", "green", "brown"]:
            t.color(colors)
            for i in range(4):
                t.forward(50)
                t.left(91)
    t.penup()
    t.forward(100)
    t.pendown()


t.mainloop()